# Static deployment notes

Muse Alert is designed for GitHub Pages behind Cloudflare Pages/Workers. The `site/` directory is static HTML/CSS and can be served without a Node build. Keep every public button and redirect pointed to an `.html` page so static hosting has a clear destination.

## Payment safety

The payment page includes an 18+ disclosure gate and provider widgets. Client-side age gates are only a UX gate, not legal verification. Before production: move entitlement verification server-side, configure provider webhooks, protect secrets, validate origin/return URLs, add terms/refund/privacy links, and obtain legal review.

Ko-fi has intentionally not been embedded. A community page is used instead of a raw Discord widget so links remain centered and reviewable.
