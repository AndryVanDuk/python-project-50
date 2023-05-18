# Difference calculator

### Hexlet tests and linter status:
[![Actions Status](https://github.com/AndryVanDuk/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/AndryVanDuk/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d88097284907373d4fdf/maintainability)](https://codeclimate.com/github/AndryVanDuk/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d88097284907373d4fdf/test_coverage)](https://codeclimate.com/github/AndryVanDuk/python-project-50/test_coverage)

### Built With

* Python
* Poetry
* PyYAML
* JSON
* Pytest
* flake8
* argparse
---
## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.8 or higher installed:

```bash
>> python --version
Python 3.8.0+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

### Package

To use the package, you need to clone the repository to your computer. This is done using the ```git clone``` command. Clone the project:

```bash
>> git clone https://github.com/venyxD/python-project-50.git
```

Then you have to build the package and install it:

```bash
>> cd python-project-50
```

```bash
>> poetry build
>> python3 -m pip install --user dist/*.whl
```

---

## Usage

Difference Generator can be used as CLI tool or as an external library.

### As external library

```python
from gendiff import generate_diff
diff = generate_diff(file_path1, file_path2, file_format)
```

### As CLI tool

The general usage is (both absolute and relative paths to files are supported):

```bash
>> gendiff [-f file_format] file_path1 file_path2
```

Difference Generator provides help command as well:

```bash
>> gendiff --help

usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output (default: 'stylish')
```
## Demo

### _Stylish format_

If no format option is provided, output will be provided in _stylish_ format.

The difference is based on how the files have changed relative to each other, the keys are rendered in alphabetical order.

The absence of a plus or minus indicates that the key is in both files, and its values coincide. In all other situations, the value of the key is either different, or the key is only in one file.

```bash
>> gendiff file_path1.json file_path2.json

{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

#### Compare two flat JSON and/or YAML files: _stylish_ format

[![asciicast](https://asciinema.org/a/585657.svg)](https://asciinema.org/a/585657)



This is the second training project of the ["Python Developer"](https://ru.hexlet.io/programs/python) course on [Hexlet.io](https://hexlet.io)

> GitHub [@AndryVanDuk](https://github.com/AndryVanDuk) &nbsp;&middot;&nbsp;
