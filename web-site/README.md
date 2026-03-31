# Event Resources Website - S3 + CloudFront (AWS CDK)

Deploy a static event resources website to **Amazon S3** with **CloudFront** as CDN, using **AWS CDK** (Python).

## Prerequisites

Before you begin, make sure you have:

1. **An AWS Account** - [Create one here](https://aws.amazon.com/free/) if you don't have one
2. **AWS CLI** installed and configured - [Installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
3. **Node.js** (v18 or later) - [Download here](https://nodejs.org/)
4. **Python 3.9+** - [Download here](https://www.python.org/downloads/)
5. **AWS CDK CLI** - Install it globally:
   ```bash
   npm install -g aws-cdk
   ```

## How It Works

```
event_config.json  -->  index.html (reads JSON)  -->  S3 Bucket  -->  CloudFront  -->  Your audience
```

- Your website files (`index.html`, `styles.css`, `event_config.json`, images) are uploaded to an **S3 bucket**
- **CloudFront** serves them globally with HTTPS
- You only need to edit `event_config.json` to customize the page for each event

## Step 1 - Configure Your Event

Edit `website/event_config.json` with your event details:

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

Place speaker photos in the `website/img/` folder and reference them in the config:

```json
"image": "img/your-photo.jpeg"
```

## Step 2 - Test Locally

Preview your site in the browser before deploying:

```bash
cd website
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

## Step 3 - Configure AWS Credentials

If you haven't configured AWS CLI yet:

```bash
aws configure
```

It will ask for:
- **AWS Access Key ID** - Get it from [IAM Console](https://console.aws.amazon.com/iam/) > Users > Security credentials
- **AWS Secret Access Key** - Same place as above
- **Default region** - e.g., `us-east-1`
- **Output format** - `json`

## Step 4 - Set Up the Project

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 5 - Bootstrap CDK (First Time Only)

If this is your first time using CDK in this AWS account/region:

```bash
cdk bootstrap
```

This creates the resources CDK needs to deploy. You only need to do this once per account/region. [Learn more about CDK bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html).

## Step 6 - Deploy

```bash
cdk deploy
```

CDK will show you the resources it will create and ask for confirmation. Type `y` to proceed.

When the deployment finishes, you will see the **CloudFront URL** in the output:

```
Outputs:
WebSiteStack.WebsiteURL = https://d1234abcdef.cloudfront.net
```

That URL is your live event resources page.

## Updating Your Event

To update the page for a new event:

1. Edit `website/event_config.json` with the new event details
2. Replace images in `website/img/` if needed
3. Run `cdk deploy` again

## Clean Up

To remove all resources and avoid charges:

```bash
cdk destroy
```

## Project Structure

```
web-site/
  app.py                    # CDK app entry point
  cdk.json                  # CDK configuration
  requirements.txt          # Python dependencies
  event_config.json         # Legacy config (not used by the website)
  web_site/
    web_site_stack.py       # CDK stack (S3 + CloudFront)
  website/
    index.html              # Main page
    styles.css              # Styles
    event_config.json       # Event data (edit this)
    img/                    # Speaker photos and icons
    presentation-deck.pdf   # Presentation deck
```

## Useful CDK Commands

| Command | Description |
|---------|-------------|
| `cdk synth` | Generate the CloudFormation template without deploying |
| `cdk diff` | See what changes will be applied |
| `cdk deploy` | Deploy the stack |
| `cdk destroy` | Delete all resources |
| `cdk docs` | Open CDK documentation |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `cdk: command not found` | Run `npm install -g aws-cdk` |
| `Unable to resolve AWS account` | Run `aws configure` and set your credentials |
| `CDK bootstrap required` | Run `cdk bootstrap` first |
| Page shows old content after deploy | Wait a few minutes for CloudFront cache to update, or run an invalidation |

## Cost

This runs at zero cost under [AWS Free Tier](https://aws.amazon.com/free/):

- **Amazon S3**: 5 GB storage, 20,000 GET requests/month
- **Amazon CloudFront**: 1 TB data transfer, 10M requests/month

For detailed pricing: [S3 Pricing](https://aws.amazon.com/s3/pricing/) | [CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/) | [AWS Pricing Calculator](https://calculator.aws)
