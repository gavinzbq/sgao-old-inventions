Unpacking a sequence into separate variables
--------------------------------------------

Unpacking works with any object that happens to be iterable, which includes
tuples, lists, strings, files, iterators and generators etc.

Example 1
=========

Unpack a string.

.. code-block:: python
    
    >>> s = 'Hello'
    >>> a, b, c, d, e = s 
    >>> a
    'H'
    >>> b
    'e'
    >>> e
    'o'
    >>>


Example 2 
=========

Pick a throwaway variable name (e.g. '-') for values you want to discard.

.. code-block:: python
    
    >>> data = [ 'ACME', 50, 91.1, (2012, 12, 21) ] 
    >>> _, shares, price, _ = data
    >>> shares
    50
    >>> price 91.1


Example 3 
=========

When you want to unpack N elements from an iterable, but the iterable is longer
than N. Use "star expressions".

.. code-block:: python
    
    >>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    >>> name, email, *phone_numbers = user_record
    >>> name
    'Dave'
    >>> email
    'dave@example.com'
    >>> phone_numbers 
    ['773-555-1212', '847-555-1212']
    
Note that `phone_numbers` will always be a list, regardless of how many phone
numbers are unpacked (including none).
