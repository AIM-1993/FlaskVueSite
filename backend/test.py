import requests
import json
r = requests.get("http://v.juhe.cn/weather/index?format=2&cityname=成都&key=3b0394793eab7b6318dcc358dd2b7b3b")
s = r.json()
print(s)