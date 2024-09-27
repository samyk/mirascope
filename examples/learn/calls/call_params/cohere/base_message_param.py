from mirascope.core import BaseMessageParam, cohere


@cohere.call("command-r-plus", call_params={"max_tokens": 512})
def recommend_book(genre: str) -> list[BaseMessageParam]:
    return [BaseMessageParam(role="user", content=f"Recommend a {genre} book")]


print(recommend_book("fantasy"))
