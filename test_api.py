import requests

BASE_URL = "http://127.0.0.1:8001/"
USERNAME = 'olesia'
PASSWORD = 'python1111'
auth=(USERNAME, PASSWORD)


print("---GET LIST:")
response = requests.get(BASE_URL + 'airports/', auth=auth)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

print("\n---GET BY ID")
response = requests.get(BASE_URL + 'airports/' + '1/', auth=auth)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

print("\n---CREATE ITEM")
airport_data = {
    "name": "Kyiv Boryspil",
    "code": "2566",
    "city": "Kyiv",
    "country": "Ukraine"
}
response = requests.post(BASE_URL + 'airports/', json=airport_data, auth=auth)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

print("\n---UPDATE ITEM BY ID")
airport_data = {
    "name": "Kyiv Boryspil",
    "code": "0000",
    "city": "Kyiv",
    "country": "Ukraine"
}
response = requests.put(BASE_URL + 'airports/' + '10/', json=airport_data, auth=auth)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

print("\n---DELETE ITEM BY ID")
response = requests.delete(BASE_URL + 'airports/' + '10/', auth=auth)
print("Status Code:", response.status_code)