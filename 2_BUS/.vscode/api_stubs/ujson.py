"""
|see_cpython_module| :mod:`python:json`.
This modules allows to convert between Python objects and the JSON
data format.
"""

def dump(obj, stream):
    """
    Serialise *obj* to a JSON string, writing it to the given *stream*.
    
    """
    pass

def dumps(obj):
    """
    Return *obj* represented as a JSON string.
    
    """
    pass

def load(stream):
    """
    Parse the given *stream*, interpreting it as a JSON string and
    deserialising the data to a Python object.  The resulting object is
    returned.
    Parsing continues until end-of-file is encountered.
    A :exc:`ValueError` is raised if the data in *stream* is not correctly formed.
    
    """
    pass

def loads(str):
    """
    Parse the JSON *str* and return an object.  Raises :exc:`ValueError` if the
    string is not correctly formed.
    
    """
    pass

