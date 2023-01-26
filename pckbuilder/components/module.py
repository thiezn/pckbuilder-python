from typing import Optional, List
from .variable import VariableComponent
from ..utils import Text


class ModuleComponent:
    """A python module is an object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing."""

    def __init__(
        self,
        name: str,
        description: str,
        imports: Optional[List[str]] = None,
        variables: Optional[List[VariableComponent]] = None,
        classes: Optional[List] = None,
        functions: Optional[List] = None,
        executable_body: Optional[str] = None,
    ):
        """Initialize our ModuleComponent instance.

        :param name: The name of the module
        :param description: The description of the module
        :param imports: The imports for this module
        :param variables: List of module scoped variables
        :param classes: List of class definitions in this module
        :param functions: List of function definitions in this module
        :param executable_body: Adds code that gets executed when running the module directly
        """
        self.name = name
        self.description = description
        self.imports = imports or set()
        self.variables = variables or set()
        self.classes = classes or set()
        self.functions = functions or set()
        self.executable_body = executable_body

    def __repr__(self) -> str:
        """Pretty representation of class instance."""
        return f"<TypeComponent '{self.name}'>"

    def text(self) -> str:
        """Convert our type to text."""
        text = Text()

        if self.executable_body:
            text.add_shebang()

        text.add_docstring(self.description, newlines=2)

        text.add(self.imports, newlines=2)

        for variable_item in self.variables:
            text.add(variable_item.text(show_value=True))
        text.add_newline()

        text.add(self.classes)
        text.add(self.functions)

        if self.executable_body:
            text.add('if __name__ == "__main__":')
            text.add(self.executable_body, indent=4)

        return text.string
