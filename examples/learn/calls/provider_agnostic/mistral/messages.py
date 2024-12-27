from mirascope.core import Messages
from mirascope.llm import call


@call(provider="mistral", model="mistral-large-latest")
def recommend_book(genre: str) -> Messages.Type:
    return Messages.User(f"Recommend a {genre} book")


response = recommend_book("fantasy")
print(response.content)
