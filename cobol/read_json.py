import json
f = open('main.json','r')
data = json.load(f)
print(data)
f.close()