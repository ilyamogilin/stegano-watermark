import method
import random

file_length = 10
message_length = 3

arr = []
message = []

for i in range(0, file_length):
    arr.append([random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1)])

for j in range(0, message_length):
    message.append(random.randint(0, 1))

print(message, arr)

f = open('initial.txt', 'w')
f.write(str(arr))
f.close()
f1 = open('changed.txt', 'w')
f1.write(str(method.kdb_method(arr, message)))
f1.close()
