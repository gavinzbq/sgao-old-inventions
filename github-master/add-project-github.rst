Adding an existing project to Github using the command line
===========================================================

1. Create a new repository on Github
------------------------------------

.. note:: To avoid errors, do not initialize with *README*, license, or "gitignore" files.

2. Open Terminal
----------------

3. Change the current directory to your local project
-----------------------------------------------------

4. Initialize the local directory as Git repository
---------------------------------------------------

  .. code-block:: python

        echo "# repo-name" >> README.md
        $ git init

5. Add the files in your new local repository. This stages them for the first commit.
-------------------------------------------------------------------------------------

  .. code-block:: python

        $ git add README.md
        # Add the files in the local repo and stages them for commit. 
        # To unstage a file, use 'git reset HEAD *YOUR-FILE*'

6. Commit the files that you've staged in your local repository
---------------------------------------------------------------

  .. code-block:: python

        $ git commit -m "First Commit"
        # Commits the tracked changes and prepares them to be pushed to a remote
        # repo. 
        # To remove this commit and modify teh file, use 'git reset --soft HEAD~1'
        # and commit and add the file again.

7. Copy the remote repository URL
---------------------------------

8. In Terminal, add the URL for the remote repo where your local repo will be pushed
------------------------------------------------------------------------------------

  .. code-block:: python

        $ git remote add origin *remote repository URL*
        # Sets the new remote
        $ git remote -v
        # Verifies the new remote URL

9. Push the changes in your local repo to Github
------------------------------------------------

  .. code-block:: python

        $ git push -u origin master
        # Pushed the changes in your local repo up to the remote rpo you specified as 
        # the origin
