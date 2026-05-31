# OTOC, Echo, and Scrambling Summary

An out-of-time-order correlator is often written as

```text
F(t) = < W†(t) V† W(t) V >
W(t) = U† W U
```

It diagnoses how an initially local operator `W` grows under time evolution and fails to commute with another operator `V`. In chaotic or scrambling systems, local information spreads into many degrees of freedom, and the OTOC can decay.

The echo circuits in this repository are simpler:

```text
U -> U†
U -> W -> U†
```

The first circuit checks reversibility. The second asks how much a local perturbation `W` prevents returning to the initial state. Loss of return probability is an echo-style sensitivity diagnostic. It is related in spirit to OTOC physics, but it is not a complete hardware OTOC protocol.

Key interview point: echo decay can come from scrambling, but it can also come from decoherence, gate error, readout error, leakage, calibration drift, or bad qubit choice. Control experiments are essential.

