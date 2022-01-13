import sqlite3
import time

import numpy as np
from flask import Flask, request

from lib.models.run_model import run_model
from lib.models.transform_data import process_array

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return """Welcome to the Longevity API"""


@app.route('/predict', methods=['GET'])
def predict():
    t1_start = time.process_time()

    remote_address = request.remote_addr
    print('remote address: ', str(remote_address))

    glucose_array = request.args.get('glucose_array')
    glucose_received = str(glucose_array)
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
    t1_stop = time.process_time()
    elapsed_time = t1_stop - t1_start

    print("Elapsed time:",
          elapsed_time)
    conn = get_db_connection()
    conn.execute("INSERT INTO requests (remote_address, received, prediction, runtime) VALUES (?, ?, ?, ?)",
                 (remote_address, glucose_received, result, elapsed_time))
    conn.commit()
    conn.close()

    return "glucose array received\n prediction: {}".format(result)

    # print(glucose_array)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
