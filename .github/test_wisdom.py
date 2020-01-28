#!/usr/bin/python

# Copyright (C) 2020 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

from griznog.wisdom import thoughts
import os


def test_wisdom(tmp_path):
    for thought in thoughts:
        assert "date" in thought
        assert "quote" in thought
        assert isinstance(thought["quote"], str)
        assert isinstance(thought["date"], str)
