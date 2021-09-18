# what is type class


# difference between
# __init__ => Called after the instance has been created by (__new__()) but before it is returned to the caller
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Gets called when instance is called as a function
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# usage
# class Logger(object):
#     __metaclass__ = Singleton

# type(Logger)
# <class 'type'>
# type(Logger())
# <class '__main__.Logger'>

#  metaclass is the class of a class; that is, a class is an instance of its metaclass.
#  You find the metaclass of an object in Python with type(obj).
#  Normal new-style classes are of type type. Logger in the code above will be of type class 'your_module.Singleton',
#  just as the (only) instance of Logger will be of type class 'your_module.Logger'.
#  When you call logger with Logger(), Python first asks the metaclass of Logger, Singleton, what to do, allowing instance creation to be pre-empted.
#  This process is the same as Python asking a class what to do by calling __getattr__ when you reference one of it's attributes by doing myclass.attribute.
#
# A metaclass essentially decides what the definition of a class means and how to implement that definition.

