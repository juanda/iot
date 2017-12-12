import json
import requests

def send(device, datos, api_key):
    """
    Sends data gathered by a device to carriots through API
    :param device  Example: resistencia@juandalibaba.juandalibaba
    :param datos:  a dict with data to send
    :return:  the response  HTTP
    """

    h = {
        'Carriots.apiKey': api_key,
        'Content-Type': 'application/json; charset=utf-8'
    }

    payload = {
        'at': 'now',
        'protocol': 'v1',
        'data': datos,
        'device': device
    }

    r = requests.post('https://api.carriots.com/streams/', headers=h, data=json.dumps(payload))

    return r
