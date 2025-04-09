from .transpiler import CircuitTranspiler
from .scheduler import ParallelScheduler
from .qec import StandardQEC
from .interface import QiskitInterface

class AutoQ:
    def __init__(self, system_params):
        required_params = ["t_gate", "p_total", "parallel_factor"]
        for param in required_params:
            if param not in system_params:
                raise ValueError(f"Missing required parameter: {param}")
        self.t_gate = system_params["t_gate"]
        self.p_total = system_params["p_total"]
        self.parallel_factor = system_params["parallel_factor"]
        self.transpiler = CircuitTranspiler()
        self.scheduler = ParallelScheduler(self.parallel_factor)
        self.qec = StandardQEC(self.p_total)

    def optimize(self, circuit):
        """Otimizador principal do AutoQ."""
        interface = QiskitInterface(circuit)
        original_gates = interface.get_gate_count()
        optimized_circuit = self.transpiler.transpile(circuit)
        optimized_gates = len(optimized_circuit.data)
        scheduled_gates = self.scheduler.schedule(optimized_circuit)
        physical_gates = self.qec.apply_qec(scheduled_gates)
        original_time = original_gates * self.qec.overhead * self.t_gate
        optimized_time = physical_gates * self.t_gate
        original_speed = original_gates / original_time if original_time > 0 else 0
        optimized_speed = optimized_gates / optimized_time if optimized_time > 0 else 0

        metrics = {
            "original_gates": original_gates,
            "optimized_gates": optimized_gates,
            "original_time": original_time,
            "optimized_time": optimized_time,
            "original_speed": original_speed,
            "optimized_speed": optimized_speed
        }

        return optimized_circuit, metrics