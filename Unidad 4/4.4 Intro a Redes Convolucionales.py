import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

#Cargar y preprocesar el MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reshape la data 
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

# Normalizar pixel values entre 0 y 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Convertir labels a one-hot encoding
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Crear el modelo CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Imprimir summary del model
model.summary()

# Entrenar
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2)

# Evaluar modelo
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc}')

# Obtener las predicciones
predictions = model.predict(test_images)

# Funcion para mostrar predicciones
def plot_image(predictions_array, true_label, img):
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions_array)
    true_label = np.argmax(true_label)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    plt.xlabel(f'{predicted_label} ({100 * np.max(predictions_array):2.0f}%)', color=color)

# Graficas las primeras 5 imagenes de test y sus labels 
num_images = 5
plt.figure(figsize=(10, 10))
for i in range(num_images):
    plt.subplot(1, num_images, i + 1)
    plot_image(predictions[i], test_labels[i], test_images[i].reshape(28, 28))
plt.show()