import json
import pandas as pd

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

# Function to convert JSON string to CSV
def json_to_csv(json_string, output_csv):
    # Load the JSON data from the string
    data = json.loads(json_string)

    # Flatten each JSON object
    flattened_data = [flatten_json(item) for item in data]

    # Convert JSON to DataFrame
    df = pd.DataFrame(flattened_data)

    # Save DataFrame to CSV
    df.to_csv(output_csv, index=False)

    print(f"Conversion completed. The CSV file has been saved as '{output_csv}'.")

# Example usage
if __name__ == "__main__":
    # Sample complex JSON string
    json_string = '''
    [
        {
            "name": "Alice",
            "age": 30,
            "address": {
                "city": "New York",
                "state": "NY"
            },
            "phones": ["123-456-7890", "987-654-3210"]
        },
        {
            "name": "Bob",
            "age": 25,
            "address": {
                "city": "San Francisco",
                "state": "CA"
            },
            "phones": ["555-555-5555"]
        }
    ]
    '''

    # Output CSV file name
    output_csv = "data.csv"

    # Convert JSON to CSV
    json_to_csv(json_string, output_csv)
