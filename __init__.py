# LaunchPad fix for colour blind users
# ST8 <st8@q3f.org>
# January 2011

import Live
from LaunchpadColour import LaunchpadColour

def create_instance(c_instance):
    return LaunchpadColour(c_instance)
