from .type import TypeComponent


class VariableComponent:
    """Holds a single value."""

    def __init__(
        self, name: str, description: str, variable_type: TypeComponent, value=None
    ):
        """Initialize our class."""
        self.name = name
        self.description = description
        self.type = variable_type
        self.value = value

    def __repr__(self) -> str:
        """Pretty representation of class instance."""
        return f"<VariableComponent '{self.text()}'>"

    def text(self, show_type_hint=True, show_value=False) -> str:
        """Convert our variable to text."""
        text = f"{self.name}"
        if self.type and show_type_hint:
            text += f": {self.type.text()}"

        if show_value:
            if isinstance(self.value, str):
                text += f' = "{self.value}"'
            else:
                text += f" = {self.value}"

        return text

    @property
    def docstring(self) -> str:
        """Generate the docstring of the VariableComponent."""
        docstring = f":param {self.name}: "
        if self.description:
            docstring += self.description

        return docstring
