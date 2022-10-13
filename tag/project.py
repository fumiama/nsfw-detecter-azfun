import os
import tensorflow as tf

from .io import deserialize_from_json
from .data import load_tags


def load_model_and_tags_from_project(project_path):
    project_context_path = os.path.join(project_path, "project.json")
    project_context = deserialize_from_json(project_context_path)

    model_type = project_context["model"]
    model_path = os.path.join(project_path, f"model-{model_type}.h5")

    tags_path = os.path.join(project_path, "tags.txt")
    tags = load_tags(tags_path)

    with tf.device("/CPU:0"):
        model =  tf.keras.models.load_model(model_path, compile=True)

    return model, tags
