"""Run an ideal Loschmidt echo circuit U followed by U dagger."""

from __future__ import annotations

import argparse
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import cirq

from src.circuits import add_measurements, make_echo_circuit, make_line_qubits, make_simple_entangling_circuit
from src.observables import bitstring_histogram, estimate_return_probability


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-qubits", type=int, default=3)
    parser.add_argument("--depth", type=int, default=4)
    parser.add_argument("--shots", type=int, default=2000)
    args = parser.parse_args()

    qubits = make_line_qubits(args.n_qubits)
    U = make_simple_entangling_circuit(qubits, args.depth)
    echo = make_echo_circuit(U, qubits)
    measured = add_measurements(echo, qubits)

    result = cirq.Simulator().run(measured, repetitions=args.shots)
    return_probability = estimate_return_probability(result, args.n_qubits)

    print("Ideal echo circuit:")
    print(measured)
    print("\nCounts:", bitstring_histogram(result))
    print(f"Return probability P(00...0): {return_probability:.4f}")


if __name__ == "__main__":
    main()

