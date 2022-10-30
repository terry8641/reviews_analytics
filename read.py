data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0: #每1000筆才印一次，以加速程式
			print(len(data))
print(len(data))

print(data[0])
print('-------------------')
print(data[1])