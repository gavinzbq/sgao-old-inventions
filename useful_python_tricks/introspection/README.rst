Python Tricks -- Introspection
-----------------------------

**Introspection** is code looking at other modules and functions in memory as
objects, getting information about them and manipulating them [*]_. The list
below are functions I found useful when debugging code.

* The `type` Function

    .. code-block:: python
        
        >>> type(1)
        <type 'int'>
        >>>
        >>> li = []
        >>> type(li)
        <type 'list'>
        >>>
        >>> di = {}
        >>> type(di)
        <type 'dict'>
        >>>
        >>> type(type)
        <type 'type'>

    `type` function takes anything and returns its datatype -- integers, strings, lists, dictionaries, classes, functions, modules.

* The `dir` Function

    .. code-block:: python
        
        >>> li = []
        >>> dir(li)
        ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
        ...         
        'pop', 'remove', 'reverse', 'sort']
  
  Note that `dir(li)` returns a list of all the methods of a list. The returned list
  contains the names of the methods as strings, not the methods themselves.


    .. code-block:: python
        
        >>> import types
        >>> dir(types)
        ['BooleanType', 'BufferType', 'BuiltinFunctionType',
        ...
        '__all__', '__builtins__', '__doc__', '__file__', '__name__',
        '__package__']

  `types` is a module, `dir(types)` returns a list including built-in
  attributes like `__all__`, and user-defined methods such as
  `BooleanType`.


* The `callable` Function

    .. code-block:: python
        
        >>> import types
        >>> callable(types.BooleanType)
        True
        >>> callable(types.__name__)
        False
        >>> types.BooleanType(1)
        True
        >>> types.BooleanType('a')
        True
        >>> types.BooleanType(0)
        False
        >>> types.BooleanType(None)
        False
        >>> types.BooleanType()
        False

  The `callable` function takes any object and returns `True` if the object
  can be called, or `False` otherwise. Callable objects includes functions,
  class methods and class themselves. Therefore, `types.BooleanType()`
  returns `False` if the input is empty, zero or `None`, and returns
  `True` otherwise.

  By using the `callable` function on object's attributes, we can determine
  the ones we care about (e.g. methods, functions, classes) and which we want
  to ignore (e.g constants) without knowing anything about the object
  beforehand.

* The `getattr` Function

    .. code-block:: python
        
        >>> li = ['a', 'b', 'c']
        >>> li.pop
        <built-in method pop of list object at 0x10fde9170>
        >>> getattr(li, 'pop')
        <built-in method pop of list object at 0x10fde9170>

  We can get a reference to a function by using the `getattr` function. Note
  that `li.pop` is not calling the `pop` method, while `li.pop()` is.
  When using `getattr`, the method name (`pop`) is specified as as tring
  argument.

    .. code-block:: python
        
        >>> getattr(li, 'append')('o')
        >>> li
        ['a', 'b', 'c', 'o']

  Since the return value of `getattr` is the method, we can then call just as
  if we did `li.append('o')`. In fact, however, we did not call the function
  directly, instead we specified the function name as a string. Incredible
  isn't it.

    .. code-block:: python
        
        >>> print getattr(li, 'append').__doc__
        L.append(object) -- append object to end

  Amazingly, the above code printed the `doc string` associated with list's
  attribute `append`.

* The `apihelper.py` program

  Use `apihelper.py` like:

    .. code-block:: python
        
        >>> from apihelper import info
        >>> li = []
        >>> info(li)
        Callable Attributes
        ===================
        __add__                 x.__add__(y) <==> x+y
        __class__               list() -> new empty list list(iterable) -> new list initialized from iterable's items
        ...

        Other Attributes
        ================
        __hash__               
        __doc__ 

  
  The `info` function is designed for programmers. Cheers.

.. [*] Pilgrim, M., 2009. *Dive Into Python*. Createspace. 
