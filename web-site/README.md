# Event Resources Website

A customizable static website deployed on Amazon S3 + Amazon CloudFront for sharing event resources with attendees. Perfect for speakers who want to share AWS account creation links, surveys, demo repositories, and social media links after presentations.

## 🚀 Features

- **Static Website**: Fast, secure, and cost-effective
- **JSON Configuration**: Configure each event through a single JSON file
- **Professional Design**: Responsive design with AWS branding
- **CDK Deployment**: Infrastructure as Code with AWS CDK
- **Private Repository**: Deploy without making your repo public
- **Social Media Integration**: LinkedIn, Twitter, GitHub, YouTube, Instagram
- **AWS Credits Section**: Highlighted section for free AWS credits survey

## 📁 Project Structure

```
web-site/
├── website/                 # Static website files
│   ├── index.html          # Main HTML template
│   └── styles.css          # CSS styles
├── web_site/               # CDK stack
│   └── web_site_stack.py   # S3 + CloudFront infrastructure
├── customize_event.py      # Event customization script
├── event_config.json       # Event configuration
├── app.py                  # CDK app entry point
└── requirements.txt        # Python dependencies
```

## 🛠️ Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Configure AWS credentials:**
```bash
aws configure
```

3. **Bootstrap CDK (first-time setup only):**
```bash
cdk bootstrap
```

## 📝 Customization

1. **Edit event configuration:**
Edit `event_config.json` with your event details:
```json
{
  "event_name": "Your Event Name",
  "date": "Event Date",
  "city": "Event City",
  "credits_url": "https://forms.gle/your-credits-survey",
  "survey_url": "https://forms.gle/your-feedback-survey",
  "demo_url": "https://github.com/your-username/your-demo",
  "deck_pdf": "your-presentation.pdf",
  "linkedin_profile_image": "https://your-profile-image-url",
  "social_links": {
    "linkedin": "https://linkedin.com/in/your-profile",
    "twitter": "https://twitter.com/your-username",
    "github": "https://github.com/your-username",
    "youtube": "https://youtube.com/@your-channel",
    "instagram": "https://instagram.com/your-username"
  }
}
```

2. **Apply customization:**
```bash
python3 customize_event.py
```

## 🚀 Deployment

1. **Deploy the stack:**
```bash
cdk deploy
```

2. **Get your website URL:**
The CloudFront URL appears in the output after deployment.

## 🔄 Updating for New Events

1. Update `event_config.json` with new event details
2. Run `python3 customize_event.py`
3. Deploy changes: `cdk deploy`

## 🔧 CDK Commands

- `cdk ls` - List all stacks
- `cdk synth` - Synthesize CloudFormation template
- `cdk deploy` - Deploy the stack
- `cdk diff` - Compare deployed stack with current state
- `cdk destroy` - Remove the stack

## 💡 Benefits

- **Private Repository**: Your code stays private
- **Fast Loading**: CloudFront CDN provides global performance
- **Cost Effective**: S3 + CloudFront costs minimal amounts per month
- **Professional Design**: Clean, responsive layout
- **Quick Updates**: JSON configuration for rapid changes
- **Secure**: HTTPS by default with CloudFront
