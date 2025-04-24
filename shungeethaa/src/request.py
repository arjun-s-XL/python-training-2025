import requests

response = requests.get('https://www.google.com/search?q=gemini&oq=&gs_lcrp=EgZjaHJvbWUqCQgCEEUYOxjCAzIJCAAQRRg7GMIDMgkIARBFGDsYwgMyCQgCEEUYOxjCAzIJCAMQRRg7GMIDMgkIBBBFGDsYwgMyCQgFEEUYOxjCAzIJCAYQRRg7GMIDMgkIBxBFGDsYwgPSAQw0Njg2NjQwNGowajeoAgiwAgHxBWIWDUJdCNZW&sourceid=chrome&ie=UTF-8')

print(response.status_code)  # 200 means OK
print(response.text)         # The raw response body
print(response.json())       # If it's JSON, parse it
