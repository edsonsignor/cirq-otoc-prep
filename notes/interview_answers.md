# Interview Answers

## What is Cirq?

Cirq is a Python quantum circuit framework. It is useful for constructing circuits at the gate and qubit level, simulating them, adding noise models, and preparing circuits that can later be adapted to device-specific workflows.

## What is an OTOC?

An OTOC is a correlation function with operators in a non-time-ordered sequence, commonly written `F(t) = < W†(t) V† W(t) V >`. It measures how operators fail to commute after time evolution and is used as a diagnostic of scrambling.

## What is an echo protocol?

An echo applies forward evolution `U` and then reverse evolution `U†`. Ideally, the state returns to its initial state. If a perturbation is inserted between `U` and `U†`, loss of return probability measures sensitivity to that perturbation.

## How would I implement a toy OTOC in Cirq?

I would build a unitary circuit `U`, insert a local operator `W`, apply `U†`, and measure a return probability or simple observable. I would sweep perturbation strength, depth, and noise. I would state clearly that this is pedagogical and not a full hardware OTOC protocol.

## How do I know whether gates are good?

I would inspect gate fidelities, readout error, decoherence times, leakage, crosstalk, calibration drift, and the chosen qubit layout. I would run control circuits to separate coherent scrambling-like effects from ordinary hardware decay.

## How do I distinguish scrambling from decoherence?

I would compare perturbed and unperturbed echoes, vary circuit depth, run noise controls, use calibration data, repeat measurements over time, and check whether the signal follows a physically expected perturbation-spreading pattern rather than simply tracking circuit duration or gate count.

## What is my honest weakness?

I am new to Cirq and hardware-specific workflows. I am addressing that by building small runnable circuits, writing tests for ideal behavior, adding controlled noise, and practicing how to explain the gap between local simulation and calibrated hardware experiments.

