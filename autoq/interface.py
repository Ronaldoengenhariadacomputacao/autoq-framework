class QiskitInterface:
    def __init__(self, circuit):
        self.circuit = circuit

    def get_gate_count(self):
        """Retorna o número de portas no circuito."""
        return len(self.circuit.data)