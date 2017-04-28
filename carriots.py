import json
import requests


def send(device, datos, api_key):
    """
    Envía los datos recogidos por un device a la api de carriots
    :param device El dispositivo, Ej: resistencia@juandalibaba.juandalibaba
    :param datos: un diccionario con los datos a enviar
    :return: la respuesta HTTP
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
