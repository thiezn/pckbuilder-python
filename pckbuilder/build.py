from pathlib import Path
from .components.package import PackageComponent
import shutil
from .utils import write_file


def build(
    package: PackageComponent,
    build_folder=Path("packagebuild/"),
    create_pyproject_file=True,
    create_setup_file=True,
):
    """Build given PackageComponent.

    :param package: The PackageComponent to build
    :param build_folder: The folder where the package will be written to. NOTE:
    any existing items in this folder will be removed before building
    """
    if build_folder.exists:
        print(f"Deleting existing folder '{build_folder}'")
        shutil.rmtree(build_folder, ignore_errors=True)

    print(f"Creating build folder '{build_folder}'")
    build_folder.mkdir()

    if create_pyproject_file:
        print("Writing pyproject.toml file")
        write_file(
            package.pyproject(),
            Path(build_folder, "pyproject.toml"),
            format_with_black=False,
        )

    if create_setup_file:
        print("Writing setup.cfg file")
        write_file(
            package.setup_text(),
            Path(build_folder, "setup.cfg"),
            format_with_black=False,
        )

    print("Creating package folder")
    package_folder = Path(build_folder, package.name)
    package_folder.mkdir()
    write_file(package.init_text(), Path(package_folder, "__init__.py"))

    for module in package.modules:
        print(f"Creating module {module.name}")
        write_file(module.text(), Path(package_folder, f"{module.name}.py"))
