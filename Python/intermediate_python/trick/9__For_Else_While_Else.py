# For Else & while else

target = 7
search = [1,2,3,4,5,6,7]


searchlen = int(len(search)+1)

for i in range(searchlen+1):
    if i == target:
        print(f"{i} is the target")
        break

else: # Alltså om inte for loopen breakas så kommer detta köras
    print("I didn't find the target")
    print(f"{target} is not in {search}")

print("\n")

i = 0
while i < len(search):
    target = search[i]
    i+=1

else: # Alltså om inte for loopen breakas så kommer detta köras
    print("I didn't find the target")
    print(f"{target} is not in {search}")