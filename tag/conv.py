import tensorflow as tf

model = tf.keras.models.load_model('model-resnet_custom_v3.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("tagv3.tflite", "wb").write(tflite_model)
