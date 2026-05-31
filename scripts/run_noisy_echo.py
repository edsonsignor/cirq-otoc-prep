"""Compare ideal and noisy echo return probabilities."""

from __future__ import annotations

import pathlib
import sys

import numpy as np

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.analysis import sweep_noise_strength
from src.circuits import make_line_qubits
from src.plotting import plot_echo_signal_vs_noise


def main() -> None:
    qubits = make_line_qubits(3)
    df = sweep_noise_strength(qubits, depth=4, noise_values=np.linspace(0, 0.05, 11))
    print(df.to_string(index=False))
    output = pathlib.Path("figures/noisy_echo.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    plot_echo_signal_vs_noise(df, str(output))
    print(f"Saved plot to {output}")


if __name__ == "__main__":
    main()

