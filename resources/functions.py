import sys
import base64

from simplegmail import Gmail
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

from resources.write_email import gpt


sys.stdout.reconfigure(encoding="utf-8")


def gmail_create_draft(email):
    """Create and insert a draft email in response to a received email."""

    creds = Credentials.from_authorized_user_file(
        "gmail_token.json", ["https://www.googleapis.com/auth/gmail.modify"]
    )

    try:
        service = build("gmail", "v1", credentials=creds)
        original_message = (
            service.users().messages().get(userId="me", id=email.id).execute()
        )

        message = EmailMessage()

        message.set_content(gpt(email.plain))
        message["To"] = email.sender
        message["From"] = email.recipient
        message["Subject"] = f"Re: {email.subject}"

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {
            "message": {
                "raw": encoded_message,
                "threadId": original_message["threadId"],
            }
        }

        draft = (
            service.users().drafts().create(userId="me", body=create_message).execute()
        )

    except HttpError as error:
        print(f"An error occurred: {error}")
        draft = None

    return draft


def draft_unread_messages():
    """Create a draft for all the unread messages from Gmail and mark them as read."""

    gmail = Gmail()
    messages = gmail.get_unread_messages()
    for message in messages:
        gmail_create_draft(message)
        message.mark_as_read()

