import os
import tensorflow as tf

from .io import deserialize_from_json
from .data import load_tags


def load_model_from_project(project_path, compile_model=True):
    project_context_path = os.path.join(project_path, "project.json")
    project_context = deserialize_from_json(project_context_path)

    model_type = project_context["model"]
    model_path = os.path.join(project_path, f"model-{model_type}.h5")
    model = tf.keras.models.load_model(model_path, compile=compile_model)

    return model


def load_tags_from_project(project_path):
    tags_path = os.path.join(project_path, "tags.txt")

    return load_tags(tags_path)
