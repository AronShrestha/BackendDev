 # function design pattern
def my_decoratr(func):
    print("Inside the decorator function ")

    def wrapper(*args,  **kwargs):
        print("Called the wrapper")
        print("Decorating with the parameters")
        print("Args are :", args)
        print("Kwargs are :", kwargs)
        result = func(*args, **kwargs)
        print("Completed the task")

        return result
    return wrapper



@my_decoratr
def caller(*args, **kwargs):
    print("after necessary beginner decoration I am called")


class CountCalls:
    def __init__(self, func) -> None:
        print("Initilizing the Count call decorators")
        self.func = func 
    

    def __call__(self, *args, **kwargs):
        print(" now we are calling the ")
        self.func()
        print("Completed")



@CountCalls
def caller2(*args, **kwargs):
    print("after necessary beginner decoration I am 2 called")


def main():
    caller("a","b",5,caller_name='Ibhonik')
    caller2("a","b",5,caller_name='Ibhonik')



if __name__ == "__main__":
    main()



