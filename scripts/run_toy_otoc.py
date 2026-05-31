"""Run a toy echo-inspired OTOC-like diagnostic."""

from __future__ import annotations

import pathlib
import sys

import numpy as np

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.analysis import sweep_perturbation_strength
from src.circuits import make_line_qubits


def main() -> None:
    qubits = make_line_qubits(4)
    df = sweep_perturbation_strength(qubits, depth=5, theta_values=np.linspace(0, np.pi, 11))
    print("Toy OTOC-like echo diagnostic.")
    print("Signal loss indicates sensitivity to a local perturbation, but it is not a full hardware OTOC protocol.")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()

