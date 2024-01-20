import json
from typing import List, Optional

class JsonValidator:
    def __init__(self):
        pass

    def validate(self, json_data: dict, schema: dict) -> bool:
        try:
            
            if not self.check_required_fields(json_data, schema):
                return False

            
            if not self.check_at_least_one_of_fields(json_data, schema):
                return False

            
            if not self.check_either_one_field_or_another(json_data, schema):
                return False

            
            if not self.check_mutually_exclusive_fields(json_data, schema):
                return False

            
            if not self.check_field_value_in_set(json_data, schema):
                return False

            
            return True

        except Exception as e:
            print(f"Error during validation: {e}")
            return False

    def check_required_fields(self, json_data: dict, schema: dict) -> bool:
        required_fields = schema.get("required", [])
        for field in required_fields:
            if field not in json_data:
                print(f"Required field '{field}' is missing.")
                return False
        return True

    def check_at_least_one_of_fields(self, json_data: dict, schema: dict) -> bool:
        one_of_fields_list = schema.get("at_least_one_of", [])
        present_fields_count = sum(1 for field in one_of_fields_list if field in json_data)
        if present_fields_count < 1:
            print(f"At least one of the fields {one_of_fields_list} is required.")
            return False
        return True

    def check_either_one_field_or_another(self, json_data: dict, schema: dict) -> bool:
        either_one_of_pairs = schema.get("either_one_of", [])
        for field1, field2 in either_one_of_pairs:
            if field1 in json_data and field2 in json_data:
                print(f"Either {field1} or {field2} is required, but both are present.")
                return False
            elif field1 not in json_data and field2 not in json_data:
                print(f"At least one of {field1} or {field2} is required.")
                return False
        return True

    def check_mutually_exclusive_fields(self, json_data: dict, schema: dict) -> bool:
        mutually_exclusive_pairs = schema.get("mutually_exclusive", [])
        for field1, field2 in mutually_exclusive_pairs:
            if field1 in json_data and field2 in json_data:
                print(f"{field1} and {field2} are mutually exclusive but both are present.")
                return False
        return True

    def check_field_value_in_set(self, json_data: dict, schema: dict) -> bool:
        field_values = schema.get("field_values", {})
        for field, allowed_values in field_values.items():
            if field in json_data and json_data[field] not in allowed_values:
                print(f"Value of field {field} is not in the allowed values: {allowed_values}.")
                return False
        return True