inp = None

def getinp():
    try: 
        inp = int(input("convertion (1 = normal to boolean,2,3,4,5,)"))
    except ValueError:
        inp = getinp()

    return inp
inp = getinp()

def convert_num_to_bin(num):
    bin = ""
    i = 1
    print(num)
    while i <= num:
        i*=2
    i/=2
    bin += "1"
    num -= i
    if i != num:
        convert_num_to_bin(num)
    print(i, bin+"dd")


        
        
if inp == 1:
    bool_inp = int(input("write num"))
    convert_num_to_bin(bool_inp)
    
    

else:
    print(inp)
