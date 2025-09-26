#!/usr/bin/env python

import argparse
import csv
import json


def extract_arrays_from_json(file_path):
    """
    Reads a JSON file and extracts the 'lists' and 'cards' arrays.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        tuple: A tuple containing the lists and cards arrays,
               or (None, None) if an error occurs.
    """
    lists = []
    cards = []

    try:
        # Open the JSON file in read mode ('r')
        with open(file_path, 'r') as file:
            # Use json.load() to parse the file into a Python dictionary
            data = json.load(file)

            # Access the arrays by their key names using .get() for safety
            lists = data.get('lists', [])
            cards = data.get('cards', [])

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file '{file_path}'.")

    return lists, cards


def extract_data(lists_data, cards_data):
    """
    Iterates through the lists and cards data and prints specific fields.

    Args:
        lists_data (list): The array of list objects.
        cards_data (list): The array of card objects.
    """
    status_lookup = {item.get('id'): item.get('name') for item in lists_data}
    filtered_cards = [c for c in cards_data if c['closed'] == False]
    rows = []

    for item in filtered_cards:
        parts = item['name'].split('*')
        id = parts[1] if len(parts) > 1 else ""
        rows.append({
            'Title': parts[0],
            'ID': id, 
            'Card URL': item.get('url'),
            'Status': status_lookup[item.get('idList')],
            'Labels': ",".join(set([i['name'] for i in item.get('labels')]))
            })

    return rows


def write_to_csv(rows, filename):
    """
    Writes an array of Trello Card data to a CSV file.
    
    Args:
        rows (list): The array of card data.
        filename (string): The location to write the the output CSV.
    """
    with open(filename, 'w+') as handle:
        fieldnames = ['Title', 'ID', 'Card URL', 'Status', 'Labels']
        writer = csv.DictWriter(handle,
                                fieldnames=fieldnames,
                                extrasaction='ignore')
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main():

    parser = argparse.ArgumentParser(
        description="A Trello JSON to CSV converter"
        )
    parser.add_argument(
        "json_file", type=str, help="The JSON file to convert"
        )
    parser.add_argument(
        "csv_file", type=str, help="The file for CSV output"
        )
    args = parser.parse_args()

    lists_data, cards_data = extract_arrays_from_json(args.json_file)

    if lists_data is not None and cards_data is not None:
        rows = extract_data(lists_data, cards_data)
        write_to_csv(rows, args.csv_file)


# --- Example usage ---
if __name__ == "__main__":
    main()
