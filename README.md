# Event Resources Website

A customizable static website deployed on [Amazon S3](https://aws.amazon.com/s3/) + [Amazon CloudFront](https://aws.amazon.com/cloudfront/) for sharing event resources with attendees. Perfect for speakers who want to share account creation links, surveys, demo repositories, and social media links after presentations.

## 🎯 Why Share Resources at Events?

Sharing resources effectively at events is crucial for:
- **Attendee Engagement**: Provide immediate access to valuable content while interest is high
- **Follow-up Connection**: Maintain engagement beyond the event through social media and demos
- **Learning Continuity**: Enable attendees to continue exploring topics covered in your presentation
- **Professional Networking**: Share your professional profiles for ongoing connections
- **Feedback Collection**: Gather valuable insights to improve future presentations

## 🚀 Features

- **Static Website**: Fast, secure, and cost-effective
- **Easy Customization**: JSON-based configuration for each event
- **Professional Design**: Responsive design with clean branding
- **CDK Deployment**: Infrastructure as Code with AWS CDK
- **Private Repository**: Deploy without making your repo public
- **Social Media Integration**: LinkedIn, Twitter, GitHub, YouTube, Instagram
- **Credits Section**: Highlighted section for free credits or special offers

## 🛠️ Built with AWS CDK

This application uses **[AWS Cloud Development Kit (CDK)](https://docs.aws.amazon.com/cdk/)** - a software development framework for defining cloud infrastructure in code. CDK allows you to:
- Define infrastructure using familiar programming languages
- Leverage the power of programming constructs like loops, conditions, and functions
- Use IDE features like auto-complete and inline documentation
- Apply software engineering practices to infrastructures

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

3. **Bootstrap CDK (first time only):**
```bash
cdk bootstrap
```

## 📝 Customization

1. **Edit event configuration:**
```bash
# Edit event_config.json with your event details
{
  "event_name": "Your Event Name",
  "date": "Event Date",
  "city": "Event City",
  "credits_url": "https://forms.gle/your-credits-survey",
  "survey_url": "https://forms.gle/your-feedback-survey",
  "demo_url": "https://github.com/your-username/your-demo",
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
The CloudFront URL will be displayed in the output after deployment.

## 🔄 Updating for New Events

1. Update `event_config.json` with new event details
2. Run `python3 customize_event.py`
3. Deploy changes: `cdk deploy`

## 💰 AWS Credits Section

The website includes a highlighted section for AWS credits that attendees can obtain by completing a survey. This section:
- Has a distinctive golden background with animation
- Appears first in the resources list
- Links to your credits survey URL

## 🎨 Website Sections

- **AWS Credits**: Get free AWS credits by completing survey
- **Create AWS Account**: Direct link to AWS Free Tier
- **Event Survey**: Feedback collection
- **Project Demo**: Link to your demo repository
- **Social Media**: All your social profiles

## 🔧 CDK Commands

- `cdk ls` - List all stacks
- `cdk synth` - Synthesize CloudFormation template
- `cdk deploy` - Deploy the stack
- `cdk diff` - Compare deployed stack with current state
- `cdk destroy` - Remove the stack

## 💰 AWS Free Tier & Costs

This application can run at **zero cost** under AWS Free Tier:

- **Amazon S3**: 5 GB of storage, 20,000 GET requests, 2,000 PUT requests per month
- **Amazon CloudFront**: 1 TB of data transfer out, 10,000,000 HTTP/HTTPS requests per month

For a typical event resources website (few MB of static files), you'll likely stay within free tier limits.

**After Free Tier or for higher usage:**
- S3: ~$0.023 per GB stored per month
- CloudFront: ~$0.085 per GB transferred

For detailed pricing information:
- [S3 Pricing](https://aws.amazon.com/s3/pricing/)
- [CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/)
- [AWS Pricing Calculator](https://calculator.aws)

## 💡 Benefits

- **No Public Repository**: Your code stays private
- **Fast Loading**: CloudFront CDN ensures global performance
- **Cost Effective**: Zero cost with Free Tier, pennies per month otherwise
- **Professional**: Clean, responsive design
- **Easy Updates**: JSON configuration for quick changes
- **Secure**: HTTPS by default with CloudFront

## 🔒 Security

- Repository remains private
- HTTPS enforced via CloudFront
- S3 bucket configured with appropriate public access settings
- No sensitive data in the website code

## 📱 Responsive Design

The website is fully responsive and works perfectly on:
- Desktop computers
- Tablets
- Mobile phones

Perfect for attendees accessing the resources on any device during or after your presentation.
