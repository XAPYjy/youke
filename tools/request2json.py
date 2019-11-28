import json


def req2json(request):
    bytes = request.read()
    json_data = json.loads(bytes.decode('utf-8'))
    return json_data