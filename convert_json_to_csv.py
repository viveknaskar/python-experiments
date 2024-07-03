import json
import pandas as pd

def flatten_json(y, parent_key='', sep='_'):
    """Recursive function to flatten a JSON object."""
    items = []
    if isinstance(y, dict):
        for k, v in y.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.extend(flatten_json(v, new_key, sep=sep).items())
    elif isinstance(y, list):
        for i, v in enumerate(y):
            new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
            items.extend(flatten_json(v, new_key, sep=sep).items())
    else:
        items.append((parent_key, y))
    return dict(items)

def json_to_csv(json_string, output_csv):
    """Converts a JSON string to a CSV file."""
    try:
        # Load the JSON data from the string
        data = json.loads(json_string)

        # Check if the JSON data is a list, if not, make it a list
        if not isinstance(data, list):
            data = [data]

        # Flatten each JSON object
        flattened_data = [flatten_json(item) for item in data]

        # Convert JSON to DataFrame
        df = pd.DataFrame(flattened_data)

        # Save DataFrame to CSV
        df.to_csv(output_csv, index=False)

        print(f"Conversion completed. The CSV file has been saved as '{output_csv}'.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Example of reading a JSON string from standard input
    json_string = '''
    {
"problems": [{
    "Diabetes":[{
        "medications":[{
            "medicationsClasses":[{
                "className":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }],
                "className2":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }]
            }]
        }],
        "labs":[{
            "missing_field": "missing_value"
        }]
    }],
    "Asthma":[{}]
}]}
    '''


    # Output CSV file name
    output_csv = "data.csv"

    # Convert JSON to CSV
    json_to_csv(json_string, output_csv)
