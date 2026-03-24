import requests
import json

LATITUDE=25.003660
LONGITUDE=93.894753


api_key="d86210ec1ad7af9c53d94be31c71296a"
api_url=f"https://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGITUDE}&appid={api_key}"


data=requests.get(api_url)
response=data.json()
print(response)
print("HTTP Status code-:",response["cod"])




