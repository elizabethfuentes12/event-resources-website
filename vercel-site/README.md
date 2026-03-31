# Event Resources Website - Vercel

Deploy a static event resources website with **Vercel**. Push to GitHub and Vercel deploys automatically.

## Prerequisites

Before you begin, make sure you have:

1. **A Vercel Account** - [Create one here](https://vercel.com/signup) (free tier available, you can sign up with GitHub)
2. **A GitHub Account** - [Create one here](https://github.com/signup)
3. **Git** installed - [Download here](https://git-scm.com/downloads)

No AWS account, Node.js, or Python required for deployment. Vercel handles everything.

## How It Works

```
Push to GitHub  -->  Vercel detects change  -->  Deploys  -->  Your audience
```

- You push your code to a GitHub repository
- **Vercel** detects the push and automatically deploys the site
- The `vercel.json` file configures routing and headers
- You only need to edit `event_config.json` to customize the page for each event

## Step 1 - Fork or Clone This Repository

Go to this repository on GitHub and click **Fork**, or clone it:

```bash
git clone https://github.com/YOUR-USERNAME/event-resources-website.git
cd event-resources-website
```

## Step 2 - Configure Your Event

Edit `vercel-site/event_config.json` with your event details:

```json
{
  "event": {
    "name": "Your Event Name",
    "date": "April 15, 2026",
    "location": "City, Country",
    "description": "What the event is about",
    "tags": ["Topic 1", "Topic 2"]
  },
  "speakers": [
    {
      "name": "Speaker Name",
      "title": "Speaker Title",
      "image": "img/profile.jpeg",
      "social_links": [
        {
          "name": "LinkedIn",
          "url": "https://www.linkedin.com/in/your-profile/",
          "icon": "img/link.png"
        }
      ]
    }
  ],
  "resources": [
    {
      "title": "Resource Title",
      "description": "What this resource is",
      "url": "https://example.com",
      "type": "link",
      "highlight": false
    }
  ]
}
```

### Resource Types

| Type | Icon | Use for |
|------|------|---------|
| `link` | External link | General URLs |
| `github` | GitHub logo | Repositories |
| `article` | Book | Blog posts, docs |
| `pdf` | Document | Presentation decks |
| `survey` | Clipboard | Feedback forms (highlighted in green) |

### Speaker Images

Place speaker photos in the `vercel-site/img/` folder and reference them in the config:

```json
"image": "img/your-photo.jpeg"
```

## Step 3 - Test Locally

Preview your site in the browser before deploying:

```bash
cd vercel-site
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

### (Optional) Test with Vercel CLI

If you want to test with the Vercel development server:

```bash
npm install -g vercel
cd vercel-site
vercel dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Step 4 - Push to GitHub

```bash
git add .
git commit -m "Configure event resources page"
git push origin main
```

## Step 5 - Deploy with Vercel

### Option A - Vercel Dashboard (Recommended for beginners)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click **Import Git Repository**
3. Select your GitHub repository
4. In the configuration:
   - Set **Root Directory** to `vercel-site`
   - **Framework Preset**: select `Other`
   - Leave build settings empty (it is a static site, no build needed)
5. Click **Deploy**

Vercel will deploy your site and give you a URL like:

```
https://your-project.vercel.app
```

### Option B - Vercel CLI

If you prefer the command line:

```bash
npm install -g vercel
cd vercel-site
vercel
```

Follow the prompts. Vercel will deploy and give you a URL.

### Custom Domain (Optional)

To use your own domain:

1. Go to your project in the [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **Settings** > **Domains**
3. Add your domain and follow the DNS instructions

[Vercel Custom Domains documentation](https://vercel.com/docs/projects/domains)

## Updating Your Event

To update the page for a new event:

1. Edit `vercel-site/event_config.json` with the new event details
2. Replace images in `vercel-site/img/` if needed
3. Commit and push:
   ```bash
   git add .
   git commit -m "Update event resources"
   git push
   ```
4. Vercel deploys automatically in seconds

## Clean Up

To remove the Vercel project:

1. Go to the [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Go to **Settings** > **General**
4. Scroll to the bottom and click **Delete Project**

## Project Structure

```
vercel-site/
  vercel.json             # Vercel configuration (routing, headers)
  index.html              # Main page
  styles.css              # Styles
  event_config.json       # Event data (edit this)
  img/                    # Speaker photos and icons
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `vercel: command not found` | Run `npm install -g vercel` |
| Build fails on Vercel | Make sure **Root Directory** is set to `vercel-site` |
| Images don't load | Verify the image paths in `event_config.json` match the files in `img/` |
| Page shows old content | Check the Vercel Dashboard for deployment status (deploys in seconds) |
| 404 on subpages | Make sure `vercel.json` exists in the root of `vercel-site/` |
