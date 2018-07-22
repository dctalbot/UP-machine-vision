"""Control routes under root."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os, time

import numpy as np
import tensorflow as tf

from website import app
from werkzeug.utils import secure_filename
from flask import render_template, url_for, request, redirect, g, session
from website.config import IMAGES_FOLDER


# ==============================
# =======     ROUTING    =======
# ==============================

@app.route('/', methods = ['GET', 'POST'])
def home():
    """Show homepage."""

    #just save an upload
    if request.method == 'POST':
        file = request.files.get('file', '')
        filename = secure_filename(file.filename)
        file_dest = os.path.dirname(__file__) + '/uploads/' + filename
        file_dest = IMAGES_FOLDER + filename
        file.save(file_dest)

    return render_template("index.html")


@app.route('/<filename>')
def test(filename):
    """Show homepage."""
    context = {
        'type': 'before',
        'result': ''
    }

    file_dest = IMAGES_FOLDER + filename
    img_type = run_image_label(file_dest, 'all')

    img_index = np.argmax(img_type['results'], axis=0)
    print(img_index)

    guess = img_type['labels'][img_index]
    print(guess)

    stats = run_image_label(file_dest, guess)
    # results = [0.27753016, 0.7224698]
    context['normal_pct'] = stats['results'][1]
    context['broken_pct'] = stats['results'][0]

    context['stats'] = stats

    context['filename'] = filename
    context['guess'] = guess

    return render_template("stats.html", **context)


def run_image_label(file_name, image_type):
    print('running')
    input_height = 299
    input_width = 299
    input_mean = 0
    input_std = 255
    input_layer = "input"
    output_layer = "InceptionV3/Predictions/Reshape_1"

    model_file = os.path.dirname(__file__) + '/tf/' + image_type + '/retrained_graph.pb'
    label_file = os.path.dirname(__file__) + '/tf/' + image_type + '/retrained_labels.txt'
    input_layer = "Placeholder"
    output_layer = "final_result"

    graph = load_graph(model_file)
    t = read_tensor_from_image_file(
        file_name,
        input_height=input_height,
        input_width=input_width,
        input_mean=input_mean,
        input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    with tf.Session(graph=graph) as sess:
      results = sess.run(output_operation.outputs[0], {
          input_operation.outputs[0]: t
      })
    results = np.squeeze(results)

    top_k = results.argsort()[-5:][::-1]
    labels = load_labels(label_file)

    # table of label, percent pairs
    for i in top_k:
      print(labels[i], results[i])

    toreturn = dict()
    toreturn['results'] = results
    toreturn['labels'] = labels

    return toreturn


def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph


def read_tensor_from_image_file(file_name,
                                input_height=299,
                                input_width=299,
                                input_mean=0,
                                input_std=255):
  input_name = "file_reader"
  output_name = "normalized"
  file_reader = tf.read_file(file_name, input_name)
  if file_name.endswith(".png"):
    image_reader = tf.image.decode_png(
        file_reader, channels=3, name="png_reader")
  elif file_name.endswith(".gif"):
    image_reader = tf.squeeze(
        tf.image.decode_gif(file_reader, name="gif_reader"))
  elif file_name.endswith(".bmp"):
    image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
  else:
    image_reader = tf.image.decode_jpeg(
        file_reader, channels=3, name="jpeg_reader")
  float_caster = tf.cast(image_reader, tf.float32)
  dims_expander = tf.expand_dims(float_caster, 0)
  resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
  normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
  sess = tf.Session()
  result = sess.run(normalized)

  return result


def load_labels(label_file):
  label = []
  proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
  for l in proto_as_ascii_lines:
    label.append(l.rstrip())
  return label
