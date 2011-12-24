#
# -- Local Core Settings --
# These settings need to be specified before the base
# settings is computed because the base settings rely
# on these settings to setup other settings.
#
from .utils import PROJ_ROOT, project_dir

DEBUG = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
