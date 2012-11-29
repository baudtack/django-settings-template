import os
import sys
from settings_common import *
from {{your_project}}.settings_map import _settings_map

settings_mod = _settings_map[os.uname()[1]]

__import__(settings_mod)
#add the settings from settings_mod to the global namespace
globals().update(sys.modules[settings_mod].__dict__)
