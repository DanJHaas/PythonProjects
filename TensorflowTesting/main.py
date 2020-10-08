# Import `tensorflow`
import tensorflow as tf

# Build a graph.
tf.compat.v1.disable_eager_execution()
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b

# Launch the graph in a session.
sess = tf.compat.v1.Session()

# Evaluate the tensor `c`.
print(sess.run(c)) # prints 30.0