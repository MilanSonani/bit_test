import unittest
from prettytable import PrettyTable
from unified import UnifiedList



class TestUnifiedList(unittest.TestCase):
    def test_compare_lists(self):
        BoM = {"ABC": 2, "XYZ": 1, "IJK": 1, "ABC": 1, "IJK": 1, "XYZ": 2, "DEF": 2}
        Disti = {"XYZ": 2, "GEF": 2, "ABC": 4, "IJK": 2}

        unified_list = UnifiedList(BoM, Disti).compare_lists()
        x = PrettyTable(unified_list[0].keys())

        for row in unified_list:
            x.add_row(row.values())
        print(x)
        return x


if __name__ == '__main__':
    unittest.main()

