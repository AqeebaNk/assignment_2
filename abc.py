import json
# from unicodedata import name
# # some JSON:
# a =  '{ "name":"Jack", "age":21, "city":"California"}'
# # parse x:
# b = json.loads(a)
# print(b["age"])


# Fruit_Dict1 = {
#   'name': 'Apple',
#   'color': 'Red',
#   'quantity': 10,
#   'price': 60
# }
# # Fruit_Json = json.dumps(Fruit_Dict)
# # print(Fruit_Json)
# Fruit_Json = json.load(Fruit_Dict1)
# print(Fruit_Json)

aqeeb= {
  "name":"aqeeb","age":35,"surname":"ank"
  
}
jamun = json.loads(aqeeb)
print(jamun[name])