# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import *
import json

app = Flask(__name__)

@app.route('/', methods= ['GET'])
def home_page():
    VEGITABLES_PRICES = {
        "Winter": {
            "Peas": "50",
            "Broccoli": "200",
            "Carrots": "50"
        },
        "Summer": {
            "Potatos": "50",
            "Beetroot": "50",
            "Cucumber": "40"
        },
        "Spring": {
            "Garlic": "40",
            "Mushroom": "120",
            "okra": "60"
        }
    }

    json_dump = json.dumps(VEGITABLES_PRICES)

    return json_dump

@app.route('/user/', methods= ['GET'])
def request_page():
    user_query = str(request.args.get("user")) #/user/?user=USER_NAME
    VEGITABLES_Weights = {
        "Winter": {
            "Peas": "2kg",
            "Broccoli": "5kg",
            "Carrots": "5kg"
        },
        "Summer": {
            "Potatos": "5kg",
            "Beetroot": "1kg",
            "Cucumber": "3kg"
        },
        "Spring": {
            "Garlic": "4kg",
            "Mushroom": "1kg",
            "okra": "6kg"
        }
    }
    json_dump = json.dumps(VEGITABLES_Weights)

    return json_dump

if __name__ =='__main__':
    app.run(port=7777)



