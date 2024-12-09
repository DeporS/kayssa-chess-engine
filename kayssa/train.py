import pandas as pd
import numpy as np

from feature_extractor import board_vector_from_fen
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras import models, layers
import keras

def train_model():
    data = pd.read_csv("files/positions_with_eval.csv")

    X = []
    y = []

    # getting vector from fen
    for index, row in data.iterrows():
        fen = row["FEN"]
        eval_value = row["Eval"]

        vector = board_vector_from_fen(fen)
        X.append(vector)
        y.append(eval_value)

    X = np.array(X)
    y = np.array(y)

    # splitting data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = models.Sequential([
        layers.Dense(512, input_dim=768, activation='relu'), 
        layers.Dense(256, activation='relu'),
        layers.Dense(128, activation='relu'),
        layers.Dense(1) 
    ])

    model.compile(optimizer='adam', loss='mse')

    # model training
    model.fit(X_train, y_train, epochs=25, batch_size=32, validation_data=(X_test, y_test))

    # model loss
    loss = model.evaluate(X_test, y_test)
    print(f"Test loss: {loss}")

    # save model
    model.save("kayssa.keras")

def fine_tune_model():
    model = keras.models.load_model("kayssa.keras")

    # read data from file
    data = pd.read_csv("files/positions_with_eval.csv")

    X = []
    y = []

    # getting vector from fen
    for index, row in data.iterrows():
        fen = row["FEN"]
        eval_value = row["Eval"]

        vector = board_vector_from_fen(fen)
        X.append(vector)
        y.append(eval_value)

    X = np.array(X)
    y = np.array(y)

    # fine tune model
    model.fit(X, y, epochs=25, batch_size=32)

    # save tuned model
    model.save("kayssa.keras")

#train_model()
fine_tune_model()