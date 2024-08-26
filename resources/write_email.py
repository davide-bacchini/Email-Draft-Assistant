import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

emails=""
context = f"""

I am providing you some examples of answers to help you write new emails: {emails}

Analyze the incoming email carefully to determine if a response is necessary. Consider the following criteria for not responding:

1. The email is clearly spam, automated marketing or an update from a work platform such as Notion, Asana or Google Calendar.
2. It's a mass email where you're not the primary recipient (e.g., CC'd or BCC'd).
3. The message doesn't contain a question or request requiring your input.
4. It's an FYI or update email not necessitating acknowledgment.
5. The sender explicitly states no response is needed.

If any of these criteria are met, return just "". Don't write text, but just "". 

If a response is needed, evaluate the sender's relationship to you (e.g., colleague, superior, client, stranger) and the email's context. Based on this analysis, determine the appropriate tone for your reply.
Match the formality level of the original email. If the sender uses phrases like "Dear" or "Good morning," maintain a similar level of formality. Avoid casual greetings like "Hi" or "Hello" unless the original email uses them.
Craft your response to directly address the main points or questions raised in the email. Be concise yet thorough, and maintain a professional demeanor throughout.
Ensure your reply includes:

1. An appropriate salutation matching the original email's tone
2. Clear and relevant answers to any questions posed
3. Any necessary action items or next steps
4. A polite closing that fits the overall tone of the conversation

Before finalizing, review your draft to ensure it accurately reflects the intended tone and addresses all relevant points from the original email.


Don't provide any answer with angle brackets. 

I am providing you the email, encapsulated by angle brackets 
"""


def gpt(email):
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        temperature=1,
        messages=[
            {
                "role": "user",
                "content": f"{context}: <{email}>.",
            }
        ],
    )
    return response.choices[0].message.content
