const CACHE_NAME = 'crimeDetect-pwa-cache';
const offlinePage = '/staticfiles/offline.html';

self.addEventListener('install', event => {
    console.log('Service Worker installed');

    event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
        return cache.addAll([
        '/',
        '/staticfiles/images/crimeDetect_icon.png',
        offlinePage,
        ]);
    })
  );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    console.log('Fetch event:', event.request.url);

    event.respondWith(
        caches.match(event.request)
            .then(response => {
                console.log('Cached response:', response);
                return response || fetch(event.request);
            })
            .catch(() => {
                console.log('Fetching offline page');
                return caches.match(offlinePage);
            })
    );
});
