from typing import Optional, List
from .module import ModuleComponent
from ..utils import Text


class PackageComponent:
    """A package is a Python module which can contain submodules or recursively, subpackages.

    Technically, a package is a Python module with a __path__ attribute.
    """

    def __init__(
        self,
        name: str,
        description: str,
        version: str,
        modules: Optional[List[ModuleComponent]] = None,
        package_license: str = "MIT",
        classifiers: Optional[List[str]] = None,
        install_requirements: Optional[List[str]] = None,
        keywords: Optional[List[str]] = None,
        imports: Optional[List[str]] = None,
    ):
        """Initialize our PackageComponent.

        :param name: The name of the module
        :param description: The description of the module
        :param version: The version of the python package
        :param modules: The list of modules part of this package
        :param imports: The list of imports to add to the package __init__.py file
        """
        self.name = name
        self.description = description

        if version.count(".") != 2:
            raise ValueError("Python packages should use symantic versioning (0.1.0)")

        self.version = version
        self.modules = modules or []
        self.license = package_license
        self.classifiers = classifiers or ["Programming Language :: Python :: 3"]
        self.install_requirements = install_requirements
        self.keywords = keywords
        self.imports = imports or []

    def pyproject(self, include_pytest=True, custom_data: Optional[str] = None) -> str:
        """Generate pyproject.toml contents."""
        text = Text()

        text.add(
            """\
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
            """,
        )

        if include_pytest:
            text.add(
                """
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = [
    "tests",
    "integration",
]
                """,
            )

        if custom_data:
            text.add(custom_data)

        return text.string

    def setup_text(
        self,
        metadata_items: Optional[List[str]] = None,
        option_items: Optional[List[str]] = None,
    ) -> str:
        """Generate setup.cfg contents."""
        text = Text()

        # metadata
        text.add("[metadata]")
        text.add(f"name = {self.name}")
        text.add(f"version = {self.version}")
        text.add(f"description = {self.description}")
        text.add("long_description = file: README.md")
        text.add(f"license = {self.license}")

        if self.keywords:
            text.add(f"keywords = {', '.join(self.keywords)}")

        if metadata_items:
            for item in metadata_items:
                text.add(item)

        # Options
        text.add_newline()
        text.add("[options]\npackages = find:")
        if self.classifiers:
            text.add(f"classifiers = ")
            for classifier in self.classifiers:
                text.add(classifier, indent=4)

        if self.install_requirements:
            text.add(f"install_requires = ")
            for requirement in self.install_requirements:
                text.add(requirement, indent=4)

        if option_items:
            for item in option_items:
                text.add(item)

        return text.string

    def init_text(self) -> str:
        """Generate __init__.py contents."""
        text = Text()
        text.add_docstring(f"{self.name} package.\n{self.description}")
        text.add(self.imports)

        return text.string
