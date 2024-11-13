x=int(input("Enter size of list: "))
num_list=[]
print("Enter numbers in list: ")
while(x!=0):
    k=int(input())
    num_list.append(k)
    x=x-1
print(num_list)
mean = sum(num_list) / len(num_list)
sorted_list = sorted(num_list)
if x % 2 == 1:
    median = sorted_list[x // 2]
else:
    median = (sorted_list[x // 2 - 1] + sorted_list[x// 2]) / 2
frequency = {}
for num in num_list:
    frequency[num] = frequency.get(num, 0) + 1
max_count = max(frequency.values())
mode = [num for num, count in frequency.items() if count == max_count]
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")