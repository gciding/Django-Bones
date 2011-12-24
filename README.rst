Getting Started
===============

This project contains a Django Project template layout setup to be deployed with it's parenting
project folder (the folder you would add to GitHub as the project name).  Therefore the actual Django component within the project falls one subdirectory down.

The way you use the project is with Django 1.4+ (you will already need Django 1.4 installed)::
	
	django-admin.py start_project your_new_project --template=https://github.com/goranstef/Django-Bones/zipball/master

This will create a project with the name 'your_new_project'.  You should note the Folder Layout information below before beginning.

After you have created the project, you may wish to rename the parent directory to something to signify that it is the project parent directory.  It actually doesn't matter what the name of this directory is because it doesn't get used anywhere in the project.  All Project files are relative within this directory.

Finally, you probably want to add it to GitHub, so from the directory where you ran the `django-admin` command::

	cd 'your_new_project'
	git init
	git add *
	git commit -m 'Initial Commit of my new project :)'
	git remote add origin git@github.com:(your project repo...)
	git push -u origin master

THat's all, you can edit your settings file, start adding apps etc and work on your project!

Folder Layout
*************



