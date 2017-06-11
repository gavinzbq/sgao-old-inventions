Useful Python Tricks
====================

*Learning notes on python useful idioms*

* Range Check

  .. code-block:: python
        
        if not (0 < n < 100):

* Non-Integer Check

  .. code-block:: python
        
        if int(n) <> n:


* Pads A String to A Given Length (integer)

  .. code-block:: python
        
        >>> s = 'hello'
        >>> s.ljust(30)
        'hello                         '
        >>>

* Printing A List

  .. code-block:: python

        >>> li = ['a', 'b', 'c']
        >>> print '\n'.join(li)
        a
        b
        c
        >>> 
