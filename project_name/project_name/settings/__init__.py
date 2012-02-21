#
# Import the settings file for the named host
# You should specify a file like settings_[your hostname].py which imports
# the relevant settings files for you.
#
import socket

host_name = socket.gethostname() or 'default'
HOSTNAME = host_name.replace('.','_')

try:
    # See http://docs.python.org/library/functions.html#__import__
    m = __import__(name="settings_%s" % HOSTNAME, 
                    globals=globals(), locals=locals(), fromlist="*")
    try:
        attrlist = m.__all__
    except AttributeError:
        attrlist = dir(m)
    for attr in [a for a in attrlist if '__' not in a]:
        globals()[attr] = getattr(m, attr)

except ImportError, e:
    import sys
    sys.stderr.write('Unable to read settings_%s.py  -- You should create this file.\n' % HOSTNAME)
    sys.exit(1)
