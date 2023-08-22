from flask import Flask, request, jsonify
import requests
import json


app = Flask(_name_)


@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    all_numbers = []

    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)
            response_data = response.json()
            numbers = response_data.get('numbers', [])
            all_numbers.extend(numbers)
        except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError):
            pass

    all_numbers = sorted(list(set(all_numbers)))

    return jsonify({'numbers': all_numbers})

if _name_ == '_main_':
    app.run(port=8008)
