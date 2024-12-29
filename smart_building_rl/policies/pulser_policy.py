from pulser import Pulse, Register
from pulser.devices import Chadoq2
from pulser.simulation import Simulation

class PulserPolicy:
    """Policy class using Pasqal Pulser."""
    def __init__(self):
        self.device = Chadoq2
        self.reg = Register.square(2)
        self.sequence = self._create_sequence()

    def _create_sequence(self):
        sequence = self.reg.build_pulse_sequence()
        sequence.add(Pulse.ConstantPulse(100, 1.0, 0.0, 0.0), self.reg.qubits[0])
        return sequence

    def evaluate(self, state):
        """Evaluates the state and returns an action."""
        sim = Simulation(self.sequence, self.device)
        result = sim.run()
        probabilities = abs(result.state) ** 2
        return int(probabilities.argmax() % 3)  # Choose an action based on probabilities
