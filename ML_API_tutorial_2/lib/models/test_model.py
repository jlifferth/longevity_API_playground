import pickle
import pandas as pd

# load the model from disk
rf_filename = 'rf_model'
lr_filename = 'lr_model'
loaded_rf_model = pickle.load(open(rf_filename, 'rb'))
loaded_lr_model = pickle.load(open(lr_filename, 'rb'))


def test_model(rf_model, lr_model):
    # read csv path and create df
    df_path = '//ML_API_tutorial_2/lib/data/glucose.csv'
    df = pd.read_csv(df_path)
    df = df.drop(columns=['Unnamed: 0'])

    # create time windows
    window_interval = 30  # time in minutes, smallest possible interval is 5 minutes

    frame_1 = 'glucose_minus_' + str(window_interval)
    frame_2 = 'glucose_minus_' + str(window_interval * 2)
    frame_3 = 'glucose_minus_' + str(window_interval * 3)

    frame_shift_1 = int(window_interval / 5)
    frame_shift_2 = int((window_interval * 2) / 5)
    frame_shift_3 = int((window_interval * 3) / 5)
    # print(frame_shift_1, frame_shift_2, frame_shift_3)

    df[frame_1] = df['glucose'].shift(+frame_shift_1)
    df[frame_2] = df['glucose'].shift(+frame_shift_2)
    df[frame_3] = df['glucose'].shift(+frame_shift_3)

    # drop na values
    df = df.dropna()
    # print(df)

    # assign models
    lin_model = loaded_lr_model
    model = loaded_rf_model

    # organize and reshape data
    import numpy as np
    x1, x2, x3, y = df[frame_1], df[frame_2], df[frame_3], df['glucose']
    x1, x2, x3, y = np.array(x1), np.array(x2), np.array(x3), np.array(y)
    x1, x2, x3, y = x1.reshape(-1, 1), x2.reshape(-1, 1), x3.reshape(-1, 1), y.reshape(-1, 1)
    final_x = np.concatenate((x1, x2, x3), axis=1)

    # split 70/30 into train and test sets
    X_train_size = int(len(final_x) * 0.7)
    set_index = len(final_x) - X_train_size
    # print(set_index)
    X_train, X_test, y_train, y_test = final_x[:-set_index], final_x[-set_index:], y[:-set_index], y[-set_index:]

    # fit models
    model.fit(X_train, y_train.ravel())  # random forest
    lin_model.fit(X_train, y_train)  # linear regression

    # make Random Forest Regressor prediction
    pred = model.predict(X_test)
    # make Linear Regression prediction
    lin_pred = lin_model.predict(X_test)
    # combine Aggregate predictions
    pred = pred.reshape(-1, 1)
    aggregate_pred = np.mean(np.array([lin_pred, pred]), axis=0)
    # print(aggregate_pred)

    return aggregate_pred


result = test_model(rf_model=loaded_rf_model, lr_model=loaded_lr_model)
print(result)
