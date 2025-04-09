from qiskit import transpile

class CircuitTranspiler:
    def __init__(self, optimization_level=3):
        self.optimization_level = optimization_level

    def transpile(self, circuit):
        """Reduz o número de portas no circuito."""
        optimized_circuit = transpile(circuit, optimization_level=self.optimization_level)
        return optimized_circuit