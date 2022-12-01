import os

data ='dos:ping 8.8.8.8'
data1 = data.split(':')[1]
print((f'dos:{data1}'))
