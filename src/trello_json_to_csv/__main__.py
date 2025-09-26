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
    status_lookup = {}
    if lists_data:
        print("Lists (id and name):")
        for item in lists_data:
            list_id = item.get('id')
            list_name = item.get('name')
            status_lookup[list_id] = list_name
            print(f"  - ID: {list_id}, Name: {list_name}")
    else:
        print("No 'lists' data found.")

    rows = []
    if cards_data:
        print("\nCards (name and shortUrl):")
        for item in [c for c in cards_data if c['closed'] == False]:
            card_name = item.get('name') # 'name' from the previous step is now 'title'
            card_url = item.get('url')
            card_status = status_lookup[item.get('idList')]
            labels = [i['name'] for i in item.get('labels')]
            print(f"  - Name: {card_name}, URL: {card_url}, Status: {card_status}")
            rows.append({'Title': card_name, 'Card URL': card_url, 'Status': card_status,
                         'Labels': ",".join(labels)})
    else:
        print("No 'cards' data found.")
    return rows

def write_to_csv(rows, filename):
    with open(filename, 'w+') as handle:
        fieldnames = ['Title', 'Card URL', 'Status', 'Labels']
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
    args = parser.parse_args()

    json_file_path = args.json_file

    lists_data, cards_data = extract_arrays_from_json(json_file_path)

    if lists_data is not None and cards_data is not None:
        rows = extract_data(lists_data, cards_data)
        write_to_csv(rows, "output.csv")

# --- Example usage ---
if __name__ == "__main__":
    main()
