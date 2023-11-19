from typing import List, IO, Dict
from pathlib import Path

import tensorflow as tf

SIZE = 512

tags = []
with open(str(Path(__file__).parent / "tags.txt")) as f:
    while line := f.readline():
        if striped := line.strip():
            tags.append(striped)

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path=str(Path(__file__).parent / "tagv3.tflite"))
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


@tf.function
def process_data(content):
    global SIZE
    img = tf.io.decode_image(content, channels=3)
    img = tf.image.resize_with_pad(img, SIZE, SIZE, method="nearest")
    img = tf.image.resize(img, (SIZE, SIZE), method="nearest")
    img = img / 255
    return img


def predict(content):
    global input_details, output_details, interpreter
    data = process_data(content)
    data = tf.expand_dims(data, 0)
    interpreter.set_tensor(input_details[0]['index'], data)
    interpreter.invoke()
    out = interpreter.get_tensor(output_details[0]['index'])[0]
    return dict((tags[i], out[i]) for i in range(len(tags)))


def predict_file(files: List[IO], limit: float) -> List[Dict]:
    r = []
    for file in files:
        data = predict(file.read())
        ret = filter(lambda x: x[1] > limit, data.items())
        ret = map(lambda x: (x[0], float(x[1])), ret)
        r.append(dict(ret))
    return r

if __name__ == "__main__": # test predict
    with open("test.jpeg", "rb") as f:
        print(predict_file([f], 0.5))
        '''
        [{
            "1girl": 0.9992879629135132,
            "bangs": 0.8319069147109985,
            "bare_shoulders": 0.7082091569900513,
            "blonde_hair": 0.8493882417678833,
            "blue_eyes": 0.951820433139801,
            "breasts": 0.9401402473449707,
            "full_body": 0.9114283323287964,
            "jewelry": 0.5107837915420532,
            "kneeling": 0.5597050189971924,
            "large_breasts": 0.6945455074310303,
            "long_hair": 0.9934541583061218,
            "looking_at_viewer": 0.8562065958976746,
            "one-piece_swimsuit": 0.6287702322006226,
            "smile": 0.6493669748306274,
            "solo": 0.9711495637893677,
            "thighhighs": 0.9874925017356873,
            "transparent_background": 0.999941349029541,
            "very_long_hair": 0.7977390289306641,
            "white_legwear": 0.9460241794586182,
            "rating:safe": 0.9942449331283569
        }]
        '''
