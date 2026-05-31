"""Plotting helpers for echo sweeps."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def _plot_signal(
    df: pd.DataFrame, x: str, xlabel: str, title: str, output_path: str | None
):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(df[x], df["return_probability"], marker="o")
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Return probability")
    ax.set_ylim(-0.05, 1.05)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    if output_path:
        fig.savefig(output_path, dpi=160)
    return fig, ax


def plot_echo_signal_vs_theta(df: pd.DataFrame, output_path: str | None = None):
    """Plot return probability versus perturbation angle."""
    return _plot_signal(df, "theta", "Perturbation angle theta", "Perturbed echo", output_path)


def plot_echo_signal_vs_depth(df: pd.DataFrame, output_path: str | None = None):
    """Plot return probability versus circuit depth."""
    return _plot_signal(df, "depth", "Circuit depth", "Ideal echo depth sweep", output_path)


def plot_echo_signal_vs_noise(df: pd.DataFrame, output_path: str | None = None):
    """Plot return probability versus depolarizing noise strength."""
    return _plot_signal(df, "noise", "Depolarizing probability", "Noisy echo", output_path)

