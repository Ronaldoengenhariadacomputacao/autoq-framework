class ParallelScheduler:
    def __init__(self, parallel_factor):
        self.parallel_factor = parallel_factor

    def schedule(self, circuit):
        """Simula paralelismo, reduzindo o tempo lógico."""
        gate_count = len(circuit.data)
        scheduled_gates = gate_count / self.parallel_factor
        return scheduled_gates