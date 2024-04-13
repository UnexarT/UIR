import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Создание датасета изображений
datagen = ImageDataGenerator(rescale=1./255)
dataset = datagen.flow_from_directory('graphs',
                                      target_size=(150, 150),
                                      batch_size=32,
                                      class_mode='binary')

# Создание модели нейронной сети
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Компиляция модели
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Создание обратного вызова для сохранения модели после каждой эпохи
checkpoint_cb = tf.keras.callbacks.ModelCheckpoint('model.keras', save_best_only=True)

# Создание обратного вызова для остановки обучения, когда качество на валидационном наборе не улучшается
early_stopping_cb = tf.keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)

# Обучение модели с обратными вызовами
model.fit(dataset, epochs=30, callbacks=[checkpoint_cb, early_stopping_cb])

model.save('model.keras')