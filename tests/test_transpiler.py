import unittest
from qiskit import QuantumCircuit
from autoq.transpiler import CircuitTranspiler

class TestCircuitTranspiler(unittest.TestCase):
    def test_transpile(self):
        circuit = QuantumCircuit(14)
        for i in range(400):
            circuit.h(i % 14)
        transpiler = CircuitTranspiler(optimization_level=3)
        optimized_circuit = transpiler.transpile(circuit)
        self.assertLess(len(optimized_circuit.data), 400)

if __name__ == "__main__":
    unittest.main()
