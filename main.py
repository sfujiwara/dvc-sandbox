from datasets import load_dataset
import tensorflow_datasets as tfds

# dataset = load_dataset("blimp")
ds = tfds.load("mnist")

import IPython;IPython.embed()
