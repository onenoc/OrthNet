import sys
sys.path.append('../')
from orthnet import Laguerre
import tensorflow as tf
import torch
from torch.autograd import Variable
import numpy as np


x_data = np.random.random((3, 2))
x_tf = tf.placeholder(dtype = tf.float32, shape = (None, 2))
x_torch = Variable(torch.Tensor(x_data))

y_tf = Laguerre('tensorflow', 2, x_tf)
y_torch = Laguerre('pytorch', 2, x_torch)

with tf.Session() as sess:
	z_tf = sess.run(y_tf.tensor, feed_dict = {x_tf:x_data})
z_torch = y_torch.tensor.data.numpy()

print('length:', y_tf.length)
print('combination:', y_tf.combination)
print('index:', y_tf.index)
print('tf values:')
print(z_tf)
print('torch values:')
print(z_torch)
print('equal?')
print(np.allclose(z_tf, z_torch))
print('\n')

y_tf.update(4)
y_torch.update(4)

with tf.Session() as sess:
	z_tf = sess.run(y_tf.tensor, feed_dict = {x_tf:x_data})
z_torch = y_torch.tensor.data.numpy()

print('updated:')
print('length:', y_tf.length)
print('combination:', y_tf.combination)
print('index:', y_tf.index)
print('tf values:')
print(z_tf)
print('torch values:')
print(z_torch)
print('equal?')
print(np.allclose(z_tf, z_torch))
