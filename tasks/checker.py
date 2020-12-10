import sys


def what_is_this(a):
    """Returns the type of variable given.
    
    Working from the terminal $ it will always return str. 
    Please import it in Python with from checker import what_is_this.
    
    given a variable it should, 
    
    if its a function: 
        return "function"
    
    if its a class object:
        return "class":
    else:
        return the type of the varible
    examples:
    
    >> what_is_this(1) -> int
    
    >> def f():
    >>     pass
    >> what_is_this(f) -> "function"
    
    """
    
    return type(a)

def main():
	print(what_is_this(sys.argv[1]))

if __name__ == '__main__':
	main()
