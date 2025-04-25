import requests

url = "https://openai.com/"
try:
    response = requests.get(url)
    print(response.status_code)
except Exception as e:
    print("Invalid link")
    print("Error:", e)
