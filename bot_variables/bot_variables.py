from os import getenv
from flask import Flask

app = Flask(__name__)
url = f'https://api.telegram.org/bot{getenv("TOKEN")}/'
