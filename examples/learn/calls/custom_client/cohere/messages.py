from cohere import AsyncClient, Client
from mirascope.core import Messages, cohere


@cohere.call("command-r-plus", client=Client())
def recommend_book(genre: str) -> Messages.Type:
    return Messages.User(f"Recommend a {genre} book")


@cohere.call("command-r-plus", client=AsyncClient())
async def recommend_book_async(genre: str) -> Messages.Type:
    return Messages.User(f"Recommend a {genre} book")
