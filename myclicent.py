import requests

resp = requests.get("http://localhost:5000/hello?id=abc&pwd=1234"
print(resp.text)
print(resp.status_code)