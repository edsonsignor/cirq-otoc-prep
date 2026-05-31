# Hardware Noise Checklist

Use this checklist when asked, "How do you know the gates are good?"

- Gate fidelity: compare single-qubit and two-qubit gate error rates, especially entangling gates.
- Readout error: measure assignment errors and consider readout mitigation.
- Decoherence: check `T1`, `T2`, and whether circuit duration is short compared with coherence times.
- Leakage: verify population is not leaving the computational subspace.
- Calibration drift: repeat calibrations or benchmarks over time.
- Crosstalk: check whether operations on one qubit disturb neighbors.
- Qubit selection: prefer connected qubits with strong two-qubit gates and stable readout.
- Circuit depth: compare expected signal with accumulated error budget.
- Control circuits: run identity echoes, no-perturbation echoes, randomized controls, and noise-only baselines.
- Statistical uncertainty: use enough shots and report error bars.

Interview phrasing: "I would not interpret OTOC-like decay until I had control circuits showing that the same decay is not explained by decoherence, readout, leakage, or calibration drift."

