# Newsletter Automation Guide: RSS-to-Email

This guide explains how to automatically trigger emails to your subscribers whenever new content is published to the **Signals** section of `ceo-playbook.com`.

## 1. The Core Engine: RSS Feed
Hugo automatically generates a machine-readable "Feed" of your content. Kit monitors this feed and creates an email whenever a new entry appears.

*   **Signals RSS URL:** `https://ceo-playbook.com/signals/index.xml`
*   **Articles RSS URL:** `https://ceo-playbook.com/articles/index.xml`

## 2. Setting Up the Automation in Kit
1.  **Log in to Kit:** Go to your dashboard at [app.kit.com](https://app.kit.com).
2.  **Create the Feed:** Navigate to **Automate** > **RSS**.
3.  **Connect the URL:** Click **New RSS Feed** and paste the Signals RSS URL above.
4.  **Verify:** Click **Check Feed** to ensure Kit can see your recent posts.

## 3. Email Configuration (The "Single Post" Strategy)
To ensure each new Signal gets its own high-impact email, use these settings in the Kit RSS editor:

*   **Format:** Select **Single** (instead of Digest).
*   **Delivery Mode:** 
    *   **Manual (Recommended for launch):** Kit creates a "Draft" Broadcast. you log in, review, and hit "Send."
    *   **Automatic:** Kit sends the email immediately after it detects the new post (usually within 1 hour).
*   **Subject Line:** Use the `{{ rss_item_title }}` tag to use your Signal's title as the email subject.

## 4. Designing the Content Template
To maintain your executive brand, keep the email template minimal. In the Kit email editor, use these liquid tags:

```html
<!-- The Email Body -->
{{ rss_item_description }}

<!-- The Call to Action -->
<p>
  <a href="{{ rss_item_url }}" style="background-color: #1677be; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold;">
    Read the Full Signal
  </a>
</p>
```

*Note: The `{{ rss_item_description }}` tag automatically pulls the `summary` field from your Hugo frontmatter.*

## 5. Maintenance: Writing for the Feed
For every new Signal or Article, ensure your Frontmatter includes a `summary`. This is what appears in the subscriber's inbox.

**Example Frontmatter:**
```yaml
---
title: "Signals: Week 11, 2026"
date: 2026-03-15
summary: "A 1-2 sentence hook that explains why the C-Suite should care about this week's briefing."
---
```

## 6. Troubleshooting
*   **Emails not sending?** Ensure your site is actually live and the RSS URL is reachable in a browser.
*   **Content looks wrong?** Kit caches the RSS feed. If you fix a typo in Hugo and re-push, it may take an hour for Kit to see the update.
