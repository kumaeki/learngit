import json
d=dict(name="kuma",age=20,score=88)
print(json.dumps(d))

jsonstr =  '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(jsonstr))