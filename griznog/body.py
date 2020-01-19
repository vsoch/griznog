"""

Copyright (C) 2019-2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from griznog.wisdom import thoughts
from griznog.utils import colorize
import random
import re
import sys
import time


class Griznog(object):
    """A Griznog is a packet of human meat (primarily carbon based, multi-cellular)
       that comes with infinite wisdom and a huge desire for pizza and the occasional
       donut. Allergies include too many other humans, useless organizational
       powers, and leaf blowers.
    """

    def __init__(self):
        self.quotes = thoughts

    def __str__(self):
        return "[griznog]"

    def __repr__(self):
        return self.__str__()

    def _speak(self, thought, add_color=True):
        """Speak a random thought, or one selected from a subset.
        """
        quote = thought["quote"]
        if add_color:
            quote = colorize(quote)
        print("%s\n--Griznog %s" % (quote, thought["date"]))

    def dump(self, topic=None, pause=3, add_color=True):
        """dump all knowledge, optionally filtered to a topic.
        """
        thoughts = self.quotes
        if topic is not None:
            thoughts = self.filter_thoughts(thoughts, topic)

        # Always randomize
        random.shuffle(thoughts)

        for thought in thoughts:
            self._speak(thought=thought, add_color=add_color)
            print("\n\n")
            time.sleep(pause)

    def filter_thoughts(self, thoughts, query):
        """filter a set of thoughts down based on a query string. We make
           the query and the quotes lowercase to support any casing
        """
        thoughts = [t for t in thoughts if re.search(query.lower(), t["quote"].lower())]

        if not thoughts:
            print("Griznog doesn't have anything to say about %s." % query)
            sys.exit(0)
        return thoughts

    def speak(self, topic=None, add_color=True):
        """Ask Griznog to speak his wisdom
        """
        thoughts = self.quotes
        if topic is not None:
            thoughts = self.filter_thoughts(thoughts, topic)

        thought = random.choice(thoughts)
        self._speak(thought=thought, add_color=add_color)
