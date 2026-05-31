# Cirq Summary

Cirq is a Python framework for writing, transforming, simulating, and executing quantum circuits. Its core objects are:

- `Qid` / `LineQubit`: labels for quantum degrees of freedom.
- `Gate`: an abstract operation such as `H`, `CZ`, `rx(theta)`, or `measure`.
- `Operation`: a gate applied to specific qubits.
- `Circuit`: an ordered collection of operations arranged into moments.
- `Simulator`: a local simulator for ideal or noisy circuits.
- `Result`: sampled measurement data.

Minimal workflow:

```python
import cirq

q0, q1 = cirq.LineQubit.range(2)
circuit = cirq.Circuit(cirq.H(q0), cirq.CNOT(q0, q1), cirq.measure(q0, q1, key="m"))
result = cirq.Simulator().run(circuit, repetitions=1000)
print(result.histogram(key="m"))
```

For interviews, be clear that writing a circuit is not the same as running a calibrated hardware experiment. Hardware requires compilation, calibration awareness, qubit selection, error characterization, and controls.

