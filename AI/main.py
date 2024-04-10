from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np

# Загрузка модели
def prediction(img_path, model_name):

    # Загрузка модели
    model = tf.keras.models.load_model(model_name)

    # Загрузка нового изображения
    img = image.load_img(img_path, target_size=(150, 150))

    # Преобразование изображения в массив numpy и масштабирование значений пикселей
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.

    # Предсказание класса изображения
    prediction = model.predict(img_array)

    # Вывод результата
    if prediction > 0.5:
        print("График линейный")
    else:
        print("График не линейный")
    return prediction

print(prediction('graphs/graphsLinear/graph_2.png','model.keras'))