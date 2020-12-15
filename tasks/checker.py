
def what_is_this(a):
    """Returns the type of variable given.
    
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
