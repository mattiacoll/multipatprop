import unittest
from multipatprop.multipatprop import System, Transmitter, Receiver, Interferer, Point
from random import seed, random, randint

seed(45)

class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.transmitter = Transmitter(Point(-2, -2.5))
        self.receiver = Receiver(Point(2, 2))
        self.interferers = [Interferer.square(Point(0, 0), 9, 0)]
        self.system = System(self.transmitter, self.receiver, self.interferers)


    def test_path_length(self):
        multipath = self.system.get_multipath(starting_number=1000, receiver_diameter=0.2, max_reflections=40, power_multiplier=0.9)
        self.assertEqual(len(multipath.paths), 497)


if __name__ == '__main__':
    unittest.main()