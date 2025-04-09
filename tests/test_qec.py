import unittest
from autoq.qec import StandardQEC

class TestStandardQEC(unittest.TestCase):
    def test_calculate_overhead(self):
        qec = StandardQEC(p_total=0.005)
<<<<<<< HEAD
        self.assertEqual(qec.overhead, 9.0)
=======
        self.assertEqual(qec.overhead, 9.0)  # p_total < 0.01, overhead = 10 * 0.9
>>>>>>> 405891aba7ee3802a9238c9251a8e62954074de9

    def test_apply_qec(self):
        qec = StandardQEC(p_total=0.011)
        scheduled_gates = 100
        physical_gates = qec.apply_qec(scheduled_gates)
<<<<<<< HEAD
        self.assertEqual(physical_gates, 1800)
=======
        self.assertEqual(physical_gates, 1800)  # overhead = 20 * 0.9 = 18, 100 * 18 = 1800
>>>>>>> 405891aba7ee3802a9238c9251a8e62954074de9

if __name__ == "__main__":
    unittest.main()
