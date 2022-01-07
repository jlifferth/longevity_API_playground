import pandas as pd
import numpy as np


def json_to_array():
    # this function will convert JSON format glucose data received via GET request
    # and convert to numpy array for use in model
    pass


def process_array(array_in):
    array_in = array_in.reshape(-1, 1)
    df = pd.DataFrame(array_in)
    df.columns = ['glucose']
    # df = df.drop(columns=['Unnamed: 0'])

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

    x1, x2, x3, y = df[frame_1], df[frame_2], df[frame_3], df['glucose']
    x1, x2, x3, y = np.array(x1), np.array(x2), np.array(x3), np.array(y)
    x1, x2, x3, y = x1.reshape(-1, 1), x2.reshape(-1, 1), x3.reshape(-1, 1), y.reshape(-1, 1)
    final_x = np.concatenate((x1, x2, x3), axis=1)
    # final_x - final_x.reshape(-1, 1)
    return final_x


# csv_df = pd.read_csv('../data/glucose.csv')
# array = np.array(csv_df['glucose'])[:100]
# array = array.reshape(-1, 1)

# print(process_array(array))
