from jsonschema import validate


schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name"]

}

data = {
  #  "name" : 50,
    "age": 30
}

validate(instance=data, schema=schema)