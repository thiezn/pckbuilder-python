from .function import FunctionComponent
from typing import List, Optional
from .variable import VariableComponent
from .type import TypeComponent


class MethodComponent(FunctionComponent):
    """A method is a function that is part of a class.

    The key differentiator is that its first argument is (usually) self. In the case of a classmethod it can also be cls, or with staticmethod doesn't have a first method
    """

    def __init__(
        self,
        name: str,
        description: str,
        body: str,
        arguments: Optional[List[VariableComponent]] = None,
        keyword_arguments: Optional[List[VariableComponent]] = None,
        return_type: Optional[TypeComponent] = None,
        is_class_method: bool = False,
        is_static_method: bool = False,
    ):
        """Initialise our FunctionComponent instance."""
        self.name = name
        self.description = description

        self.arguments = arguments or []
        self.keyword_arguments = keyword_arguments or []
        self.body = body
        self.return_type = return_type

        if is_class_method and is_static_method:
            raise ValueError("A method can't be both a class- and staticmethod")

        self.is_class_method = is_class_method
        self.is_static_method = is_static_method

    @property
    def function_definition(self) -> str:
        """Returns the function definition string.

        This manipulates the FunctionComponent superclass to add
        class- or staticmethod definition.
        """
        text = super().function_definition

        if self.is_class_method:
            text = text.replace(f"def {self.name}(", f"def {self.name}(cls, ")
            text = f"@classmethod\n{text}"
        elif not self.is_static_method:
            text = text.replace(f"def {self.name}(", f"def {self.name}(self, ")

        return text
