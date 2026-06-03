from twilio.rest import Client
import os

def get_client():
    return Client(
        os.getenv("TWILIO_ACCOUNT_SID"),
        os.getenv("TWILIO_AUTH_TOKEN")
    )

def send_sms(to_number: str, message: str) -> dict:
    """Send an SMS via Twilio. Returns status dict."""
    try:
        client = get_client()
        msg = client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=to_number
        )
        return {"status": "sent", "sid": msg.sid}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
