"""Run a basic Bell-state circuit in Cirq."""

from __future__ import annotations

import pathlib
import sys

import cirq

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))


def main() -> None:
    q0, q1 = cirq.LineQubit.range(2)
    circuit = cirq.Circuit(cirq.H(q0), cirq.CNOT(q0, q1), cirq.measure(q0, q1, key="m"))
    result = cirq.Simulator().run(circuit, repetitions=1000)

    print(circuit)
    print(result.histogram(key="m"))


if __name__ == "__main__":
    main()

