# Import the json module
import json
from pprint import pprint
# pp = pprint.PrettyPrinter(indent=4)


# JSON basics


# Deserialization of JSON is a conversion of JSON objects into their respective Python objects using JSON decoder following the translations bellow.
# It is important to note here that the json.loads() method will not always return a dictionary. The following table shows JSON objects and the Python data types after conversion. For more details, see Python docs.

# JSON OBJECT	PYTHON OBJECT
# object	    dict
# array	        list
# string	    str
# null	        None
# number(int)	int
# number(real)	float
# true	        True
# false	        False

# Load JSON from file (deserialize text or binary file containing a JSON document to a Python object)


with open("./data/data_subset.json") as json_file:
    data = json.load(json_file)
pprint(data)


# Create JSON string (serialize object to a JSON formatted string) and pretty print of JSON string

json_formatted_string = json.dumps(data)
pprint(json_formatted_string)

# Load JSON string (deserialize a str, bytes or bytearray instance containing a JSON document to a Python object)

transactions_list_of_dicts = json.loads(json_formatted_string)
pprint(transactions_list_of_dicts)


# Access individual attributes within the object

# List of keys at the first list element (dictionary)
pprint(transactions_list_of_dicts[0].keys())
# > dict_keys(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'])

# Loop through a list of transactions and access all 'InvoiceNo' for each transaction by using .get method with a key name 'InvoiceNo'
for transaction in transactions_list_of_dicts:
    pprint(transaction.get('InvoiceNo'))
# > 536370
# > 536372
# > 536389
# > 562106

# or more pythonic via list comprehensions:

pprint([transaction.get('InvoiceNo')
       for transaction in transactions_list_of_dicts])
# > [536370, 536372, 536389, 562106]

# Modify the object's attributes
# Update a value of the transaction with a InvoiceNo 536370

# old dictionary:
# {
#         "InvoiceNo": 536370,
#         "StockCode": 22492,
#         "Description": "MINI PAINT SET VINTAGE",
#         "Quantity": 36,
#         "InvoiceDate": "12/1/2010 8:45",
#         "UnitPrice": 0.65,
#         "CustomerID": 12583,
#         "Country": "France"
#     }

# print the dictionary with InvoiceNo 536370
for transaction in transactions_list_of_dicts:
    if transaction.get('InvoiceNo') == 536370:
        pprint(transaction)
# > {'Country': 'France',
# >  'CustomerID': 12583,
# >  'Description': 'MINI PAINT SET VINTAGE',
# >  'InvoiceDate': '12/1/2010 8:45',
# >  'InvoiceNo': 536370,
# >  'Quantity': 36,
# >  'StockCode': 22492,
# >  'UnitPrice': 0.65}


# and replace it with new dictionary

update_dict = {
    "InvoiceNo": 1,
    "StockCode": 1,
    "Description": "Updated dict",
    "Quantity": 1,
    "InvoiceDate": "9/9/9999 9:99",
    "UnitPrice": 1,
    "CustomerID": 1,
    "Country": "Nowhere"
}

for transaction in transactions_list_of_dicts:
    if transaction.get('InvoiceNo') == 536370:
        transaction.update(update_dict)
pprint(transactions_list_of_dicts)


# Converting Python objects to JSON objects is also known as serialization or JSON encoding

# Dump it back into a string:

pprint(json.dumps(transactions_list_of_dicts))


# or to a file (do not forget to specify 'w' write mode):
with open("./data/dumped_json.json", 'w') as json_file:
    json.dump(transactions_list_of_dicts, json_file)
