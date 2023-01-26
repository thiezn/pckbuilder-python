BUILTIN_TYPES = {
    "str",
    "int",
    "float",
    "bool",
    "dict",
    "list",
    "tuple",
    "range",
}

BUILTIN_GENERIC_TYPES = {
    "List",
    "Tuple",
    "Iterable",
    "Dict",
    "Union",
    "Callable",
}


class TypeComponent:
    """A Python type.

    This can be a builtin python type like str or int, or it could be a custom class defined
    in the package.
    """

    def __init__(self, name: str, is_optional: bool = False):
        """Initialize our class.

        :param name: The name of the type
        :param is_optional: Determines if the type is optional
        :param is_generic:
        """
        self.name = name
        self.is_optional = is_optional

    def __repr__(self) -> str:
        """Pretty representation of class instance."""
        return f"<TypeComponent '{self.text()}'>"

    @property
    def is_builtin(self) -> bool:
        """Returns if this type definition is builtin to the python language."""
        return self.name in BUILTIN_GENERIC_TYPES or self.name in BUILTIN_TYPES

    @property
    def is_generic(self) -> bool:
        """Returns if its one of the generic types from the typing module like List and Dict.

        NOTE: we are not yet able to specify the sub types of generics.
        """
        return self.name in BUILTIN_GENERIC_TYPES

    def text(self) -> str:
        """Convert our type to text."""
        text = f"{self.name}"
        if self.is_optional:
            text = f"Optional[{self.name}]"
        else:
            text = self.name

        return text
