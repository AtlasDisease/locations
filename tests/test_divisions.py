# --- Imports --- #

import unittest as utest
from ..divisions import Division


# --- DivisionsTestCase Class --- #

class DivisionsTestCase(utest.TestCase):
    def setUp(self):
        self.division = Division("MyDiv", [])

    def test_rename_div(self):
        result_div = Division("Austin", [])
        self.assertEqual(self.division.rename("Austin"),
                         result_div,
                         "name is not correct")
