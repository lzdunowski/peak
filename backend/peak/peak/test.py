"""
Sample testing
"""

from django.test import SimpleTestCase
from peak import calc


class CalcTests(SimpleTestCase):
    """Test calc module."""
    def testAdd(self):
        check = calc.add(1, 1)
        self.assertEqual(check, 2)
