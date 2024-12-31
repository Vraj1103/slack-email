# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
# from app.config import SLACK_BOT_TOKEN, SLACK_CHANNEL_ID

# slack_client = WebClient(token=SLACK_BOT_TOKEN)

# async def send_to_slack_thread(email_from: str, message: str):
#     """
#     Sends a message to a Slack thread for the specific email sender.
#     """
#     try:
#         # Post the message to Slack
#         response = slack_client.chat_postMessage(
#             channel=SLACK_CHANNEL_ID,
#             text=message,
#             thread_ts=email_from  # Using email address as a unique identifier
#         )
#         return response
#     except SlackApiError as e:
#         print(f"Error sending to Slack: {e.response['error']}")
