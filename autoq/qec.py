class StandardQEC:
    def __init__(self, p_total):
        self.p_total = p_total
        self.overhead = self.calculate_overhead()

    def calculate_overhead(self):
        """Calcula o overhead de QEC com base em p_total."""
        if self.p_total < 0.01:
            overhead = 10
        elif self.p_total < 0.05:
            overhead = 20
        else:
            overhead = 30
        return overhead * 0.9

    def apply_qec(self, scheduled_gates):
        """Aplica QEC, retornando o número de portas físicas."""
        return scheduled_gates * self.overhead