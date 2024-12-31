# app/services/email_service.py
import logging

logger = logging.getLogger(__name__)

def process_incoming_email(payload: dict):
    """
    Process the incoming email payload from Twilio SendGrid.
    """
    from_email = payload.get("from")
    subject = payload.get("subject")
    body = payload.get("text")  # Plain text body
    html_body = payload.get("html")  # HTML body (if available)

    logger.info(f"Received email from: {from_email}")
    logger.info(f"Subject: {subject}")
    logger.info(f"Body preview: {body[:50]}")  # Log the first 50 characters

    # Perform your desired processing (e.g., save to DB, forward, etc.)
    return {"status": "success", "message": "Email processed successfully"}

# Add this to email_service.py
def verify_signature(headers, payload, secret):
    """
    Verify the request signature to ensure authenticity.
    """
    import hmac
    import hashlib
    computed_signature = hmac.new(
        key=secret.encode(),
        msg=payload.encode(),
        digestmod=hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(headers.get("X-Twilio-Signature", ""), computed_signature)
