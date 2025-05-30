import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))  # fallback to 587
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# def send_email_notification(to_email: str, subject: str, body: str):
#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = EMAIL_USERNAME
#     msg["To"] = to_email

#     try:
#         with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
#             server.ehlo()
#             server.starttls()
#             server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
#             server.send_message(msg)
#         print(f"✅ Email sent to {to_email}")
#     except Exception as e:
#         print(f"❌ Failed to send email: {e}")
#         raise

def send_email_notification(to_email: str, subject: str, body: str):
    print("📤 Attempting to send email...")
    print(f"➡️ Sending to: {to_email}")
    print(f"📧 SMTP Host: {EMAIL_HOST}, Port: {EMAIL_PORT}")
    print(f"👤 Username: {EMAIL_USERNAME}")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USERNAME
    msg["To"] = to_email

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.ehlo()
            server.starttls()
            print("🔐 Starting TLS...")
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            print("✅ Logged in successfully")
            server.send_message(msg)
        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        raise
