"""Sweep a local perturbation inserted between U and U dagger."""

from __future__ import annotations

import argparse
import pathlib
import sys

import numpy as np

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.analysis import sweep_perturbation_strength
from src.circuits import make_line_qubits
from src.plotting import plot_echo_signal_vs_theta


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-qubits", type=int, default=3)
    parser.add_argument("--depth", type=int, default=4)
    parser.add_argument("--shots", type=int, default=2000)
    parser.add_argument("--num-points", type=int, default=21)
    parser.add_argument("--save", default="figures/perturbed_echo.png")
    args = parser.parse_args()

    qubits = make_line_qubits(args.n_qubits)
    theta_values = np.linspace(0.0, np.pi, args.num_points)
    df = sweep_perturbation_strength(
        qubits, args.depth, theta_values, repetitions=args.shots
    )

    print(df.to_string(index=False))
    if args.save:
        output = pathlib.Path(args.save)
        output.parent.mkdir(parents=True, exist_ok=True)
        plot_echo_signal_vs_theta(df, str(output))
        print(f"Saved plot to {output}")


if __name__ == "__main__":
    main()

