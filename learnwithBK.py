import mph
import numpy as np

client = mph.start()
model = client.load('learnwithBK.mph')

print(client.names())
print(model.parameters())

newvoltage = 2

