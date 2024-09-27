from mirascope.core import gemini
from pydantic import BaseModel


class Book(BaseModel):
    """An extracted book."""

    title: str
    author: str


@gemini.call("gemini-1.5-flash", response_model=Book)
def extract_book(text: str) -> str:
    return f"Extract {text}"


book = extract_book("The Name of the Wind by Patrick Rothfuss")
print(book)
# Output: title='The Name of the Wind' author='Patrick Rothfuss'
