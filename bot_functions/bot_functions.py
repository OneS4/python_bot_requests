from bot_variables import *
import json
import requests


def save_json(json_dict, filename='updates_users.json'):
    with open(filename, 'w') as file:
        json.dump(json_dict, file, indent=2)


def get_updates():
    url_local = url + 'getUpdates'
    response = requests.post(url_local)
    save_json(response.json())
    return response.json()


def send_message(chat_id, text):
    url_local = url + 'sendMessage'
    response = requests.post(url_local, json={'chat_id': chat_id, 'text': text})
    return response.json()


def send_sticker(chat_id, sticker, file_id_or_input_file=True):
    url_local = url + 'sendSticker'
    if file_id_or_input_file:
        response = requests.post(url_local, json={'chat_id': chat_id, 'sticker': sticker})
    else:
        response = requests.post(url_local + f'?chat_id={chat_id}', files={'sticker': open(sticker, 'rb')})
    return response.json()
