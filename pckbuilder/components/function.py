from typing import List, Optional
from .variable import VariableComponent
from .type import TypeComponent
from ..utils import Text


class FunctionComponent:
    """A function is a series of statements which returns some value to a caller.

    It can also be passed zero or more arguments which may be used in the execution of the body.
    """

    def __init__(
        self,
        name: str,
        description: str,
        body: str,
        arguments: Optional[List[VariableComponent]] = None,
        keyword_arguments: Optional[List[VariableComponent]] = None,
        return_type: Optional[TypeComponent] = None,
    ):
        """Initialise our FunctionComponent instance."""
        self.name = name
        self.description = description

        self.arguments = arguments or []
        self.keyword_arguments = keyword_arguments or []
        self.body = body
        self.return_type = return_type

    def __repr__(self) -> str:
        """Pretty representation of class instance."""
        return f"<{self.__class__.__name__} '{self.name}'>"

    @property
    def all_arguments(self) -> List[VariableComponent]:
        """Returns all function arguments in a single list.

        Keyword arguments will be added to the end
        """
        return self.arguments + self.keyword_arguments

    @property
    def function_definition(self) -> str:
        """Returns the function definition string."""
        text = f"def {self.name}("

        for argument in self.all_arguments:
            if argument.value:
                show_value = True
            else:
                show_value = False

            text += f"{argument.text(show_value=show_value)}, "

        text = text.rstrip(", ")

        if self.return_type:
            text += f") -> {self.return_type.text}:"
        else:
            text += f"):"

        return text

    def text(self) -> str:
        """Convert our function component to text."""
        text = Text()

        text.add(self.function_definition)
        text.add_docstring(self.description, indent=4)
        text.add(self.body, indent=4)

        return text.string
