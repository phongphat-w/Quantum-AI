import pennylane as qml
from pennylane import numpy as np

class PennyLanePolicy:
    """Policy class using Xanadu PennyLane."""
    def __init__(self):
        self.num_qubits = 3
        self.dev = qml.device("default.qubit", wires=self.num_qubits)

    @qml.qnode(self.dev)
    def circuit(self, inputs, weights):
        for i in range(len(inputs)):
            qml.RX(inputs[i], wires=i)
        for i in range(len(weights)):
            qml.RY(weights[i], wires=i)
        return qml.probs(wires=[0, 1, 2])

    def evaluate(self, state):
        """Evaluates the state and returns an action."""
        weights = np.random.uniform(0, np.pi, self.num_qubits)
        return int(self.circuit(state, weights).argmax())
