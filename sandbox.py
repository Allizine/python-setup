print('Hello from inside a file c:')


pack_list = ["Apple", "Water", "Phone"]

def say_hello():
    print("Hello!")

def pack(a,b,c):
    return a,b,c

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My Lunchbox is empty :c")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else: 
                print(f"next I eat{my_list[i]}")
            
        
say_hello()
pack("a","b","c")
eat_lunch([])
