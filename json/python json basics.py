import json

x = '{"name": "jhon", "age":30}'


y = json.loads(x)


print(y["age"])