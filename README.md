# dotenvpy, a python-dotenv wrapper

![version 0.1.0](https://img.shields.io/badge/version-0.1.0-blue "version 0.1.0")

This module is a simple wrapper around the well-known [`python-dotenv`](https://pypi.org/project/python-dotenv/) module for Python. It provides attribute-like read access to environment variables.

## Table of contents

1. [Installation](#installation)
2. [Usage](#usage)
   1. [Typed environment variables](#typed-environment-variables)
3. [Features](#features)

## Installation

**_INSTALLATION THROUGH `pip` COMING SOON!_**

- `pip install dotenvpy`

`python-dotenv` already comes as a requirement for `dotenvpy`; no need to worry about that.

## Usage

Use it as you would use `python-dotenv`:

```python
import dotenvpy as env
env.load_dotenv()

print(env.HOME)
print(env.PATH)

# This is equivalent to:
# print(os.getenv("HOME"))
# print(os.getenv("PATH"))
```

### Typed environment variables

`dotenvpy` uses Python's `ast` module to evaluate each environment variable as a literal. This allows for automatic conversion to the right types at access time, reducing the number of explicit type conversions users have to make in order to operate with their variables.

Asume a `.env` file as follows:

```dotenv
NON_VAR=None
BOL_VAR=True
INT_VAR=4
FLT_VAR=5.18
CPX_VAR=(2+3j)
LST_VAR=[1,2]
TPL_VAR=("1",2)
DCT_VAR={"a":1,"b":2}
STR_VAR="Just a string"
```

The following code would be valid with `dotenvpy`:

```python
import dotenvpy as env
env.load_dotenv()


# Without dotenvpy, this code would be quite larger
#
# At least a whole section with explicit type conversions and variable
# assignations would have been necessary

if env.NON_VAR is None and env.BOL_VAR:
    a = 9 % env.INT_VAR
    b = pow(env.FLT_VAR, 2)

if env.CPX_VAR.real + 1 == env.CPX_VAR.imag:
    print(env.LST_VAR[1])
    print(env.TPL_VAR[0])

if env.DCT_VAR["a"] + 1 == env.DCT_VAR["b"]:
    print(env.STR_VAR)
```

Since `ast` is the module Python internally uses for its own interpretation, it has the same capabilities as the language literals themselves:

- `None`
- Booleans
- Numbers: integers, floating-point, complex
- Lists (of any nested literal types)
- Tuples (of any nested literal types)
- Dictionaries (of any nested literal types)
- Strings

## Features

- **All** the capabilities of `python-dotenv`.
- Attribute-like read access to environment variables.
- Automatic conversion of the environment variables to their most suitable type.
