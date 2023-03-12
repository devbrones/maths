from fmic import fmic

data:str = None
with open('test.txt', 'r') as file:
    data = file.read()
labels:list = ['eggos', 'eggo', 'cool']
tf = fmic(data,labels,0.5)
for x in range(0,100):
    val = x/2000
    print(val)
    tf.threshold = val
    print(tf.find().short)

