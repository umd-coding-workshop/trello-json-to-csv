# trello-json-to-csv
Convert Trello JSON export into a simple CSV file


## Quick Start

A VS Code Dev container configuration is provided for local development.


```bash
# The following two commands are not needed when running in a
# VS Code Dev container
$ python -m venv --prompt "trello-json-to-csv$(cat .python-version)" .venv
$ source .venv/bin/activate

# Install the dependencies
$ pip install -e .
```

## Sample Usage

```
$ trello-json-to-csv <JSON_FILE>
```

where \<JSON_FILE> is the Trello JSON file to convert.

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
