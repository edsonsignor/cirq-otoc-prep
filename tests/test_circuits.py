import cirq

from src.circuits import (
    add_measurements,
    make_echo_circuit,
    make_line_qubits,
    make_perturbed_echo_circuit,
    make_simple_entangling_circuit,
)


def test_make_line_qubits_count():
    qubits = make_line_qubits(3)
    assert qubits == [cirq.LineQubit(0), cirq.LineQubit(1), cirq.LineQubit(2)]


def test_echo_circuit_contains_inverse():
    qubits = make_line_qubits(2)
    U = make_simple_entangling_circuit(qubits, depth=2)
    echo = make_echo_circuit(U, qubits)
    assert len(echo) >= len(U)


def test_perturbed_echo_accepts_z_rotation():
    qubits = make_line_qubits(2)
    U = make_simple_entangling_circuit(qubits, depth=1)
    circuit = make_perturbed_echo_circuit(U, qubits, perturbation="Z", theta=0.2)
    assert isinstance(circuit, cirq.Circuit)


def test_add_measurements_adds_key():
    qubits = make_line_qubits(2)
    circuit = add_measurements(cirq.Circuit(), qubits, key="readout")
    measurement_keys = []
    for op in circuit.all_operations():
        if isinstance(op.gate, cirq.MeasurementGate):
            measurement_keys.append(cirq.measurement_key_name(op))
    assert "readout" in measurement_keys
