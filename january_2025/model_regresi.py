import tensorflow as tf
import numpy as np

#Generating the data // y = 5x - 3
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-8.0, -3.0, 2.0, 7.0, 12.0, 17.0], dtype=float)

#Define and compile the Neural Network
model = tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1)
])

model.compile(optimizer='sgd', loss='mean_squared_error')

#Training the NN
model.fit(xs, ys, epochs=500)

#Predicting : suppose to be 47
print(f"Model predicted: {model.predict(np.array([10.0]), verbose=0).item():.5f}")