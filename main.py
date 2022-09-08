from flask import request, jsonify

from bot_functions import *


@app.route('/setWebhook<path:url_webhook>')
def set_webhook(url_webhook):
    url_local = url + 'setWebhook'
    response = requests.get(url_local, json={'url': url_webhook, 'drop_pending_updates': True})
    return response.json()


@app.route('/deleteWebhook')
def delete_webhook():
    url_local = url + 'deleteWebhook'
    response = requests.get(url_local)
    return response.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        response = request.get_json()
        save_json(response, 'update_user.json')
        save_json(send_sticker(response['message']['chat']['id'], 'bot_stickers/sticker.webp', False), 'update_bot.json')
        return jsonify(response)
    return ''


if __name__ == '__main__':
    app.run(debug=True)
