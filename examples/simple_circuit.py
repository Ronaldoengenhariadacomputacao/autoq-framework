from qiskit import QuantumCircuit
from autoq import AutoQ

# Create a simple circuit
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)

# System parameters
system_params = {
    "t_gate": 1.0,
    "p_total": 0.011,
    "parallel_factor": 2.0
}

# Optimize with AutoQ
autoq = AutoQ(system_params)
optimized_circuit, metrics = autoq.optimize(circuit)

# Results
print("Results for Simple Circuit:")
for key, value in metrics.items():
    print(f"{key}: {value}")