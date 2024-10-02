from mirascope.core import BaseMessageParam, BaseTool, azure
from pydantic import Field


class GetBookAuthor(BaseTool):
    """Returns the author of the book with the given title."""

    title: str = Field(..., description="The title of the book.")

    def call(self) -> str:
        if self.title == "The Name of the Wind":
            return "Patrick Rothfuss"
        elif self.title == "Mistborn: The Final Empire":
            return "Brandon Sanderson"
        else:
            return "Unknown"


@azure.call("gpt-4o-mini", tools=[GetBookAuthor])
def identify_authors(books: list[str]) -> list[BaseMessageParam]:
    return [BaseMessageParam(role="user", content=f"Who wrote {books}?")]


response = identify_authors(["The Name of the Wind", "Mistborn: The Final Empire"])
if tools := response.tools:
    for tool in tools:
        print(tool.call())
else:
    print(response.content)
