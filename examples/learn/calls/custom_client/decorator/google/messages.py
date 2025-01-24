from google.genai import Client
from mirascope.core import Messages, google


@google.call("gemini-1.5-flash", client=Client())
def recommend_book(genre: str) -> Messages.Type:
    return Messages.User(f"Recommend a {genre} book")
