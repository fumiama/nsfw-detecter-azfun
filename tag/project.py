import os
import tensorflow as tf

from .data import load_tags


def load_model_and_tags_from_project(project_path):
    model_path = os.path.join(project_path, "model-resnet_custom_v3.h5")
    tags_path = os.path.join(project_path, "tags.txt")
    tags = load_tags(tags_path)
    model = tf.keras.models.load_model(model_path, compile=True)
    return model, tags
