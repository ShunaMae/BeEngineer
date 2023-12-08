import requests

r=requests.get("http://example.com")
# HTMLのコードを取得することができる
print(r.status_code)
print(r.text)