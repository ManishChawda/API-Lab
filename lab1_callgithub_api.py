import requests

url = "https://api.github.com"

response = requests.get(url)

data = response.json()

print("Current User URL:", data["current_user_url"])
print("Repository Search URL:", data["repository_search_url"])
print("Rate Limit URL:", data["rate_limit_url"])


import requests
url = "https://api.github.com/search/repositories?q=python"

response = requests.get(url)

data = response.json()

print(type(data))
print(data.keys())
print(len(data["items"]))

print(data["items"][0]["full_name"])
print(data["items"][0]["description"])
print(data["items"][1]["full_name"])
print(data["items"][2]["full_name"])



