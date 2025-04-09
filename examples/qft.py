from qiskit import QuantumCircuit
from autoq import AutoQ

# Create a QFT circuit for 4 qubits
n = 4
circuit = QuantumCircuit(n)
for i in range(n):
    circuit.h(i)
    for j in range(i + 1, n):
        circuit.cp(3.14159 / 2**(j - i), j, i)
for i in range(n // 2):
    circuit.swap(i, n - 1 - i)

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
print("Results for QFT (4 qubits):")
for key, value in metrics.items():
    print(f"{key}: {value}")
