# QR Code Generator

Generate QR codes for your event resources website URL to share with attendees.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Open the Jupyter notebook:
```bash
jupyter notebook qr_code_generator.ipynb
```

## Usage

1. Replace `website_url` with your CloudFront URL from CDK deployment
2. Update `event_name` with your event details
3. Run all cells to generate and save QR codes

## Output

- Standard QR code for digital sharing
- High-resolution QR code for printing
- Both saved as PNG files with event name and date
