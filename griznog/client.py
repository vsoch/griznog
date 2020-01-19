#!/usr/bin/env python

"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

import griznog
import argparse
from glob import glob
import sys
import os
import re
import tempfile


def get_parser():
    parser = argparse.ArgumentParser(description="Griznog, captured in code")
    parser.add_argument(
        "--version",
        dest="version",
        help="print the version and exit.",
        default=False,
        action="store_true",
    )

    subparsers = parser.add_subparsers(
        help="griznog actions",
        title="actions",
        description="actions for Griznog",
        dest="command",
    )

    speak = subparsers.add_parser("speak", help="ask Griznog to speak his wisdom.")

    speak.add_argument(
        "--topic",
        dest="topic",
        help="subset to particular topic.",
        type=str,
        default=None,
    )

    speak.add_argument(
        "--pause",
        dest="pause",
        help="seconds to allow Griznog to breathe between spurts (default 3 seconds).",
        type=int,
        default=3,
    )

    speak.add_argument(
        "--dump",
        dest="dump",
        help="Just hear everything. Optionally set a --pause (seconds)",
        default=False,
        action="store_true",
    )

    speak.add_argument(
        "--no-color",
        dest="nocolor",
        help="disable color",
        default=False,
        action="store_true",
    )

    return parser


def main():
    """main is the entrypoint to griznog. Get your head out of the gutter.
    """

    parser = get_parser()

    # Will exit with subcommand help if doesn't parse
    args, extra = parser.parse_known_args()

    # Show the version and exit
    if args.version:
        print(griznog.__version__)
        sys.exit(0)

    # Initialize the JuliaSet
    if args.command == "speak":

        from griznog import Griznog

        human = Griznog()

        # Case 1: dump all the wisdom, optionally limited to a topic/date
        if args.dump:
            human.dump(topic=args.topic, pause=args.pause, add_color=not args.nocolor)

        # Case 2: Randomly speak, optionally filter to topic/date
        else:
            human.speak(topic=args.topic, add_color=not args.nocolor)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
