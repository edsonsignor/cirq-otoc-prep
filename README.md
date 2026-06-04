# Cirq OTOC Preparation

This repository is a beginner-friendly but research-oriented preparation project for learning Cirq and studying echo-style circuits related to Loschmidt echoes, toy OTOC diagnostics, scrambling, and hardware noise.

It is for interview and study preparation. It is not an official Google, Willow, or hardware-calibrated OTOC implementation.

## Motivation

The goal is to build enough practical fluency to discuss:

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

## Two-Week Study Plan

Day 1: Run `01_cirq_basics.ipynb` and `scripts/run_basic_circuit.py`. Commit: basic Cirq notes and first Bell circuit output.

Day 2: Read `src/circuits.py`. Modify one rotation angle and predict the result before running it. Commit: comments or notes on circuit construction.

Day 3: Run `scripts/run_echo.py`. Explain why `U -> U†` returns to the initial state in ideal simulation. Commit: ideal echo result.

Day 4: Work through `02_echo_circuits.ipynb`. Commit: Loschmidt echo notes.

Day 5: Run `scripts/run_perturbed_echo.py`. Inspect `figures/perturbed_echo.png`. Commit: perturbation sweep plot.

Day 6: Work through `03_perturbed_echo.ipynb`. Commit: notes on local perturbations and sensitivity.

Day 7: Read `notes/otoc_summary.md`. Explain the difference between a full OTOC and this toy diagnostic. Commit: toy OTOC explanation.

Day 8: Run `scripts/run_toy_otoc.py`. Commit: toy OTOC diagnostic output.

Day 9: Run `scripts/run_noisy_echo.py`. Commit: noisy echo plot.

Day 10: Work through `05_noisy_echo.ipynb`. Commit: notes on why noise can fake decay.

Day 11: Study `notes/hardware_noise_checklist.md`. Commit: gate-quality checklist refinements.

Day 12: Run `pytest`. Commit: tests passing and any small fixes.

Day 13: Work through `06_interview_summary.ipynb`. Commit: polished interview answers.

Day 14: Do a mock interview using `notes/interview_answers.md`. Commit: final study summary and next questions.

## Deliverables

- A runnable local Cirq repository.
- Ideal and perturbed echo scripts.
- Noisy echo simulations.
- Plots of return probability versus perturbation and noise.
- Beginner-facing notebooks.
- Interview notes connecting simulation, physics, and hardware limitations.

## Important Limitation

The examples here use local simulation with simple noise channels. Real Willow experiments require hardware access, calibration data, device-specific compilation, qubit selection, readout mitigation, control circuits, and experimental protocols beyond this repository.



