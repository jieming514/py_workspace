import json

# python 处理json

## json 转换成字符串
json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

parsed_json = json.loads(json_string)

print('first_name:', parsed_json["first_name"])
print('last_name:', parsed_json["last_name"])


## 对账转换成json格式
d = {
    'first_name': 'Guido',
    'second_name': 'Rossum',
    'titles': ['BDFL', 'Developer'],
}
print(json.dumps(d))