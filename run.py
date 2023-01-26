#!/usr/bin/env python3

from pckbuilder import (
    TypeComponent,
    PackageComponent,
    ModuleComponent,
    MethodComponent,
    FunctionComponent,
    VariableComponent,
    TypeComponent,
    ClassComponent,
    build,
)


def main():
    """Script entrypoint for testing the modulebuilder package."""
    str_type = TypeComponent("str")
    int_type = TypeComponent("int")
    optional_list = TypeComponent("List", is_optional=True)
    str_list = TypeComponent("List")
    variables = [
        VariableComponent("mystr", "test variable", str_type, value="hello world"),
        VariableComponent("myint", "an integer variable", int_type, value=1),
        VariableComponent("mylist", "A list", str_list, value=["hello", "world"]),
        VariableComponent("myoptionallist", "A list", optional_list),
    ]
    # classes = [ClassComponent("MyClass", "A test class component.")]
    functions = [
        FunctionComponent(
            "my_function", "A test function component.", "print('hello world')"
        ),
        FunctionComponent(
            "my_second_function",
            "A second test function component.",
            "print('hello world')",
            [VariableComponent("test", "a test function argument", str_type)],
            [
                VariableComponent(
                    "test_kw",
                    "a test function keyword argument",
                    str_type,
                    value="default value",
                )
            ],
        ),
    ]
    methods = [
        MethodComponent(
            "__init__",
            "Initialize class instance.",
            "self.mystr = mystr",
            [
                VariableComponent(
                    "mystr", "test variable", str_type, value="hello world"
                )
            ],
        )
    ]
    classes = [
        ClassComponent(
            "MyClass",
            "A test class",
            [
                VariableComponent(
                    "myclassvar", "test class variable", str_type, value="hello world"
                )
            ],
            methods,
        )
    ]
    module = ModuleComponent(
        "test",
        "My test module.",
        ["from typing import List, Optional"],
        variables,
        classes,
        functions,
    )

    package = PackageComponent(
        "mypackage",
        "a test package",
        "0.1.0",
        modules=[module],
        install_requirements=["httpx"],
        keywords=["test", "mathijs"],
    )
    build(package)


if __name__ == "__main__":
    main()
