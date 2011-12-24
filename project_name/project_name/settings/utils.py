#
# Utility methods for settings files that any settings file can import
#
import os

PROJ_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
def project_dir(*args):
    return os.path.abspath(os.path.join(PROJ_ROOT, *args))