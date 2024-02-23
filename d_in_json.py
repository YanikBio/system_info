import json

def json_decorator(way_to_file = 'json_data.json'):
    def in_json(func):
        def decor():
            data = func()
            with open(way_to_file, 'w') as file:
                json.dump(data, file)

            return data
        
        return decor
    return in_json