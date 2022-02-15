import tensorflow as tf

# 请观察打印出的shape

x1 = tf.constant([[5.8, 4.0, 1.2, 0.2]])
w1 = tf.random.truncated_normal([4, 3])
b1 = tf.random.truncated_normal([1, 3])
y = tf.matmul(x1, w1) + b1
print("x1.shape:", x1.shape)
print("w1.shape:", w1.shape)
print("b1.shape:", b1.shape)
print("y.shape:", y.shape)
print("y:", y)

y_dim = tf.squeeze(y)  # 去掉y中纬度1（观察y_dim与 y 效果对比）
y_pro = tf.nn.softmax(y_dim)  # 使y_dim符合概率分布，输出为概率值了
print("y_dim:", y_dim)
print("y_pro:", y_pro)
