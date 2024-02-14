# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://api.trello.com//cards/65818c5eda9d5419f0c4a4d0"
url_cards = "https://api.trello.com/1/boards/22anUFBN"
url_lists = "https://api.trello.com/1/boards/22anUFBN/lists"
url_members = "https://api.trello.com/1/boards/22anUFBN/members"
url_archive = "https://api.trello.com/1/boards/22anUFBN/checkItemStates"
headers = {
  "Accept": "application/json"


}

query = {
  'cards': 'all',
  'key': '***',
  'token': '****'
}

query_all = {
  'key': '***',
  'token': '****'
}



response_cards = requests.request(
   "GET",
   url_cards,
   #cards='all',
   headers=headers,
   params=query
)

response_lists = requests.request(
   "GET",
   url_lists,
   headers=headers,
   params=query_all
)

response_members = requests.request(
   "GET",
   url_members,
   headers=headers,
   params=query_all
)



#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))