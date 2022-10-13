from typing import Any, List, Dict

from .data import load_image_for_evaluate

def evaluate_image(
    image_input: bytes, model: Any, tags: List[str], threshold: float
) -> Dict[str, float]:
    width = model.input_shape[2]
    height = model.input_shape[1]

    image = load_image_for_evaluate(image_input, width=width, height=height)

    image_shape = image.shape
    image = image.reshape((1, image_shape[0], image_shape[1], image_shape[2]))
    y = model.predict(image)[0]
    del image

    result_dict = {}

    for i, tag in enumerate(tags):
        if y[i] >= threshold: result_dict[tag] = float(y[i])

    del y

    return result_dict
