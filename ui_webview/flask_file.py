from flask import Flask, render_template, request, jsonify
from ui_webview.unitconverter.converter import convert_units

from . import __name__

flask_app = Flask(__name__)


@flask_app.route('/')
def index():
    return render_template("index.html")


@flask_app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    value = float(data['value'])
    from_unit = data['from_unit']
    to_unit = data['to_unit']

    result = convert_units(value, from_unit, to_unit)

    return jsonify({'result': result})
