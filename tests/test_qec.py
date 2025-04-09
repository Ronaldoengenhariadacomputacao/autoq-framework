import unittest
from autoq.qec import StandardQEC

class TestStandardQEC(unittest.TestCase):
    def test_calculate_overhead(self):
        qec = StandardQEC(p_total=0.005)
        self.assertEqual(qec.overhead, 9.0)  # p_total < 0.01, overhead = 10 * 0.9

    def test_apply_qec(self):
        qec = StandardQEC(p_total=0.011)
        scheduled_gates = 100
        physical_gates = qec.apply_qec(scheduled_gates)
        self.assertEqual(physical_gates, 1800)  # overhead = 20 * 0.9 = 18, 100 * 18 = 1800

if __name__ == "__main__":
    unittest.main()
