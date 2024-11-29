'''TASK 1'''
def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("All lists must be of equal length for strict zipping.")
    else:
        min_len = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_len)]

customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [102, 101, 103]
shopping_points = [500, 400, 600]

try:
    zipped_data_strict = my_zip(customer_names, customer_ids, shopping_points, strct=True)
    print("Strict zipped data:", zipped_data_strict)
except ValueError as e:
    print(e)
    
zipped_data_non_strict = my_zip(customer_names, customer_ids, shopping_points, strct=False)
print("Non-strict zipped data:", zipped_data_non_strict)


'''TASK 2'''
def my_sort(data, key=0):
    n = len(data)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    
    return data

customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [102, 101, 103]
shopping_points = [500, 400, 600]

zipped_data = my_zip(customer_names, customer_ids, shopping_points, strct=True)

sorted_by_name = my_sort(zipped_data, key=0)
print("Sorted by customer name:", sorted_by_name)

sorted_by_id = my_sort(zipped_data, key=1)
print("Sorted by customer ID:", sorted_by_id)

sorted_by_points = my_sort(zipped_data, key=2)
print("Sorted by shopping points:", sorted_by_points)


'''TASK 3'''
def my_max(*container):
    if len(container) == 0:
        raise ValueError("The container is empty.")
    
    max_value = container[0]

    for value in container:
        if value > max_value:
            max_value = value
    
    return max_value

my_list = [1, 4, 9, 7, 2]
my_set = {11, 22, 5, 8}
my_tuple = (3, 6, 2, 8, 1)

print("Maximum in list:", my_max(*my_list))

print("Maximum in set:", my_max(*my_set))

print("Maximum in tuple:", my_max(*my_tuple))