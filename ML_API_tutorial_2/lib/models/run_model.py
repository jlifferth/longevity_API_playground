import pickle
import time

import pandas as pd
import numpy as np


def run_model(test_array):
    # from ML_API_tutorial_2.lib.models.transform_data import process_array
    # processed_array = process_array(test_array)

    rf_filename = 'lib/models/lr_model'
    lr_filename = 'lib/models/rf_model'
    loaded_rf_model = pickle.load(open(rf_filename, 'rb'))
    loaded_lr_model = pickle.load(open(lr_filename, 'rb'))

    # make Random Forest Regressor prediction
    rf_pred = loaded_rf_model.predict(test_array)

    # make Linear Regression prediction
    lr_pred = loaded_lr_model.predict(test_array)

    # combine Aggregate predictions
    # rf_pred = rf_pred.reshape(-1, 1)
    lr_pred = lr_pred.reshape(-1, 1)

    aggregate_pred = np.mean(np.array([lr_pred, rf_pred]), axis=0)
    # print('process time: ')
    # print(time.process_time())
    return aggregate_pred


# df = pd.read_csv('../data/glucose.csv')
# array = np.array(df['glucose'])[:100]
# # array = array.reshape(-1, 1)
# print(array)
# print(run_model(array))
