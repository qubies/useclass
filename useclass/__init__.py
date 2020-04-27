import tensorflow as tf
import tensorflow_hub as hub

from myutils import print_banner_completion_wrapper


class USE:
    @print_banner_completion_wrapper("Initializing USE")
    def __init__(self):
        self.USE = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

    def embed(self, s):
        return self.USE([s])[0]

    def batch_embed(self, sentences):
        return self.USE(sentences)

