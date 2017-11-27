import method
import random

file_width = 2
file_height = 2
message_length = 3

arr = []
message = []

for x in range(0, file_height):
    arr.append([])
    for y in range(0, file_width):
        arr[x].append([random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1)])

for j in range(0, message_length):
    message.append(random.randint(0, 1))

print(arr[0][0])
print(arr)

f = open('initial.txt', 'w')
f.write(str(arr))
f.close()
f1 = open('changed.txt', 'w')
f1.write(str(method.kdb_method(arr, message)))
f1.close()
