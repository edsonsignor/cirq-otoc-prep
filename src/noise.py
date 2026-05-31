"""Noise-model helpers for local Cirq simulations."""

from __future__ import annotations

import cirq


def depolarizing_noise_model(p: float) -> cirq.NoiseModel:
    """Return a depolarizing noise model applied after each operation."""
    if not 0 <= p <= 1:
        raise ValueError("p must be in [0, 1]")
    return cirq.ConstantQubitNoiseModel(cirq.depolarize(p))


def amplitude_damping_noise_model(gamma: float) -> cirq.NoiseModel:
    """Return an amplitude damping noise model."""
    if not 0 <= gamma <= 1:
        raise ValueError("gamma must be in [0, 1]")
    return cirq.ConstantQubitNoiseModel(cirq.amplitude_damp(gamma))


def phase_damping_noise_model(gamma: float) -> cirq.NoiseModel:
    """Return a phase damping noise model."""
    if not 0 <= gamma <= 1:
        raise ValueError("gamma must be in [0, 1]")
    return cirq.ConstantQubitNoiseModel(cirq.phase_damp(gamma))

