import requests

BASE_URl = "https://api.punkapi.com/v2/"

# Get status code
response = requests.get(BASE_URl + "beers")
print(response.status_code)

# get headers
print(response.headers)

# get beer
all_beers = response.json()
print(all_beers[0])

# get beer between 20 and 30 ABV
payload = {
    "abv_gt": 20,
    "abv_lt": 30
}

response = requests.get(BASE_URl + "beers", params=payload)
print(response)

beers_between_20_and_30_percent = response.json()

# url request was sent to
print(response.url)

# print length of beers between 20 and 30 percent
print(len(beers_between_20_and_30_percent))

# List of all the keys

# print(beers_between_20_and_30_percent[0].keys())


#  get beer names and alcohol percentages
# beer_summary = [
#     {
#         "beer_name": beer.get("name"),
#         "beer_alcohol": beer.get("abv")
#     }
# ]

# # print(beer_summary)
# for beer in beers_between_20_and_30_percent:
#     print(beer.get("name"), beer.get("abv"))

# # get beer with id 1


response = requests.get(f'{BASE_URl}/beers/{1}')
print(response.status_code)

beer_no_1 = response.json()
print(len(beer_no_1))
print(beer_no_1)


# Fake data API
BASE_URL = "https://reqres.in/api"
response = requests.get(BASE_URL + "/users")
print(response.status_code)
print(response.json())

# get user with id 3
response = requests.get(BASE_URL + "/users/3")
print(response.status_code)
print(response.json())

# create a user
user = {
    "name": "morpheus",
    "job": "mata data engineer"
}

response = requests.post(BASE_URL + "/users", data=user)
print(response)

# print content of the new user created
print(response.json())
