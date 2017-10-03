# Command Arguments Parser - v0.4
# by: Dylan Dwyer
# ///////////////////////////////

# !!! - this module is somewhat delicate and expects users to not be idiots

import sys, platform

# adjust mode prefix for system conventions
if 'windows' in str(platform.system()).lower():
    platform_flag = "/"
else:
    platform_flag = "-"

# check for a mode switch - prepends platform_flag automatically
def is_mode(mode):
    return (platform_flag+mode in sys.argv)

# same as above but without platform_flag
def is_string():
    return (mode in sys.argv)

# returns item directly after the given mode
def mode_value(mode, default):
    if platform_flag+mode in sys.argv and\
    sys.argv.index(platform_flag+mode) < (len(sys.argv)-1):
        return sys.argv[sys.argv.index(platform_flag+mode)+1]
    else:
        return default

# returns item at the position asked for
def positional_value(position, default):
    if position < len(sys.argv):
        return sys.argv[position]
    else:
        return default



#//////////////////////////////////////////////////////////////////////////////
