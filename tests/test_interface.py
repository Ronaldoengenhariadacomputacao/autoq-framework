import unittest
from qiskit import QuantumCircuit
from autoq.interface import QiskitInterface

class TestQiskitInterface(unittest.TestCase):
    def test_get_gate_count(self):
        circuit = QuantumCircuit(14)
        for i in range(400):
            circuit.h(i % 14)
        interface = QiskitInterface(circuit)
        gate_count = interface.get_gate_count()
        self.assertEqual(gate_count, 400)

if __name__ == "__main__":
    unittest.main()
