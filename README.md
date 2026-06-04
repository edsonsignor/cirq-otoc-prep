# Cirq OTOC Preparation

This repository is a beginner-friendly Cirq learning and studying echo-style circuits related to Loschmidt echoes, toy OTOC diagnostics, scrambling, and hardware noise.

## Motivation

- Cirq qubits, gates, operations, circuits, moments, measurements, simulators, and shots.
- Echo circuits of the form `U -> U†`.
- Perturbed echoes of the form `U -> W -> U†`.
- How echo decay connects to sensitivity, scrambling, Loschmidt echoes, and toy OTOC thinking.
- Why noisy hardware can mimic signal decay.
- How to reason about gate fidelity, readout error, decoherence, leakage, calibration drift, qubit choice, and control circuits.

## Installation

Using `venv`:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Using conda:

```bash
conda env create -f environment.yml
conda activate cirq-otoc-prep
```

## Run Scripts

From the repository root:

```bash
python scripts/run_basic_circuit.py
python scripts/run_echo.py
python scripts/run_perturbed_echo.py
python scripts/run_toy_otoc.py
python scripts/run_noisy_echo.py
```

Run tests:

```bash
pytest
```

## Repository Map

- `src/circuits.py`: qubit and circuit builders.
- `src/observables.py`: simple estimators from measurement results.
- `src/noise.py`: local Cirq noise models.
- `src/analysis.py`: parameter sweeps.
- `src/plotting.py`: Matplotlib plotting helpers.
- `scripts/`: command-line entry points.
- `notebooks/`: guided learning notebooks.
- `notes/`: interview and physics summaries.
- `tests/`: minimal correctness checks.



