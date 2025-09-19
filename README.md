# trello-json-to-csv
Convert Trello JSON export into a simple CSV file

Current implementation assumes that the JSON file is named `data.json`.

```bash
$ python3 json_to_csv.py
```

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
