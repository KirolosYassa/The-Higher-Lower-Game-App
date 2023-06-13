
def make_italic(func):

    def wrapper_func():
        result = "<i>" + func() + "</i>"
        return result
    
    return wrapper_func

def make_underlined(func):

    def wrapper_func():
        result = "<u>" + func() + "</u>"
        return result
    
    return wrapper_func

def make_bold(func):

    def wrapper_func():
        result = "<b>" + func() + "</b>"
        return result
    
    return wrapper_func
