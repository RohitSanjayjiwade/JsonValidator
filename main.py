# main.py

from json_validator.json_validator import JsonValidator

def main():
    json_data = {
        "id": 1,
        "name": "John",
        "home_phone": "123-456-7890",
        "day": "SU"
    }

    schema = {
        "required": ["id", "name"],
        "at_least_one_of": ["home_phone", "cell_phone", "work_phone"],
        "either_one_of": [("birth_date", "govt_id_number")],
        "mutually_exclusive": [("home_phone", "work_phone")],
        "field_values": {"day": ["SU", "MO", "TU", "WE", "TH", "FR", "SA"]}
    }

   
    json_validator = JsonValidator()

    # Validate the JSON data against the schema
    result = json_validator.validate(json_data, schema)

    # Print the validation result
    if result:
        print("JSON data is valid against the schema.")
    else:
        print("Validation failed. Please check the error messages.")

if __name__ == "__main__":
    main()
