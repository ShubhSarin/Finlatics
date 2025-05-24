nums = []
for i in range(10):
    nums.append(int(input()))
for num in nums:
    if num % 2 == 0:
        print(num ** 2)
    else: 
        print(num ** 3)