from mirascope.core import BaseMessageParam
from mirascope.llm import call


@call(provider="mistral", model="mistral-large-latest")
def recommend_book(genre: str) -> list[BaseMessageParam]:
    return [BaseMessageParam(role="user", content=f"Recommend a {genre} book")]


response = recommend_book("fantasy")
print(response.content)
