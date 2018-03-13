import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)
X = tf.placeholder(tf.float32,[None,28,28,1])
Y = tf.placeholder(tf.float32,[None,10])
keep_prob = tf.placeholder(tf.float32)
W1 = tf.Variable(tf.random_normal([3,3,1,32],stddev=0.01))
L1 = tf.nn.conv2d(X,strides=[1,1,1,1],padding='SAME')
L1 = tf.nn.relu(L1)

L1 = tf.nn.max_pool(L1, ksize=[1,2,2,1]), strides=[1,2,2,1], padding='SAME')
