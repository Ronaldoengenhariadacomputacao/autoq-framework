# Usage

## 4.1. Basic Structure
AutoQ is used as a Python library. The user provides a quantum circuit (via Qiskit) and system parameters (e.g., \( p_{\text{total}} \), \( t_{\text{gate}} \)), and AutoQ returns the optimized circuit with speed metrics.

## 4.2. Example Usage
Here’s an example of using AutoQ to optimize a quantum circuit:

```python
from qiskit import QuantumCircuit
from autoq import AutoQ

# Create a quantum circuit (simplified example)
circuit = QuantumCircuit(14)  # 14 qubits
for i in range(400):
    circuit.h(0)  # Add Hadamard gates as an example

# Configure system parameters
system_params = {
    "t_gate": 1.0,  # Gate time in µs
    "p_total": 0.011,  # Total error rate (1.1%)
    "parallel_factor": 2.0  # Parallelism factor
}

# Initialize AutoQ
autoq = AutoQ(system_params)

# Optimize the circuit
optimized_circuit, metrics = autoq.optimize(circuit)

# Display results
print("AutoQ Metrics:")
print(f"Original Gates: {metrics['original_gates']}")
print(f"Optimized Gates: {metrics['optimized_gates']}")
print(f"Original Time: {metrics['original_time']} µs")
print(f"Optimized Time: {metrics['optimized_time']} µs")
print(f"Original Speed: {metrics['original_speed']} gates/µs")
print(f"Optimized Speed: {metrics['optimized_speed']} gates/µs")