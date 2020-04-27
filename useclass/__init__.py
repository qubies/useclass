import tensorflow.compat.v1 as tf
import tensorflow_hub as hub

tf.disable_v2_behavior()

from myutils import print_banner_completion_wrapper

from myutils import *
import os


class Use:
    @print_banner_completion_wrapper("Initializing USE")
    def __init__(self):
        with tf.Graph().as_default():
            sentences = tf.placeholder(tf.string)
            embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder/4")
            embeddings = embed(sentences)
            session = tf.train.MonitoredSession()
        self.USE = lambda x: session.run(embeddings, {sentences: x})
        self.mm = None

    def embed(self, s):
        return self.USE([s])[0]

    def batch_embed(self, sentences):
        return self.USE(sentences)


if __name__ == "__main__":
    U = USE()
    while True:
        print(U.batch_embed([input("enter a sentence: "), input("next!")]))
