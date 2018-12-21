import requests

r = requests.get("http://www.douban.com")
print("r.status_code : ", r.status_code)
# print(r.text)

r = requests.get("http://www.douban.com",
                 params={"q": "python", "cat": "1001"})
print("r.url : ", r.url)
print("r.encoding :", r.encoding)

r = requests.get(
    'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print("r.josn() : ", r.json())
