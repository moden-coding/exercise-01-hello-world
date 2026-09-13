#!/usr/bin/env python3
"""Tests for the Hello World assignment."""

import contextlib
import io
import unittest

from src.hello_world import main


class TestMain(unittest.TestCase):
    """main() -> prints the exact greeting to standard output."""

    def _capture(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main()
        return buf.getvalue()

    def test_prints_the_exact_greeting(self):
        output = self._capture().strip()
        self.assertEqual(
            output,
            "Hello, world!",
            msg="main() should print exactly 'Hello, world!' (with the "
            "comma and exclamation point). Got %r." % (output,),
        )

    def test_prints_only_one_line(self):
        output = self._capture()
        lines = output.strip("\n").split("\n")
        self.assertEqual(
            len(lines),
            1,
            msg="main() should print exactly one line. Got %r." % (output,),
        )

    def test_does_not_print_anything_extra(self):
        output = self._capture().strip()
        self.assertNotIn(
            "  ",
            output,
            msg="The greeting should use single spaces only, not extra "
            "spacing. Got %r." % (output,),
        )


if __name__ == "__main__":
    unittest.main()
