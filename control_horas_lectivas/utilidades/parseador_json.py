import json

def encode_complex(obj):
    return obj.__dict__

def to_json(objeto):
    texto = json.dumps(objeto, default=encode_complex, skipkeys=True)
    return json.loads(texto)

def to_json_object(body):
    return json.loads(body.decode('utf-8'))