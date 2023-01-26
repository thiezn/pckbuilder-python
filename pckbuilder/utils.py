import black
from pathlib import Path
from typing import Iterable


def write_file(content: str, location: Path, overwrite=True, format_with_black=True):
    """Write content to file.

    :param location: The full path to the file to write
    :param overwrite: determines if we allow overwriting existing files
    :param format_with_black: format the text with black formatter
    """
    if overwrite is False and location.exists:
        raise IOError(f"Location {location} already exists")

    if format_with_black is True:
        content = black.format_str(
            content,
            mode=black.Mode(),  # type: ignore
        )

    with open(location, "w") as f:
        f.write(content)


class Text:
    """Class representing text.

    It offers helpers to easily compose a text with with proper indentation and layout.
    """

    def __init__(self):
        """Initialise TextFile with empty text."""
        self._text = ""

    def _indent(self, text: str, indent: int) -> str:
        """Indents the given text with spaces.

        :param text: the text to indent
        :param indent: the amount of spaces to indent the text with.
        """
        spaces = indent * " "
        text = "\n".join([f"{spaces}{line}" for line in text.splitlines()])
        return text

    def add(self, text: Iterable, indent: int = 0, newlines: int = 1):
        """Add a line to the text.

        :param text: Can be a string, Text instance or an iterable of these two
        :param indent: The amount of indentation to add to the given text
        :param newlines: The amount of newlines to add after the given text. It will first remove
        any newlines that might already be present from the given text
        """
        if isinstance(text, str):
            if indent:
                text = self._indent(text, indent)

            self._text += text
        else:
            for item in text:
                if isinstance(item, str):
                    self.add(item, indent, newlines=1)
                else:
                    self.add(item.text(), indent, newlines=1)  # type: ignore

        self._text = self._text.rstrip("\n")
        self._text += newlines * "\n"

    def add_shebang(self):
        """Adds a unix style shebang to the text."""
        self.add("#!/usr/bin/env python3", newlines=2)

    def add_docstring(self, text: str, indent: int = 0, newlines: int = 1):
        """Returns the piece of text in a properly formatted docstring.

        :param text: the text to put into a docstring
        :param indentation: the amount of spaces to indent the docstring with.
        """
        if "." not in text:
            docstring = f'"""{text}."""'
        else:
            first_line, remaining_lines = text.split(".", 1)
            first_line = f"{first_line.rstrip('.')}."

            if remaining_lines:
                docstring = f'"""{first_line}\n\n{remaining_lines.strip()}\n"""'
            else:
                docstring = f'"""{first_line}"""'

        self.add(docstring, indent, newlines)

    def add_newline(self, count=1):
        """Adds a newline to the text.

        :param count: The amount of newlines to add
        """
        self._text += count * "\n"

    @classmethod
    def from_string(cls, text: str):
        """Create class instance from text."""
        instance = cls()
        instance._text = text
        return instance

    @property
    def string(self) -> str:
        """String representation of Text."""
        return self._text
