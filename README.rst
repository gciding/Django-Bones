Getting Started
===============

This project contains a Django Project template layout setup to be deployed
with it's parenting project folder (the folder you would add to GitHub as the
project name).  Therefore the actual Django component within the project falls
one subdirectory down.

The way you use the project is with Django 1.4+ (you will already need Django
1.4 installed)::
	
	django-admin.py start_project your_new_project --template=https://github.com/goranstef/Django-Bones/zipball/master

This will create a project with the name 'your_new_project'.  You should note
the Folder Layout information below before beginning.

After you have created the project, you may wish to rename the parent directory 
to something to signify that it is the project parent directory.  It actually 
doesn't matter what the name of this directory is because it doesn't get used 
anywhere in the project.  All Project files are relative within this directory.


Finally, you probably want to add it to GitHub, so from the directory where you 
ran the `django-admin` command::

	cd 'your_new_project'
	git init
	git add *
	git commit -m 'Initial Commit of my new project :)'
	git remote add origin git@github.com:(your project repo...)
	git push -u origin master

You can now edit your settings file, start adding apps etc and work on your 
project!

Folder Layout
-------------

When you run the `start_project` command, a folder with your project name is 
created.  Let's assume your new project was called `bonesy`.   The `bonesy` 
folder which was created is actually the parent folder which will hold your 
entire Django project (including the setup files, doc directory etc).

I would often rename this folder to match the name I gave my GitHub (or 
Bitbucket etc) repostiory.  I would then CD into this folder and work from this 
destination for all other items. Each of the folders are explained below:

So, we're under the `bonesy` parent folder, we now have the files we're 
interested in::

	+  bonsey/ - the Django project parent directory.
	.  .
	.  +  bonsey/ - the Django project app corresponding to the project.
	.  .  .
	.  .  +  settings/ - This folder houses our various settings files.
	.  .  .  .		
	.  .  .  *  __init__.py -- Does the importing so we can use import settings
	.  .  .  .
	.  .  .  *  base.py -- Pretty much the settings file django produces with some extras.
	.  .  .  .
	.  .  .  *  settings_locahost_template.py -- a 'local settings' for the host
	.  .  .  .
	.  .  .  *  utils.py - some helpers used within the settings files.
	.  .  .
	.  .  *  urls.py - Django's generated URls conf for the project
	.  .  .
	.  .  *  wsgi.py	- Used by django's runserver.  .
	.   .
	.   +  public_media/ - This is where our user generated media goes.
	.  .  
	.  +  static/ - This is where we put our js/css and image files.	
	.  .
	.  +  templates/ - This is where we store our project level templates
	.  .
	.  *  manage.py - the management file created by Django.
	.
	+  deploy/ - houses our requirements files, and any specific deployment files
	.  .
	.  +  requirements/ - the Django project app corresponding to the project.
	.  .  .
	.  .  *  core_reqs.txt - put your webapps core python requirements in here.
	.  .  .
	.  .  *  dev_reqs.txt - loads core_reqs, but also specify dev only stuff
	.  .  .
	.  .  *  prod_reqs.txt - speficy your production server libs here
	.   
	+  docs/ -- where you put the project docs, generate these with Sphinx maybe?
	.  
	*  README.rst -- this file!


Understanding the Settings layout
---------------------------------

The project uses a special layout for settings in order to maintain the 
``DJANGO_SETTINGS_VARIABLE=myproject.settings`` defaults set by Django (i.e. 
so you don't need to pass your custom settings filename each time) but also
allow for advanced settings customisation.

Essentially, the project requires a settings file which has been named for 
the host which you are running the program on.  For example, if your host name 
is 'web20.hoster.com' then your local settings file will be named
``settings_web20_hoster_com.py`` (the '.' are replaced with '_').

There is also a settings file named ``local_core.py`` - this file is responisble
for defining local settings which some of the settings in ``base.py`` may rely
on.  Typically, this file (which is optional) will set the root directory for
where static files will be collated and where media files are located.  It may
also specify the ``MEDIA_URL`` and ``STATIC_URL`` and ``DEBUG=True``.

The reason that this file is required, is that where there are settings in 
``base.py`` which extend one of the variables in this file (such as 
``TEMPLATE_DEBUG` = `DEBUG``) then the typical overwrite method of importing
a local settings file at the end of the base settings file causes inconsistencies.

The way it works is:

#. ``settings/__init__.py`` is loaded when the module ``myproject.settings`` is imported.

#. This file will seach for a host settings file and import all of it's items.

#. The hosts settings file is responsible for importing the base settings so that it may extend the base settings where necessary.

#. The base settings file actually tries to import a ``local_core`` file itself. This gives the developer an opportunity to overwrite some of the core variables in the settings file.

  
Next Steps
==========

* Incorporate AUTHOR, settings.py, LICENCE etc into the top level of the project
* Incorporate some Fabfiles with basic methods in them