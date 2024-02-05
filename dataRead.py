from datetime import datetime


default_args={
    'owner':'airscholor',
    'start_date':datetime(2024, 2, 2, 10, 00)
}


def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]  # this results the object results with list[0]
    return res

def format_data(res):
    data = {}
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']

    return data


# this returns the api in a json format
def stream_data():
    import json
    res = get_data()
    res = format_data(res)
    print(json.dumps(res,indent=3))

# creating a dag

stream_data()