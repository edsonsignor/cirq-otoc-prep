import cirq

from src.circuits import add_measurements, make_echo_circuit, make_line_qubits, make_simple_entangling_circuit
from src.observables import estimate_return_probability


def test_ideal_echo_returns_to_zero_state():
    qubits = make_line_qubits(3)
    U = make_simple_entangling_circuit(qubits, depth=4)
    echo = make_echo_circuit(U, qubits)
    measured = add_measurements(echo, qubits)

    result = cirq.Simulator().run(measured, repetitions=200)

    assert estimate_return_probability(result, len(qubits)) == 1.0

