import json


def req2json(request):
    bytes = request.read()
    if len(bytes) == 0:
        json_data = 1
    else:
        json_data = json.loads(bytes.decode('utf-8'))
        print(json_data)
    return json_data