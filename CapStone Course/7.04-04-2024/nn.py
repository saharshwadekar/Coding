import tensorflow as tf
from tensorflow import keras
from tensforflow.
from tensorflow.keras.layers import Dense
from IPython.display import Image

# Create a simple neural network model
model = keras.Sequential([
    Dense(128, activation='relu', input_shape=(784,), name='new_input_layer'),
    Dense(64, activation='relu', name='hidden_layer'),
    Dense(10, activation='softmax', name='output_layer')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Visualize the model architecture
tf.keras.utils.plot_model(model, to_file='neural_network.png', show_shapes=True, show_layer_names=True)

# Display the image of the neural network architecture
Image(filename='neural_network.png')
