import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.shape_base import column_stack
import pandas as pd
import random
from pandas.core.frame import DataFrame
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.python.keras.utils.tf_utils import dataset_is_infinite
main_list = []
def main(months, datalist):
    for i in range(months):

        df = pd.read_csv("random_dataset.csv")
        total_rows = df['Subs_Gained'].count() 
        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = scaler.fit_transform(df["Subs_Gained"].values.reshape(-1,1))   
        prediction_week = 12

        x_train = []
        y_train = []

        for x in range(prediction_week, len(scaled_data)):
            x_train.append(scaled_data[x-prediction_week:x, 0])
            y_train.append(scaled_data[x, 0])

        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

        model = Sequential()

        model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50))
        model.add(Dropout(0.2))
        model.add(Dense(units=1))

        model.compile(optimizer='adam', loss='mean_squared_error')
        model.fit(x_train, y_train, epochs=100, batch_size=32)

        model_inputs = df[len(df) - prediction_week:].values
        model_inputs = model_inputs.reshape(-1,1)
        model_inputs = scaler.transform(model_inputs)

        real_data = [model_inputs[len(model_inputs)+1 - prediction_week:len(model_inputs+1), 0]]
        real_data = np.array(real_data)
        real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1],1))

        prediction = model.predict(real_data)
        prediction = scaler.inverse_transform(prediction)
        prediction = round(prediction[0][0])
        new_week = total_rows + i + 1
        to_append = [new_week, prediction]
        datalist.append(to_append)
        print(i+1)
    return datalist

#main = main(4, main_list)
#subs = 0
#for i in main:
#    subs+=i[1]
#print(subs)
