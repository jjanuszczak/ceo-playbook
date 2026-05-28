# Plan: Design Sticky Notification Bar Shortcode

## Objective
Create a reusable Hugo shortcode for a sticky notification/announcement bar that can be embedded in specific posts.

## Proposed Solution
- Create a new shortcode template: `layouts/shortcodes/notification-bar.html`
- Style the component using Tailwind classes (consistent with Blowfish theme).
- Parameters:
    - `message`: Text content.
    - `link`: Optional URL.
    - `type`: Optional styling variants (e.g., `info`, `warning`, `success`).

## Implementation Steps
1.  **Draft Shortcode:** Write `layouts/shortcodes/notification-bar.html`.
2.  **Define Styles:** Ensure Tailwind classes match the site's design system.
3.  **Documentation:** Provide a brief usage example for the user.

## Verification
- Add the shortcode to a test post.
- Run `hugo server -D` to verify the bar appears correctly.
