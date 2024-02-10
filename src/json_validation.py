import json
# jsonschema is an implementation of the JSON Schema specification for Python.
import jsonschema
from jsonschema import validate
from pprint import pprint

transaction_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
            "InvoiceNo": {
                "type": "integer"
            },
        "StockCode": {
                "type": "integer"
                },
        "Description": {
                "type": "string"
                },
        "Quantity": {
                "type": "integer",
                },
        "InvoiceDate": {
                "type": "string"
                },
        "UnitPrice": {
                "type": "number"
                },
        "CustomerID": {
                "type": "integer"
                },
        "Country": {
                "type": "string"
                }
    },
    "required": [
        "InvoiceNo",
        "StockCode",
        "Quantity",
        "CustomerID",
        "InvoiceDate",
        "UnitPrice"

    ]
}

# create a validation function


def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True


def validate_json_schema(json_data, my_schema):
    """REF: https://json-schema.org/ """
    schema = my_schema
    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is not valid "
        return False, err
    message = "Given JSON is valid."
    return True, message


if __name__ == '__main__':

    # create JSON schema with attributes and types

    # JSON validation

    with open("./data/data_subset.json") as json_file:
        data = json.load(json_file)

    valid_transaction_dict = data[0]
    pprint(valid_transaction_dict)

    res = validate(instance=valid_transaction_dict, schema=transaction_schema)
    # > None
    print(res)

    print("############################################################################################")
    customer_id_missing_dict = {
        "InvoiceNo": 536370,
        "StockCode": 22492,
        "Description": "MINI PAINT SET VINTAGE",
        "Quantity": 36,
        "InvoiceDate": "12/1/2010 8:45",
        "UnitPrice": 0.65,
        "Country": "France"
    }
    ############################################################################################
    # 1- Just tests with the validate function that throws an error directly
    ############################################################################################

    # uncomment the line below to see the error from the wrong JSON
    # validate(instance=customer_id_missing_dict, schema=transaction_schema)

    InvoiceNo_is_a_string = {
        "InvoiceNo": "536370",
        "StockCode": 22492,
        "Description": "MINI PAINT SET VINTAGE",
        "Quantity": 36,
        "InvoiceDate": "12/1/2010 8:45",
        "UnitPrice": 0.65,
        "CustomerID": 12583,
        "Country": "France",
        "CustomerID": 12583,
    }
    # validate(instance=InvoiceNo_is_a_string, schema=transaction_schema)

    ############################################################################################
    # 2- Tests with the custom validate_json function
    ############################################################################################

    # Load valid JSON string
    valid_json_string = json.dumps(valid_transaction_dict)

    # Create invalid JSON string - missing ',' delimiter
    invalid_json_string = '{"InvoiceNo": 536370 "StockCode": 22492, "Description":  "MINI PAINT SET VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45",   "UnitPrice": 0.65, "CustomerID": 12583, "Country": "France"}'

    # validate valid json string
    res = validate_json(valid_json_string)
    print(res)
    print("############################################################################################")

    # validate INVALID json string
    res = validate_json(invalid_json_string)
    print(res)
    print("############################################################################################")

    # validate data with valid schema
    res = validate_json_schema(
        valid_transaction_dict,  my_schema=transaction_schema)
    print(res)
    # > (True, 'Given JSON data is Valid')
    print("############################################################################################")

    # validate data with invalid schema
    res = validate_json_schema(
        InvoiceNo_is_a_string,  my_schema=transaction_schema)

    print("############################################################################################")

    print(res)
