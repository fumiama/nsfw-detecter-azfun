import json

def deserialize_from_json(path, encoding="utf-8"):
    with open(path, "r", encoding=encoding) as stream:
        return json.loads(stream.read())
