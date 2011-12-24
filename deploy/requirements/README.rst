========================================
Understanding the PIP Requirements setup
========================================

The requirements directory is housed in the deploy folder and contain a 
collection of text files which specify the project's requirements.

The requirements are structured as follows:

core_reqs.txt
	This is where you put in all the requirements that are necessary
	for the project to run whether in a development or production enviornment.

dev_reqs.txt
	This file will call all the requirements from core_reqs.txt so you would
	only use this with pip initially when testing on your computer.  It may
	have no additional requirements, but often you would put things like the
	Django Debug Toolbar here.

prod_reqs.txt
	This file will call all the requiremnts from core_reqs.txt.  You can put
	in any extra packages in here which the production server will use, for 
	example - if you are developing of SQLite3 but the production uses memcache
	and postresql, you would put the relevant Python libraries for those here
	rather than in core_reqs.txt.
