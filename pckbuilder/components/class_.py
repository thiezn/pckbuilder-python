from .method import MethodComponent
from typing import List, Optional
from .variable import VariableComponent
from ..utils import Text


class ClassComponent:
    """A template for creating user-defined objects.

    Class definitions normally contain method definitions which operate on instances of the class.
    """

    def __init__(
        self,
        name: str,
        description: str,
        class_arguments: Optional[List[VariableComponent]] = None,
        methods: Optional[List[MethodComponent]] = None,
        base_class_name: Optional[str] = None,
    ):
        """Initialize ClassComponent instance."""
        self.name = name
        self.description = description
        self.class_arguments = class_arguments or []
        self.methods = methods or []

        self.base_class_name = base_class_name

    def text(self) -> str:
        """Convert our class component to text."""
        text = Text()

        if self.base_class_name:
            text.add(f"class {self.name}({self.base_class_name}):")
        else:
            text.add(f"class {self.name}:")

        text.add_docstring(self.description, indent=4, newlines=2)

        for argument in self.class_arguments:
            if argument.value:
                show_value = True
            else:
                show_value = False

            text.add(f"{argument.text(show_value=show_value)}", indent=4)

        text.add_newline()

        text.add(self.methods, indent=4)

        return text.string
