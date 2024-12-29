from pulser import Pulse, Register
from pulser.devices import Chadoq2
from pulser.simulation import Simulation
import numpy as np

# Define a 2-qubit register
reg = Register.square(2)

# Device and parameters
device = Chadoq2
amplitude = 1.0
phase = 0.0
detuning = 0.0

# Create a pulse sequence
sequence = reg.build_pulse_sequence()
theta = np.pi / 4

# Add pulses
sequence.add(Pulse.ConstantPulse(100, amplitude, phase, detuning), reg.qubits[0])
sequence.add(Pulse.ConstantPulse(100, amplitude, theta, detuning), reg.qubits[1])

# Simulate the sequence
sim = Simulation(sequence, device=device)
result = sim.run()
print("Final statevector:", result.state)
