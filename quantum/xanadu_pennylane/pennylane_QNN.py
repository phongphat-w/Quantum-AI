import pennylane as qml
from pennylane import numpy as np
import tensorflow as tf

# Define quantum device and circuit
n_qubits = 2
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev, interface="tf")
def quantum_circuit(inputs, weights):
    # Use the shape information for tensor compatibility
    for i in range(inputs.shape[-1]):  # Loop through input features
        qml.RY(inputs[i], wires=i)
    qml.CNOT(wires=[0, 1])
    qml.Rot(weights[0], weights[1], weights[2], wires=0)
    return qml.expval(qml.PauliZ(0))

# TensorFlow model integration
inputs = tf.keras.Input(shape=(n_qubits,))  # Input layer with shape (n_qubits,)
weights = tf.Variable(tf.random.uniform((3,)))  # Trainable weights for the quantum circuit

# Lambda layer with specified output shape
outputs = tf.keras.layers.Lambda(
    lambda x: quantum_circuit(x, weights),  # Quantum circuit applied to inputs
    output_shape=(1,)  # Specify output shape explicitly
)(inputs)
outputs

# Build and compile the model
model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.compile(optimizer="adam", loss="mse")

# Example data
X = np.random.rand(10, n_qubits)  # 10 samples with 2 features each
y = np.random.rand(10, 1)  # Random target values

# Train the model
model.fit(X, y, epochs=10, batch_size=2)