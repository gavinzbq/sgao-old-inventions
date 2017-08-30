"""Cheap and simple API helper

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.

Modified by Shanyun Gao, 06/08/2017
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.3 $"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

# While this is a good example script to teach about introspection,
# in real life it has been superceded by PyDoc, which is part of the
# standard library in Python 2.1 and later.
# 
# Your IDE may already import the "help" function from pydoc
# automatically on startup; if not, do this:
# 
# >>> from pydoc import help
# 
# The help function in this module takes the object itself to get
# help on, but PyDoc can also take a string, like this:
# 
# >>> help("string") # gets help on the string module
# >>> help("apihelper.help") # gets help on the function below
# >>> help() # enters an interactive help mode
# 
# PyDoc can also act as an HTTP server to dynamically produce
# HTML-formatted documentation of any module in your path.
# That's wicked cool.  Read more about PyDoc here:
#   http://www.onlamp.com/pub/a/python/2001/04/18/pydoc.html

def info(object, spacing=23, collapse=1):
    """Print methods and doc strings.

    Takes module, class, list, dictionary, or string."""
    methodList = [e for e in dir(object) if callable(getattr(object, e))]
    constantList = list(set(dir(object)) - set(methodList))
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print 'Callable Attributes'
    print '==================='
    print "\n".join(["%s %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])
    print '\nOther Attributes'
    print '================'
    print "\n".join(["%s" %
                     (method.ljust(spacing))
                     for method in constantList])


if __name__ == "__main__":
    print help.__doc__
