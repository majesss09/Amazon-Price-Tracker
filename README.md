# Amazon Price Tracker

A simple Python script that checks the price of a specific Amazon product and sends
an email alert if the price drops below a defined threshold. Ideal for learning web
scraping, environment variable handling, and basic SMTP email notifications.

## Features

- Fetches product page using `requests`.
- Parses price information with `BeautifulSoup`.
- Compares current price against `TARGET_PRICE` constant.
- Sends an email via SMTP when price condition is met.
- Credentials and configuration are loaded from environment variables.

## Setup

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd clone
   ```
2. Create a `.env` file based on the example below and fill in your email
   credentials.
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the script:
   ```sh
   python main.py
   ```

## Environment Variables

The script expects the following variables to be defined (example `.env.example`):

```
MY_EMAIL=your_email@example.com
MY_PASSWORD=your_email_password_or_app_token
SMTP_ADDRESS=smtp.yourprovider.com
```

Never commit real credentials; use `.gitignore` to exclude your `.env` file.

## Notes

- Make sure scraping Amazon complies with their terms of service.
- This is intended as a simple learning project; error handling and scheduler
  integration can be added for production use.