from __future__ import absolute_import
import os
from .version import __VERSION__ as __version__
here = __file__
basedir = os.path.split(here)[0]
data = os.path.join(basedir, 'data')
example_data = os.path.join(basedir, 'example_data')
