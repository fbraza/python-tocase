[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/summarize_dataframe
[pypi-url]: https://pypi.org/project/summarize-dataframe/
[build-image]: https://github.com/fbraza/summarize_dataframe/actions/workflows/ci.yml/badge.svg
[build-url]: https://github.com/fbraza/summarize_dataframe/blob/master/.github/workflows/ci.yml

![](assets/banner_ToCase.png)

## Functionality

`tocase` leverages the `regex` library to convert your strings into any case.

## Setup

To install the package run the following command:

```bash
pip install tocase
```

Once installed import the `ToCase` class.

## Usage

### Camel

It is a naming convention where the first letter in compound words is capitalized, except for the first one.

```python
# Example with simple string
Tocase("camel-case").camel() # ==> camelCase
Tocase("camel case").camel() # ==> camelCase

# Example with Pandas DataFrame and Iris DataFrame
list(df_with_original_column_names.columns) = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df_with_modified_column_names = df.rename(columns=lambda x: ToCase(x).camel()
list(df_with_modified_column_names.columns) = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'species']
```

### Constant

It is a naming convention where all letters in compound words are capitalized. Words are joined with an underscore.

```python
# Example with simple string
Tocase("Constant-case").constant() # ==> CONSTANT_CASE
Tocase("constant Case").constant() # ==> CONSTANT_CASE

# Example with Pandas DataFrame and Iris DataFrame
list(df_with_original_column_names.columns) = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df_with_modified_column_names = df.rename(columns=lambda x: ToCase(x).constant()
list(df_with_modified_column_names.columns) = ['SEPAL_LENGTH', 'SEPAL_WIDTH', 'PETAL_LENGTH', 'PETAL_WIDTH', 'SPECIES']
```

### Dot

It is a naming convention where all letters in compound words are lowercased. Words are joined with a dot.

```python
# Example with simple string
Tocase("Dot-case").dot() # ==> dot.case
Tocase("dot Case").dot() # ==> dot.case

# Example with Pandas DataFrame and Iris DataFrame
list(df_with_original_column_names.columns) = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df_with_modified_column_names = df.rename(columns=lambda x: ToCase(x).dot()
list(df_with_modified_column_names.columns) = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width', 'species']
```

### Header

It is a naming convention where the first letter in compound words is capitalized. Words are joined by a dash.

```python
# Example with simple string
Tocase("Header-case").header() # ==> Header-Case
Tocase("header Case").header() # ==> Header-Case

# Example with Pandas DataFrame and Iris DataFrame
list(df_with_original_column_names.columns) = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df_with_modified_column_names = df.rename(columns=lambda x: ToCase(x).header()
list(df_with_modified_column_names.columns) = ['Sepal-Length', 'Sepal-Width', 'Petal-Length', 'Petal-Width', 'Species']
```

### Kebab

It is a naming convention where all letters in compound words are lowercased. Words are joined by a dash.

```python
# Example with simple string
Tocase("Header-case").kebab() # ==> Header-Case
Tocase("header Case").kebab() # ==> Header-Case

# Example with Pandas DataFrame and Iris DataFrame
list(df_with_original_column_names.columns) = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df_with_modified_column_names = df.rename(columns=lambda x: ToCase(x).kebab()
list(df_with_modified_column_names.columns) = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
```

### Pascal

It is a naming convention where the first letter in compound words is capitalized.

```python
# Example with simple string
Tocase("Pascal-case").pascal() # ==> PascalCase
Tocase("pascal Case").pascal() # ==> PascalCase

# Example with Pandas DataFrame and Iris DataFrame
list(df_with_original_column_names.columns) = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df_with_modified_column_names = df.rename(columns=lambda x: ToCase(x).pascal()
list(df_with_modified_column_names.columns) = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
```

### 'Sepal-Length', 'Sepal-Width', 'Petal-Length', 'Petal-Width', 'Species'Snake

It is a naming convention where all letters in compound words are lowercased. Words are joined by an underscore.

```python
# Example with simple string
Tocase("Pascal-case").snake() # ==> PascalCase
Tocase("pascal Case").snake() # ==> PascalCase

# Example with Pandas DataFrame and Iris DataFrame
list(df_with_original_column_names.columns) = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df_with_modified_column_names = df.rename(columns=lambda x: ToCase(x).snake()
list(df_with_modified_column_names.columns) = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
```

### Title

It is a naming convention where the first letter in compound words is capitalized. Words are separated by a space.

```python
# Example with simple string
Tocase("Pascal-case").snake() # ==> PascalCase
Tocase("pascal Case").snake() # ==> PascalCase

# Example with Pandas DataFrame and Iris DataFrame
list(df_with_original_column_names.columns) = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df_with_modified_column_names = df.rename(columns=lambda x: ToCase(x).snake()
list(df_with_modified_column_names.columns) = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']
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

To run test, stay at the root of the directory and run:

```bash
pytest -v
```

All contributions are more than welcome. So feel free to to make a PR.

## Author

Faouzi Braza
