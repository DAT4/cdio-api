import requests

url = 'http://localhost:8000/'
r = requests.get(url)
print(r)
print(r.text)

url = 'http://localhost:8000/upload/'

headers = {
    'accept': 'application/json',
    'Content-Type': 'multipart/form-data',
}


files = {
    'file': ('ace.jpg', open('../ace.jpg', 'rb'),'image/jpg'),
}

r = requests.post('http://localhost:8000/upload/', headers=headers, files=files)

print(r)

