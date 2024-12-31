# app/routes/email.py
from fastapi import APIRouter, Request, HTTPException, Header
from app.services.email_service import process_incoming_email, verify_signature

router = APIRouter()

@router.post("/")
async def receive_email(data: dict):
    # Placeholder for email processing logic
    return {"message": "Email received", "data": data}

# @router.post("/receive")
# async def receive_email(request: Request):
#     """
#     Endpoint to receive emails from SendGrid's Inbound Parse Webhook.
#     """
#     try:
#         # Parse the incoming request
#         form_data = await request.form()
#         email_data = {
#             "from": form_data.get("from"),
#             "to": form_data.get("to"),
#             "subject": form_data.get("subject"),
#             "text": form_data.get("text"),
#             "html": form_data.get("html"),
#             "attachments": form_data.get("attachment-info"),  # Attachments metadata
#         }
#         # Process the incoming email
#         await process_incoming_email(email_data)
#         return {"status": "success", "message": "Email received and processed"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error processing email: {str(e)}")

# app/routes/email.py
# from fastapi import APIRouter, Request, HTTPException

router = APIRouter()

@router.post("/webhook/inbound")
async def inbound_email(request: Request, x_twilio_signature: str = Header(None)):
    """
    Webhook to receive incoming emails from Twilio SendGrid.
    """
    try:
        # Parse form data from the request
        form_data = await request.form()
        payload = {key: value for key, value in form_data.items()}

        raw_body = await request.body()
        # if not verify_signature(
        #     headers={"X-Twilio-Signature": x_twilio_signature},
        #     payload=raw_body.decode("utf-8"),
        #     secret=SECRET,
        # ):
        #     raise HTTPException(status_code=401, detail="Invalid signature")

        # Process the email
        result = process_incoming_email(payload)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing email: {str(e)}")

