import requests

response=requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()


lat=response.json()["iss_position"]["longitude"]
long=response.json()["iss_position"]["latitude"]
print(lat)
print(long)