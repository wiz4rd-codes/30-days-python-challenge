import time
def timer(func):
    def calc_time(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function executed in {end - start} sec")
    return calc_time    



@timer
def prime_finder(a,b):
    for i in range(a,b+1):
        prime = 1
        if(i in [0,1,2]):
            print(f"{i} is not a prime number") if(i in [0,1]) else print(f"{i} is a prime number")
            continue
     
        else :     
            for c in range(2,i):
                if i%c == 0:
                    prime = 0
                    break
               
           
        print(f"{i} is a prime number") if(prime==1) else (print(f"{i} is not a prime number"))

prime_finder(0,1000)
