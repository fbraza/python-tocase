[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/tocase
[pypi-url]: https://pypi.org/project/tocase/
[build-image]: https://github.com/fbraza/tocase/actions/workflows/ci.yml/badge.svg
[build-url]: https://github.com/fbraza/tocase/blob/master/.github/workflows/ci.yml

![](assets/banner_ToCase.png)

## Functionality

`tocase` leverages the `regex` library to convert your strings into any case.

## Setup

To install the package run the following command:

```bash
pip install tocase
```

Once installed, import the `for_strings` if you want to use the basic API to recase strings. Import the `for_pandas` modules to use the pandas API to recase column names and column values.

```python
import tocase.tocase.for_strings.ToCase as ToCase
import tocase.tocase.for_pandas
```

## Usage

### Camel

It is a naming convention where the first letter in compound words is capitalized, except for the first one.

```python
# Example with simple string
Tocase("camel-case").camel() # ==> camelCase
Tocase("camel case").camel() # ==> camelCase
```

### Constant

It is a naming convention where all letters in compound words are capitalized. Words are joined with an underscore.

```python
# Example with simple string
Tocase("Constant-case").constant() # ==> CONSTANT_CASE
Tocase("constant Case").constant() # ==> CONSTANT_CASE
```

### Dot

It is a naming convention where all letters in compound words are lowercased. Words are joined with a dot.

```python
# Example with simple string
Tocase("Dot-case").dot() # ==> dot.case
Tocase("dot Case").dot() # ==> dot.case
```

### Header

It is a naming convention where the first letter in compound words is capitalized. Words are joined by a dash.

```python
# Example with simple string
Tocase("Header-case").header() # ==> Header-Case
Tocase("header Case").header() # ==> Header-Case
```

### Kebab

It is a naming convention where all letters in compound words are lowercased. Words are joined by a dash.

```python
# Example with simple string
Tocase("Kebab-case").kebab() # ==> kebab-case
Tocase("kebab Case").kebab() # ==> kebab-case
```

### Pascal

It is a naming convention where the first letter in compound words is capitalized.

```python
# Example with simple string
Tocase("Pascal-case").pascal() # ==> PascalCase
Tocase("pascal Case").pascal() # ==> PascalCase
```

### Snake

It is a naming convention where all letters in compound words are lowercased. Words are joined by an underscore.

```python
# Example with simple string
Tocase("Snake-case").snake() # ==> snake_case
Tocase("snake Case").snake() # ==> snake_case
```

### Title

It is a naming convention where the first letter in compound words is capitalized. Words are separated by a space.

```python
# Example with simple string
Tocase("Title-case").title() # ==> "Title Case"
Tocase("title Case").title() # ==> "Title Case"
```

### With pandas DataFrames

You can work with pandas DataFrame to recase columns names or column values. See the following examples with fake data.

```python
columns = ["first name", "last name", "age", "family doctor"]
values = [
        ["Jules", "Otti", 35, "Dr James Porter"],
        ["Marie", "Curie", 22, "Dr Vicky Laporte"],
        ["Marc", "El Bichon", 35, "Dr Hyde Frank"]
        ]
data =  pd.DataFrame(data=values, columns=columns)
```

To recase columns names, use the `col` DataFrame accessor and the appropriate recasing function described above.

```python
print(data)

"""
  first name last name  age   family doctor
0      Jules      Otti   35   DrJamesPorter
1      Marie     Curie   22  DrVickyLaporte
2       Marc  ElBichon   35     DrHydeFrank

"""

print(data.col.constant())

"""
  FIRST_NAME LAST_NAME  AGE   FAMILY_DOCTOR
0      Jules      Otti   35   DrJamesPorter
1      Marie     Curie   22  DrVickyLaporte
2       Marc  ElBichon   35     DrHydeFrank
"""
```

To recase columns values, use the `val` DataFrame accessor, the appropriate recasing function described above with a list of the columns to be processed.

```python
columns_to_process = ["first name", "last name", "family doctor"]
print(data.val.constant(columns_to_process))

"""
  first name  last name  age     family doctor
0      JULES       OTTI   35   DR_JAMES_PORTER
1      MARIE      CURIE   22  DR_VICKY_LAPORTE
2       MARC  EL_BICHON   35     DR_HYDE_FRANK

"""
```

## For developers

Clone or download the repository on your machine. If you have `poetry` installed just run the following command to restore the working environment:

```bash
poetry install
```

If you don't have `poetry` you can use `pip` and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

To run tests, stay at the root of the directory and run:

```bash
pytest -v
```

All contributions are more than welcome. So feel free to to make a PR.

## Author

Faouzi Braza
