print_str = "1"
fibonacci_list = [0,1]
iterations = 60
for i in range(iterations):
    item = fibonacci_list[-1]+fibonacci_list[-2]
    print_str+=f" {item}"
    fibonacci_list.append(item)
fibonacci_list = fibonacci_list[1:]
print(print_str)
