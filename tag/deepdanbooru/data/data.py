from typing import Any

import tensorflow as tf
import tensorflow_io as tfio

from ..image import transform_and_pad_image

def load_tags(tags_path):
    with open(tags_path, "r") as tags_stream:
        tags = [tag for tag in (tag.strip() for tag in tags_stream) if tag]
        return tags

def load_image_for_evaluate(
    image_raw: bytes, width: int, height: int, normalize: bool = True
) -> Any:
    try:
        image = tf.io.decode_png(image_raw, channels=3)
    except:
        image = tfio.image.decode_webp(image_raw)
        image = tfio.experimental.color.rgba_to_rgb(image)

    image = tf.image.resize(
        image,
        size=(height, width),
        method=tf.image.ResizeMethod.AREA,
        preserve_aspect_ratio=True,
    )
    image = image.numpy()  # EagerTensor to np.array
    image = transform_and_pad_image(image, width, height)

    if normalize:
        image = image / 255.0

    return image
