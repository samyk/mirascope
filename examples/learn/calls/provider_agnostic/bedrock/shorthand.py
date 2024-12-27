from mirascope.llm import call


@call(provider="bedrock", model="anthropic.claude-3-haiku-20240307-v1:0")
def recommend_book(genre: str) -> str:
    return f"Recommend a {genre} book"


response = recommend_book("fantasy")
print(response.content)
