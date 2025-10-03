# trello-json-to-csv

Convert Trello JSON export into a simple CSV file

## Develpment Quick Start

This application uses Python 3.12.

A VS Code Dev container configuration is provided for local development.


```bash
# The following two commands are not needed when running in a
# VS Code Dev container
$ python -m venv --prompt "trello-json-to-csv$(cat .python-version)" .venv
$ source .venv/bin/activate

# Install the dependencies
$ pip install -e .
```

Running the tests:

```bash
$ pytest
```

## Sample Usage

```
$ trello-json-to-csv <JSON_FILE> <CSV_OUTPUT_FILE>
```

where:

* \<JSON_FILE> is the Trello JSON file to convert.
* \<CSV_OUTPUT_FILE> is the file to output the CSV to.

## Trello "cards" array entries

Only keys of interest for this project are shown:

```json
"cards": [
    {
      "id": "<CARD_ID>",
      "desc": "<Concatenated string of multiple fields>",
      "idList": "<LIST_ID>",
      "labels": [
        {
          "id": "<LABEL_ID>",
          "name": "<LABEL_NAME>",
        },
      ],
      ...
    }
]
```

## Trello "lists" array entries

Only keys of interest for this project are shown:

```json
"lists": [
  {
    "id": "<LIST_ID>",
    "name": "<LIST_NAME>",
    ...
  },
  ...
]
```
