import tensorflow as tf

a = tf.fill([1, 2], 3.)
print("a: ", a)
print("a ^ 3: ", tf.pow(a, 3))
print("a ^ 2: ", tf.square(a))
print("a ^ 1/2: ", tf.sqrt(a))