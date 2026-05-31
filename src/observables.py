"""Observable estimators from sampled Cirq measurement results."""

from __future__ import annotations

from collections import Counter

import cirq


def _measurement_rows(result: cirq.Result, key: str) -> list[tuple[int, ...]]:
    if key not in result.measurements:
        raise KeyError(f"measurement key {key!r} not found")
    return [tuple(int(x) for x in row) for row in result.measurements[key]]


def bitstring_histogram(result: cirq.Result, key: str = "m") -> dict[str, int]:
    """Return counts keyed by bitstrings such as '010'."""
    rows = _measurement_rows(result, key)
    counts = Counter("".join(str(bit) for bit in row) for row in rows)
    return dict(sorted(counts.items()))


def probability_all_zero(
    result: cirq.Result, n_qubits: int, key: str = "m"
) -> float:
    """Estimate the probability of measuring |00...0>."""
    rows = _measurement_rows(result, key)
    if not rows:
        return 0.0
    zero = tuple(0 for _ in range(n_qubits))
    return sum(row[:n_qubits] == zero for row in rows) / len(rows)


def expectation_z_from_counts(
    result: cirq.Result, qubit_index: int, n_qubits: int, key: str = "m"
) -> float:
    """Estimate <Z_i> from computational-basis samples."""
    if not 0 <= qubit_index < n_qubits:
        raise IndexError("qubit_index is out of range")

    rows = _measurement_rows(result, key)
    if not rows:
        return 0.0
    values = [1 if row[qubit_index] == 0 else -1 for row in rows]
    return sum(values) / len(values)


def estimate_return_probability(
    result: cirq.Result, n_qubits: int, key: str = "m"
) -> float:
    """Estimate echo return probability to the initial |00...0> state."""
    return probability_all_zero(result, n_qubits, key)

