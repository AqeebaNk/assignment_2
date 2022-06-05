import json

x = { "cars":["bmw","audi","ferrari"],"brands":["ncbab","abksb"]}
z = {'name':'Fatha','lastname':'JKD'}
y = json.dumps(x)
z1 = json.dumps(z)
file = open("myfile.json",'a')
file.write(y)
