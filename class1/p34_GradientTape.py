import tensorflow as tf

with tf.GradientTape() as tape:
    x = tf.Variable(tf.constant(3.0))
    loss = tf.pow(x, 2)
grad = tape.gradient(loss, x)
print(grad)
