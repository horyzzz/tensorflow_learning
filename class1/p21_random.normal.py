import tensorflow as tf

d = tf.random.normal([2, 2], mean=0.5, stddev=1)
print("d:", d)
e = tf.random.truncated_normal([2, 2], mean=0.5, stddev=1)
print("e:", e)

d = tf.random.normal([2, 2], mean=0.5, stddev=1)
print("d:", d)
# 2xigma之间   截断的正态分布
e = tf.random.truncated_normal([2, 2], mean=0.5, stddev=1)
print("e:", e)