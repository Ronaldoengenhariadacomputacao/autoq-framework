import unittest
from qiskit import QuantumCircuit
from autoq.scheduler import ParallelScheduler

class TestParallelScheduler(unittest.TestCase):
    def test_schedule(self):
        circuit = QuantumCircuit(14)
        for i in range(400):
            circuit.h(i % 14)
        scheduler = ParallelScheduler(parallel_factor=2.0)
        scheduled_gates = scheduler.schedule(circuit)
        self.assertEqual(scheduled_gates, 200)

if __name__ == "__main__":
    unittest.main()