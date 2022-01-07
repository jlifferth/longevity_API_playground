import numpy as np
from flask import Flask, request, jsonify
from lib.models.run_model import run_model
from lib.models.transform_data import process_array

app = Flask(__name__)


# model = run_model()


@app.route('/')
def home():
    return """Welcome to the Longevity API"""


@app.route('/predict', methods=['GET'])
def predict():
    glucose_array = request.args.get('glucose_array')
    # return "glucose array received {}".format(glucose_array)

    glucose_array = glucose_array.split(',')
    # return "glucose array received {}".format(glucose_array)

    glucose_array = [float(x) for x in glucose_array]
    # return "glucose array received {}".format(glucose_array)

    glucose_array = np.asarray(glucose_array, dtype=np.float32)
    # return "glucose array received, datatype is {} {}".format(type(glucose_array), glucose_array)

    glucose_array = process_array(glucose_array)
    # return "glucose array received {}".format(glucose_array)

    result = run_model(glucose_array)

    return "glucose array received {}".format(result)

    # print(glucose_array)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
