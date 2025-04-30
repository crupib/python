import sys
import unittest
import better_exceptions


def patch(self, err, test):
    lines = better_exceptions.format_exception(*err)
    if sys.version_info[0] == 2:
        return "".join(lines).encode("utf-8")
    return "".join(lines)


unittest.result.TestResult._exc_info_to_string = patch
