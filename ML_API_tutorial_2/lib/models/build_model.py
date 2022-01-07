import pandas as pd
import pickle


def build_model():
    # current df_path is absolute, deployed version should have a relative path
    df_path = '//ML_API_tutorial_2/lib/data/glucose.csv'
    # read csv path and create df
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

    # load sklearn models
    from sklearn.linear_model import LinearRegression
    lin_model = LinearRegression()
    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor(n_estimators=100, max_features=3, random_state=1)

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

    # pickle models
    rf_filename = 'rf_model'
    lr_filename = 'lr_model'
    pickle.dump(model, open(rf_filename, 'wb'))
    pickle.dump(lin_model, open(lr_filename, 'wb'))


if __name__ == "__main__":
    build_model()
