'''
HelloWorld example using TensorFlow library.

Author: Satish Verma
Project: https://github.com/satishverma17/Tensorflow_Samples/
'''

from __future__ import print_function

import tensorflow as tf

# Simple hello world using TensorFlow

# Create a Constant op 
# This constant is added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.
hello = tf.constant('Hello, I am TensorFlow!')

# Start tf session
sess = tf.Session()

# Run the op
print(sess.run(hello))
