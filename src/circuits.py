"""Circuit-building utilities for Cirq echo and toy OTOC studies."""

from __future__ import annotations

import numpy as np
import cirq


def make_line_qubits(n: int) -> list[cirq.LineQubit]:
    """Return n nearest-neighbor line qubits."""
    if n <= 0:
        raise ValueError("n must be positive")
    return list(cirq.LineQubit.range(n))


def make_simple_entangling_circuit(
    qubits: list[cirq.Qid], depth: int
) -> cirq.Circuit:
    """Build a deterministic circuit with single-qubit rotations and CZ gates."""
    if depth < 0:
        raise ValueError("depth must be non-negative")

    circuit = cirq.Circuit()
    for layer in range(depth):
        for i, q in enumerate(qubits):
            circuit.append(cirq.ry(0.17 * (layer + 1) * (i + 1))(q))
            circuit.append(cirq.rz(0.11 * (layer + 1))(q))

        start = layer % 2
        for i in range(start, len(qubits) - 1, 2):
            circuit.append(cirq.CZ(qubits[i], qubits[i + 1]))

    return circuit


def make_random_layered_circuit(
    qubits: list[cirq.Qid], depth: int, seed: int | None = None
) -> cirq.Circuit:
    """Build a small pseudo-random layered circuit with reproducible angles."""
    if depth < 0:
        raise ValueError("depth must be non-negative")

    rng = np.random.default_rng(seed)
    circuit = cirq.Circuit()
    for layer in range(depth):
        for q in qubits:
            circuit.append(cirq.rx(float(rng.uniform(-np.pi, np.pi)))(q))
            circuit.append(cirq.rz(float(rng.uniform(-np.pi, np.pi)))(q))

        for i in range(layer % 2, len(qubits) - 1, 2):
            circuit.append(cirq.CZ(qubits[i], qubits[i + 1]))

    return circuit


def make_echo_circuit(U: cirq.Circuit, qubits: list[cirq.Qid]) -> cirq.Circuit:
    """Return the Loschmidt echo circuit U followed by U dagger."""
    del qubits  # Kept in the signature to make call sites explicit.
    return cirq.Circuit(U, cirq.inverse(U))


def make_perturbed_echo_circuit(
    U: cirq.Circuit,
    qubits: list[cirq.Qid],
    perturbation_qubit: int = 0,
    perturbation: str = "Z",
    theta: float | None = None,
) -> cirq.Circuit:
    """Return U, then a local perturbation W, then U dagger."""
    if not 0 <= perturbation_qubit < len(qubits):
        raise IndexError("perturbation_qubit is out of range")

    q = qubits[perturbation_qubit]
    angle = np.pi if theta is None else theta
    name = perturbation.upper()

    if name == "X":
        W = cirq.rx(angle)(q)
    elif name == "Y":
        W = cirq.ry(angle)(q)
    elif name == "Z":
        W = cirq.rz(angle)(q)
    else:
        raise ValueError("perturbation must be 'X', 'Y', or 'Z'")

    return cirq.Circuit(U, W, cirq.inverse(U))


def add_measurements(
    circuit: cirq.Circuit, qubits: list[cirq.Qid], key: str = "m"
) -> cirq.Circuit:
    """Return a copy of circuit with computational-basis measurements appended."""
    measured = circuit.copy()
    measured.append(cirq.measure(*qubits, key=key))
    return measured

