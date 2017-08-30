Initialize Git Repo and Commit
------------------------------

  .. code-block:: python
        
        $ git init .
        $ touch .gitignore

For example, write `__pycache__` and `*.py[cod]` to `.gitignore` file.

Then add files and check the files added into the staging area.


  .. code-block:: python

        $ git add .
        $ git status


Remove files that you don't want to commit.


  .. code-block:: python
        
        $ git rm --cached path_of_file


To see the commit made.


  .. code-block:: python
        
        $ git commit -m "first commit"
        $ git log


To create a new empty repository
--------------------------------

  .. code-block:: python
        
        $ git remote add origin https:
        $ git push -u origin master

"-u" means to set upstream.

  .. code-block:: python
        
        $ git branch -a

To see active branches.



