Quick Examples of Python
========================


PyQuery
-------


  .. code-block:: python
        
        from pyquery import PyQuery as pq
                doc = pq('a html string')
                print(doc('p').text())


argparse: command-line parsing module
-------------------------------------


  .. code-block:: python
        
        parser = argparse.ArgumentParser()
        parser.add_argument()
        parser.parse_args()            # returns namespace object
        vars(parser.parse_args())      # returns a dictionary


Fabric (used with Pelican)
--------------------------


  .. code-block:: python
        
        fab do-something
        fab do-something: True, False
        fab do-something: kill=True, happy=False

