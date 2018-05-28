#Workouts
import tensorflow as tf
matrix = tf.constant([[1., 2.]])
neg_matrix = tf.negative(matrix)
with tf.Session() as sess:
    result = sess.run(neg_matrix)
print(result)
#------------------------
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b
with tf.Session():
    print(c.eval())

#---------------------------
import tensorflow as tf

x = tf.placeholder("float", None)
y = x * 2

with tf.Session() as session:
    result = session.run(y, feed_dict={x: [1, 2, 3]})
    print(result)
