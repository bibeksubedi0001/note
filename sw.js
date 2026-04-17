/* ============================================================
   Study Notes — Service Worker
   Strategy:
     • Navigations (HTML): network-first, fall back to cache, then
       fall back to a cached copy of the originating page / root.
     • Same-origin static assets (CSS/JS/img/fonts): stale-while-
       revalidate — instant from cache, refreshed in background.
     • Cross-origin (MathJax CDN etc.): cache-first with background
       refresh so the site still renders offline once visited.
   Everything is cached on first visit, so reloading offline works.
   ============================================================ */

const VERSION       = 'v1.0.0';
const RUNTIME_CACHE = `studynotes-runtime-${VERSION}`;
const PRECACHE      = `studynotes-precache-${VERSION}`;

// Minimal precache so the site shell works offline from the start.
const PRECACHE_URLS = [
  './',
  './index.html',
  './index-style.css',
  './common.js'
];

self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(PRECACHE).then((cache) =>
      // Use {cache:'reload'} to bypass HTTP cache on install.
      Promise.all(
        PRECACHE_URLS.map((u) =>
          cache.add(new Request(u, { cache: 'reload' })).catch(() => null)
        )
      )
    )
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    (async () => {
      const keys = await caches.keys();
      await Promise.all(
        keys
          .filter((k) => k !== RUNTIME_CACHE && k !== PRECACHE)
          .map((k) => caches.delete(k))
      );
      await self.clients.claim();
    })()
  );
});

// Allow pages to trigger an update immediately.
self.addEventListener('message', (event) => {
  if (event.data === 'SKIP_WAITING') self.skipWaiting();
});

function isHTMLRequest(request) {
  if (request.mode === 'navigate') return true;
  const accept = request.headers.get('accept') || '';
  return accept.includes('text/html');
}

async function networkFirst(request) {
  const cache = await caches.open(RUNTIME_CACHE);
  try {
    const fresh = await fetch(request);
    if (fresh && fresh.ok && request.method === 'GET') {
      cache.put(request, fresh.clone()).catch(() => {});
    }
    return fresh;
  } catch (err) {
    const cached = await cache.match(request, { ignoreSearch: true });
    if (cached) return cached;
    // Last-resort fallback: cached root page.
    const root = await cache.match('./') || await cache.match('./index.html');
    if (root) return root;
    throw err;
  }
}

async function staleWhileRevalidate(request) {
  const cache = await caches.open(RUNTIME_CACHE);
  const cached = await cache.match(request);
  const network = fetch(request)
    .then((resp) => {
      if (resp && (resp.ok || resp.type === 'opaque') && request.method === 'GET') {
        cache.put(request, resp.clone()).catch(() => {});
      }
      return resp;
    })
    .catch(() => null);
  return cached || (await network) || Response.error();
}

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);

  // Skip non-http(s) schemes (chrome-extension:, data:, etc.)
  if (url.protocol !== 'http:' && url.protocol !== 'https:') return;

  if (isHTMLRequest(req)) {
    event.respondWith(networkFirst(req));
    return;
  }

  event.respondWith(staleWhileRevalidate(req));
});
