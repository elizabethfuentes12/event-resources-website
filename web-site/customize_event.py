#!/usr/bin/env python3
"""
Script to customize the website for each event
"""

import json
import os
from pathlib import Path

def customize_website(config_file="event_config.json"):
    """Customize the website based on event configuration"""
    
    # Load configuration
    if not os.path.exists(config_file):
        print(f"Configuration file {config_file} not found.")
        create_sample_config(config_file)
        return
    
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Read HTML template
    template_path = Path("website/index.html")
    with open(template_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Replace event info
    html_content = html_content.replace(
        "AWS Community Day | August 30, 2024 | New York City",
        f"{config['event_name']} | {config['date']} | {config['city']}"
    )
    
    # Update LinkedIn profile image
    if 'linkedin_profile_image' in config:
        html_content = html_content.replace(
            'src="https://media.licdn.com/dms/image/v2/D4E03AQHQbOe7VxCGpA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1724173071138?e=1730332800&v=beta&t=YourLinkedInImageToken"',
            f'src="{config["linkedin_profile_image"]}"'
        )
    
    # Update PDF link
    if 'deck_pdf' in config:
        html_content = html_content.replace(
            'href="presentation-deck.pdf"',
            f'href="{config["deck_pdf"]}"'
        )
    
    # Update other links
    html_content = html_content.replace(
        'href="https://forms.gle/your-credits-survey-here"',
        f'href="{config["credits_url"]}"'
    )
    
    html_content = html_content.replace(
        'href="https://forms.gle/your-survey-here"',
        f'href="{config["survey_url"]}"'
    )
    
    html_content = html_content.replace(
        'href="https://github.com/your-username/your-demo"',
        f'href="{config["demo_url"]}"'
    )
    
    # Update social links
    for social, url in config["social_links"].items():
        old_pattern = f'href="https://www.linkedin.com/in/lizfue/"' if social == 'linkedin' else \
                     f'href="https://twitter.com/ElizabethFue12"' if social == 'twitter' else \
                     f'href="https://github.com/elizabethfuentes12"' if social == 'github' else \
                     f'href="https://www.youtube.com/channel/UCr0Gnc-t30m4xyrvsQpNp2Q?sub_confirmation=1"' if social == 'youtube' else \
                     f'href="https://www.instagram.com/elifue.tech"' if social == 'instagram' else None
        
        if old_pattern:
            html_content = html_content.replace(old_pattern, f'href="{url}"')
    
    # Save updated file
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Website customized for: {config['event_name']}")
    print(f"📄 PDF deck: {config.get('deck_pdf', 'Not configured')}")
    print(f"🖼️  Profile image: {'Configured' if 'linkedin_profile_image' in config else 'Not configured'}")

def create_sample_config(filename):
    """Create a sample configuration file"""
    sample_config = {
        "event_name": "API World + CloudX + DataWeek 2025",
        "date": "September 03, 2025",
        "city": "Santa Clara",
        "credits_url": "https://forms.gle/your-credits-survey-here",
        "survey_url": "https://forms.gle/your-survey-here",
        "demo_url": "https://github.com/your-username/your-demo",
        "deck_pdf": "presentation-deck.pdf",
        "linkedin_profile_image": "https://media.licdn.com/dms/image/v2/YOUR_LINKEDIN_IMAGE_URL",
        "social_links": {
            "linkedin": "https://www.linkedin.com/in/lizfue/",
            "twitter": "https://twitter.com/ElizabethFue12",
            "github": "https://github.com/elizabethfuentes12",
            "youtube": "https://www.youtube.com/channel/UCr0Gnc-t30m4xyrvsQpNp2Q?sub_confirmation=1",
            "instagram": "https://www.instagram.com/elifue.tech"
        }
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(sample_config, f, indent=2, ensure_ascii=False)
    
    print(f"📝 Configuration file created: {filename}")
    print("Edit this file with your event data and run the script again.")

if __name__ == "__main__":
    customize_website()
