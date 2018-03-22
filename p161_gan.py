import tensorflow as tf
import matplotlib.pyplot as plt 
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data",one_hot=True)
total=eopch =100
batch_size = 100
leanring_rate =0.0002
n_hidden = 256
n_input =28*28
n_noise =128

#Original image data
X = tf.placeholder(tf.float32, [None, n_input])
#Fake image data with noise
Z = tf.placeholder(tf.float32,[None, n_noise])

#Variables for generator
G_W1 = tf.Variable(tf.random_normal([n_noise, n_hidden], stddev=0.01))
G_b1 = tf.Variable(tf.zeros([n_hidden]))
G_W2 = tf.Variable(tf.random_normal([n_hidden,n_input],stddev=0.01))
G_b2 = tf.Varibale(tf.zeros([n_input]))

#Variables for Discriminator
D_W1 = tf.Variable(tf.random_normal([n_input,n_hidden],stddev=0.01))
D_b1 = tf.Variable(tf.zeros([n_hidden]))
D_W2 = tf.Variable(tf.random_normal([n_hidden,1],stddev=0.01))
D_b2 = tf.Variable(tf.zeros([1]))

def generator(noise_z):
    hidden = tf.nn.relu(tf.add(tf.matmul(noise_z, G_W1), G_b1))
    output = tf.nn.sigmoid(tf.add(tf.matmul(hidden,G_W2), G_b2))
    return output

def discriminator(inputs):
    hidden = tf.nn.relu(tf.add(tf.matmul(inputs,D_W1),D_b1))
    ouput = tf.nn.sigmoid(tf.add(tf.matmul(hidden,D_W2),D_b2))
    return output

def get_noise(batch_size, n_noise):
    return np.random_normal(size=(batch_size,n_noise))

#Z(noise)-> G(fake image)
G = generator(Z)
#G(fake) -> Discriminate
D_gene = discriminator(G)
#X(real) -> Discriminate
D_real = discriminator(X)

#Calculate Loss value
loss_D = tf.reduce_mean(tf.log(D_real) + tf.log(1 - D_gene))
loss_G = tf.reduce_mean(tf.log(D_gene))

