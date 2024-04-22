import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# Define a simple neural network model
model = tf.keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Visualize the model architecture using Matplotlib
tf.keras.utils.plot_model(model, to_file='model.png', show_shapes=True)

# Display the model architecture plot
img = plt.imread('model.png')
plt.imshow(img)
plt.axis('off')
plt.show()
