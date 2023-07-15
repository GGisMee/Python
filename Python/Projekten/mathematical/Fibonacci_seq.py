print_str = "1"
fibonacci_list = [0,1]
iterations = 10
for i in range(iterations):
    print_str+=f" {fibonacci_list[-1]+fibonacci_list[-2]}"
    fibonacci_list.append(fibonacci_list[-1]+fibonacci_list[-2])
fibonacci_list[1:]
print(print_str)