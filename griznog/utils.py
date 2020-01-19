"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

Modified from https://github.com/Visual-mov/Colorful-Julia (MIT License)

"""

from datetime import datetime
import os
import re
import random
import sys

here = os.path.dirname(os.path.abspath(__file__))


def colorize(text):
    """add color to the prompt
    """
    off = "\033[0m"  # end sequence
    colors = {
        "CYAN": "\033[36m",
        "PURPLE": "\033[95m",
        "RED": "\033[91m",
        "DARKRED": "\033[31m",
        "YELLOW": "\033[93m",
    }
    color = random.choice(list(colors.keys()))
    return "%s%s%s" % (colors[color], text, off)
