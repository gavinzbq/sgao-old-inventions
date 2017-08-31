Vim Editor
==========

* Find every occurance and substitute.


  .. code-block:: python
        
        :%s/old/new/gc


* Buffers

  To list all buffers.

  .. code-block:: python
        
        :ls

* Fold and unfold


  .. code-block:: python
        
        za


* To open file below / to the right to the current file


  .. code-block:: python
        
        :sp <filename>
        :vs <filename>


**Note**: Other Vim add-ons include *Powerline*, *CtrlP*, *NerdTREE*, *YouCompleteMe*. 
They remain exploring.


virtualenvwrapper
=================


* Remove an <env>


  .. code-block:: python
        
        $ rmvirtualenv ENVNAME


* Change the current working directory to $VIRTUAL_ENV


  .. code-block:: python
        
        $ cdvirtualenv


* Remove all the third party packages in the current directory


  .. code-block:: python
        
        $ wipeenv
