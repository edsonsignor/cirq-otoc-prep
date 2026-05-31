"""Small parameter sweeps for echo and toy OTOC diagnostics."""

from __future__ import annotations

from collections.abc import Iterable

import cirq
import numpy as np
import pandas as pd

from .circuits import (
    add_measurements,
    make_echo_circuit,
    make_perturbed_echo_circuit,
    make_simple_entangling_circuit,
)
from .noise import depolarizing_noise_model
from .observables import estimate_return_probability


def _sample_return_probability(
    circuit: cirq.Circuit,
    qubits: list[cirq.Qid],
    repetitions: int = 2000,
    noise: cirq.NoiseModel | None = None,
) -> float:
    simulator = cirq.Simulator(noise=noise)
    measured = add_measurements(circuit, qubits)
    result = simulator.run(measured, repetitions=repetitions)
    return estimate_return_probability(result, len(qubits))


def sweep_perturbation_strength(
    qubits: list[cirq.Qid],
    depth: int,
    theta_values: Iterable[float],
    repetitions: int = 2000,
) -> pd.DataFrame:
    """Sweep local perturbation angle and return echo signal estimates."""
    U = make_simple_entangling_circuit(qubits, depth)
    rows = []
    for theta in theta_values:
        circuit = make_perturbed_echo_circuit(U, qubits, theta=float(theta))
        rows.append(
            {
                "theta": float(theta),
                "return_probability": _sample_return_probability(
                    circuit, qubits, repetitions=repetitions
                ),
            }
        )
    return pd.DataFrame(rows)


def sweep_circuit_depth(
    qubits: list[cirq.Qid],
    depths: Iterable[int],
    repetitions: int = 2000,
) -> pd.DataFrame:
    """Sweep depth for an ideal U followed by U dagger echo."""
    rows = []
    for depth in depths:
        U = make_simple_entangling_circuit(qubits, int(depth))
        circuit = make_echo_circuit(U, qubits)
        rows.append(
            {
                "depth": int(depth),
                "return_probability": _sample_return_probability(
                    circuit, qubits, repetitions=repetitions
                ),
            }
        )
    return pd.DataFrame(rows)


def sweep_noise_strength(
    qubits: list[cirq.Qid],
    depth: int,
    noise_values: Iterable[float],
    repetitions: int = 2000,
) -> pd.DataFrame:
    """Sweep depolarizing noise strength for a perfect echo circuit."""
    U = make_simple_entangling_circuit(qubits, depth)
    circuit = make_echo_circuit(U, qubits)
    rows = []
    for p in noise_values:
        rows.append(
            {
                "noise": float(p),
                "return_probability": _sample_return_probability(
                    circuit,
                    qubits,
                    repetitions=repetitions,
                    noise=depolarizing_noise_model(float(p)),
                ),
            }
        )
    return pd.DataFrame(rows)


def default_theta_values(num: int = 21) -> np.ndarray:
    """Return a useful default theta grid from 0 to pi."""
    return np.linspace(0.0, np.pi, num)

