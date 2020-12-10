import sys


def what_is_this(a):
    """Returns the type of variable given.
    
    Working from the terminal $ it will always return str. 
    Please import it in Python with from checker import what_is_this."""
    
    return type(a)

def main():
	print(what_is_this(sys.argv[1]))

if __name__ == '__main__':
	main()
