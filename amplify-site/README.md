# Event Resources Website - AWS Amplify

Deploy a static event resources website with **AWS Amplify Hosting**. Push to GitHub and Amplify deploys automatically.

## Prerequisites

Before you begin, make sure you have:

1. **An AWS Account** - [Create one here](https://aws.amazon.com/free/) if you don't have one
2. **A GitHub Account** - [Create one here](https://github.com/signup)
3. **Git** installed - [Download here](https://git-scm.com/downloads)

No local tooling (Node.js, Python, CDK) is required. Amplify handles the build and deploy.

## How It Works

```
Push to GitHub  -->  Amplify detects change  -->  Builds & deploys  -->  Your audience
```

- You push your code to a GitHub repository
- **AWS Amplify** detects the push and automatically deploys the site
- The `amplify.yml` file tells Amplify which folder to serve
- You only need to edit `event_config.json` to customize the page for each event

## Step 1 - Fork or Clone This Repository

Go to this repository on GitHub and click **Fork**, or clone it:

```bash
git clone https://github.com/YOUR-USERNAME/event-resources-website.git
cd event-resources-website
```

## Step 2 - Configure Your Event

Edit `amplify-site/event_config.json` with your event details:

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

Place speaker photos in the `amplify-site/img/` folder and reference them in the config:

```json
"image": "img/your-photo.jpeg"
```

## Step 3 - Test Locally

Preview your site in the browser before deploying:

```bash
cd amplify-site
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

## Step 4 - Push to GitHub

```bash
git add .
git commit -m "Configure event resources page"
git push origin main
```

## Step 5 - Connect to AWS Amplify

1. Go to the [AWS Amplify Console](https://console.aws.amazon.com/amplify/)
2. Click **New app** > **Host web app**
3. Select **GitHub** as the source provider
4. Authorize AWS Amplify to access your GitHub account (you will see a GitHub authorization popup)
5. Select your **repository** and **branch** (usually `main`)
6. In the build settings:
   - Set **App root** to `amplify-site`
   - Amplify will detect the `amplify.yml` file automatically
7. Click **Save and deploy**

Amplify will build and deploy your site. When it finishes, you will get a URL like:

```
https://main.d1234abcdef.amplifyapp.com
```

### Custom Domain (Optional)

To use your own domain:

1. In the Amplify Console, go to **Domain management**
2. Click **Add domain**
3. Follow the instructions to verify DNS ownership

[Amplify Custom Domains documentation](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html)

## Updating Your Event

To update the page for a new event:

1. Edit `amplify-site/event_config.json` with the new event details
2. Replace images in `amplify-site/img/` if needed
3. Commit and push:
   ```bash
   git add .
   git commit -m "Update event resources"
   git push
   ```
4. Amplify deploys automatically in about 1 minute

## Clean Up

To remove the Amplify app and stop charges:

1. Go to the [AWS Amplify Console](https://console.aws.amazon.com/amplify/)
2. Select your app
3. Go to **App settings** > **General**
4. Click **Delete app**

## Project Structure

```
amplify-site/
  amplify.yml             # Amplify build configuration
  index.html              # Main page
  styles.css              # Styles
  event_config.json       # Event data (edit this)
  img/                    # Speaker photos and icons
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Amplify build fails | Check that **App root** is set to `amplify-site` in the build settings |
| Page looks broken | Make sure `amplify.yml` exists in the `amplify-site/` folder |
| Images don't load | Verify the image paths in `event_config.json` match the files in `img/` |
| Changes not showing | Check the Amplify Console for deployment status (takes about 1 minute) |
