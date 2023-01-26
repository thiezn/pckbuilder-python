# Python Package Builder

This provides abstractions to generate a python package from code. The purpose is to decouple the generation of
directories and files from the schema/source to convert. 

For example with GraphQL API's you will want to parse the schema and convert them into the
relevant components from this Package Builder. A different use case could be to parse the AWS botocore
json files and generate classes for all the AWS models.

# Components

These are the basic building blocks used to build up a python package. To start the build you import the build command and feed it a PackageComponent.

```python
from pckbuilder import PackageComponent, build
package = PackageComponent(...)
build(package)
```

## Package

A package is a Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with a __path__ attribute.

TODO: How can I be flexible in where to generate the __init__.py files. sometimes you want sub folders but imports happening in top
level folder.

Arguments:
    name: str
    description: str
    modules: List[Module]
    subpackages: List[Package]  # Lets leave out support initially for this, or perhaps 
                                # create a separate SubPackage class. We only want to generate 
                                # a single pyproject.toml file for instance.

## Module

A python module is an object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

https://docs.python.org/3/glossary.html#term-module

Arguments:
 name: str
 description: str
 imports: List[str]
 variables: List[Variable]
 classes: List[Class]
 functions: List[Function]


## Variable

Holds a single value

Arguments:
    name: str
    description: str
    type: Type

## Type

A Python type. This can be a builtin python type like str or int, or it could be a custom class defined in the package

Arguments:
    name: str
    is_optional: bool
    is_built_in: bool
    # TODO: how to represent Unions?
    # TODO: how to switch between old style type hints and > 3.9/.10 type hints? maybe something like:
    # python_version: str  # This determines how to represent some of the built_in types, eg. List vs list

## Function

A function is a series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body.

https://docs.python.org/3/glossary.html#term-function

Arguments:
    name: str
    description: str
    arguments: List[Variables]
    keyword_arguments: List[Variables]
    return_type: Type
    body: str

## Method

A method is a function that is part of a class. The key differentiator is that its first argument is (usually) self. In the case of a classmethod it can also be cls, or with staticmethod doesn't have a first method

Inherits from Function

Arguments:
    is_classmethod: bool
    is_staticmethod: bool

## Class

A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.

https://docs.python.org/3/glossary.html#term-class

Arguments:
    name: str
    description: str
    base_class_name: Optional[str]  # Or do we need the whole class? This determines inheritance
    decorator: str # name of a decorator like dataclass? Or perhaps something like is_dataclass instead?
    class_arguments: [Variable]  # These are 'global' class variables, NOT the ones from __init__
    methods: [Method]  # Do i need a special __init__ method representation and perhaps some others?

