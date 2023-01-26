# Python Package Builder

***IMPORTANT*** This repository is very much a work in progress, use at your own risk.

This provides abstractions to generate a Python package from code. The purpose is to decouple the generation of
directories and files from the schema/source to convert. 

For example with GraphQL API's you will want to parse the schema and convert them into the
relevant components from this Package Builder. A different use case could be to parse the AWS botocore
json files and generate classes for all the AWS models.

# Usage

Clone the repository locally and install it with pip. The example.py builds a sample
package in the default packagebuild folder.

```sh
git clone https://github.com/thiezn/pckbuilder-python.git
python3 -m pip install .
chmod +x example.py
./example.py
```

# Components

These are the basic building blocks used to build up a Python package. To start the build you import the build command and feed it a PackageComponent.

```python
from pckbuilder import PackageComponent, build
package = PackageComponent(...)
build(package)
```

## PackageComponent

A package is a Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with a __path__ attribute.

https://docs.python.org/3/glossary.html#term-package

## ModuleComponent

A Python module is an object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

https://docs.python.org/3/glossary.html#term-module


## VariableComponent

Holds a single value

## TypeComponent

A Python type. This can be a builtin Python type like str or int, or it could be a custom class defined in the package

## FunctionComponent

A function is a series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body.

https://docs.python.org/3/glossary.html#term-function


## MethodComponent

A method is a function that is part of a class. The key differentiator is that its first argument is (usually) self. In the case of a classmethod it can also be cls, or with staticmethod doesn't have a first method

Inherits from FunctionComponent

https://docs.python.org/3/glossary.html#term-method


## ClassComponent

A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.

https://docs.python.org/3/glossary.html#term-class


# Text helper

Composing large text within Python can get messy. The pckbuilder project exposes a helper class called Text thats heavily being used by the
package itself to generate the files.

You can use this class yourself to, for instance, compose a function body. It can help with indentation, docstrings and
adding newlines.

```python
>>> text = Text()

>>> text.add("just a string")
>>> text.add(["multiple", "lines"])
>>> text.add("indented", indent=4)
>>> text.add("space is the place", newlines=3)
>>> text.add("Thanks for watching", indent=2, newlines=0)

>>> print(text.string)
just a string
multiple
lines

    indented
space is the place


  Thanks for watching
>>>
```
