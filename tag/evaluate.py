from typing import Any, List, Dict

from .data import load_image_for_evaluate


def evaluate_image(
    image_input: bytes, model: Any, tags: List[str], threshold: float
) -> Dict[str, float]:
    d = model.get_input_details()[0]
    image = load_image_for_evaluate(image_input, width=d['shape'][1], height=d['shape'][2])
    del d

    image_shape = image.shape
    image = image.reshape((1, image_shape[0], image_shape[1], image_shape[2]))
    del image_shape

    y = model.get_signature_runner()(input_1=image)['activation_142'][0]
    del image

    result_dict = {}

    for i, tag in enumerate(tags):
        if y[i] >= threshold: result_dict[tag] = float(y[i])
    del y

    return result_dict
