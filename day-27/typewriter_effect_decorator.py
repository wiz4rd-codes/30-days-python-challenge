import time
def typwritter_effect(func):
    def slow_type(*args,**kwargs):
        text = func(*args, **kwargs)
        for ch in text :
            print(ch, end="",flush=True)
            time.sleep(0.17)
        print()
    return slow_type

@typwritter_effect
def string_func(a):
    return a

a = input("Enter a string : ")
string_func(a)
