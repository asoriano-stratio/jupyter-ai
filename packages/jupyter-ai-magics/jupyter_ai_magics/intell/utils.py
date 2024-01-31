
def mixedomatic(cls):
    """ Mixed-in class decorator. Allows to execute all __init__ methods in mixed inheritance"""
    classinit = cls.__dict__.get('__init__')  # Possibly None.

    # Define an __init__ function for the class.
    def __init__(self, *args, **kwargs):
        # Call the __init__ functions of all the bases.
        for base in cls.__bases__:
            base.__init__(self, *args, **kwargs)
        # Also call any __init__ function that was in the class.
        if classinit:
            classinit(self, *args, **kwargs)

    # Make the local function the class's __init__.
    setattr(cls, '__init__', __init__)
    return cls
