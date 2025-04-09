from qiskit import QuantumCircuit
from autoq import AutoQ

# Create a simplified Shor circuit for N=35
circuit = QuantumCircuit(14)
for i in range(400):
    circuit.h(i % 14)  # Distribute Hadamard gates

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
print("Results for Shor N=35:")
for key, value in metrics.items():
    print(f"{key}: {value}")