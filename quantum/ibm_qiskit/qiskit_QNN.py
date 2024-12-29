from qiskit import Aer, QuantumCircuit
from qiskit.circuit import Parameter
from qiskit_machine_learning.neural_networks import EstimatorQNN
from qiskit_machine_learning.connectors import TorchConnector
import torch
import torch.nn as nn

# Create a parameterized quantum circuit
num_qubits = 2
qc = QuantumCircuit(num_qubits)

# Parameters for rotation gates
theta = Parameter("θ")
qc.h(0)
qc.cx(0, 1)
qc.rx(theta, 0)
qc.measure_all()

# Use Qiskit Aer simulator
backend = Aer.get_backend('statevector_simulator')

# Define a Quantum Neural Network
qnn = EstimatorQNN(qc, input_params=[theta], backend=backend)

# Connect to PyTorch
qnn_layer = TorchConnector(qnn)

# Create a PyTorch model
class QuantumModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(1, 1)
        self.qnn = qnn_layer

    def forward(self, x):
        x = self.fc(x)
        return self.qnn(x)

# Instantiate and train the model
model = QuantumModel()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Dummy data
X = torch.tensor([[0.1], [0.2], [0.3]], dtype=torch.float32)
y = torch.tensor([[0.3], [0.5], [0.7]], dtype=torch.float32)

for epoch in range(10):
    optimizer.zero_grad()
    output = model(X)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch + 1}: Loss = {loss.item():.4f}")