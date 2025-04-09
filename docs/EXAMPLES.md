# Examples

## 5.1. Setup
- **Circuit:** Shor’s algorithm for \( N = 35 \), with 14 qubits and ~400 logical gates.
- **System:** Photonic system (\( t_{\text{gate}} = 1 \, \mu\text{s} \), \( p_{\text{total}} \sim 1.1\% \), parallelism 2.0).

## 5.2. Code
```python
from qiskit import QuantumCircuit
from autoq import AutoQ

# Create a simplified Shor circuit
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