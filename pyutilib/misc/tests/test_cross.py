#
# Unit Tests for util/math
#
#

from os.path import abspath, dirname
pkgdir = f"{dirname(abspath(__file__))}/../.."

import pyutilib.th as unittest
import pyutilib.misc


class CrossDebug(unittest.TestCase):

    def setUp(self):
        self.tmp = [(10, 22, 31), (10, 22, 32), (10, 22, 33), (10, 23, 31),
                    (10, 23, 32), (10, 23, 33), (11, 22, 31), (11, 22, 32),
                    (11, 22, 33), (11, 23, 31), (11, 23, 32), (11, 23, 33)]
        self.tmp.sort()

        self.ttmp = [(10, 22, 31), (10, 23, 32), (11, 22, 31), (11, 23, 32)]
        self.ttmp.sort()

    def test_cross1(self):
        # Apply the cross() method
        ans = pyutilib.misc.cross(((10, 11), (22, 23), (31, 32, 33)))
        ans.sort()
        self.assertEqual(ans, self.tmp)

    def test_cross2(self):
        ans = sorted(pyutilib.misc.cross_iter((10, 11), (22, 23), (31, 32, 33)))
        self.assertEqual(ans, self.tmp)

    def test_cross3(self):
        ans = sorted(
            pyutilib.misc.flattened_cross_iter((10, 11), ((22, 31), (23, 32)))
        )
        self.assertEqual(ans, self.ttmp)


if __name__ == "__main__":
    unittest.main()
