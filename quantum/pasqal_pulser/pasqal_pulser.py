import matplotlib.pyplot as plt
import numpy as np
import pulser
from pulser_simulation import QutipEmulator

# Define the number of layers for the hexagonal register
layers = 3

# Create a hexagonal arrangement of atoms for the quantum register
reg = pulser.Register.hexagon(layers, prefix="q")

# Visualize the hexagonal register
reg.draw(with_labels=False)

# Define the duration of the pulse in time units (e.g., nanoseconds or microseconds)
duration = 1000  # Typical duration ~1 µsec

# Define a pulse with amplitude, detuning, and phase using custom waveforms
pulse = pulser.Pulse(
    amplitude=pulser.BlackmanWaveform(duration, np.pi),  # Smooth Blackman amplitude
    detuning=pulser.RampWaveform(duration, -5.0, 10.0),  # Linear ramp detuning
    phase=0  # Phase of the pulse
)

# Visualize the pulse waveform
pulse.draw()

# Define a rectangular arrangement of atoms for a quantum register
# This creates a 1x2 grid of atoms with a spacing of 8 units
reg = pulser.Register.rectangle(1, 2, spacing=8, prefix="atom")

# Visualize the rectangular register
reg.draw()

# Create a π pulse using constant detuning with a Blackman waveform
pi_pulse = pulser.Pulse.ConstantDetuning(
    pulser.BlackmanWaveform(duration, np.pi),  # Smooth Blackman waveform for amplitude
    0.0,  # Constant detuning value
    0.0   # Phase of the detuning
)

# Initialize a sequence with the defined register and a digital-analog device
seq = pulser.Sequence(reg, pulser.DigitalAnalogDevice)

# Declare a Rydberg channel for qubit operations
seq.declare_channel("ryd", "rydberg_local", "atom0")

# Add the π pulse to the Rydberg channel for atom0
seq.add(pi_pulse, "ryd")

# Change the target of the Rydberg channel to atom1
seq.target("atom1", "ryd")

# Add the π pulse to the Rydberg channel for atom1
seq.add(pi_pulse, "ryd")

# Visualize the sequence of operations
seq.draw()
