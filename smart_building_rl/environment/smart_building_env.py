import numpy as np

class SmartBuildingEnv:
    """Environment class for simulating a smart building."""
    def __init__(self):
        self.temperature = 22  # Initial temperature in Celsius
        self.energy_usage = 0  # Initial energy usage
        self.light_intensity = 50  # Initial light intensity (0-100 scale)
        self.max_steps = 20  # Max steps per episode
        self.current_step = 0

    def reset(self):
        """Resets the environment to its initial state."""
        self.temperature = 22
        self.energy_usage = 0
        self.light_intensity = 50
        self.current_step = 0
        return np.array([self.temperature, self.energy_usage, self.light_intensity])

    def step(self, action):
        """Performs an action in the environment and returns the next state, reward, and done flag."""
        if action == 0:
            self.temperature -= 1
        elif action == 1:
            self.temperature += 1
        elif action == 2:
            self.light_intensity += 10

        self.energy_usage += abs(self.temperature - 22) + abs(self.light_intensity - 50)
        reward = -self.energy_usage

        self.current_step += 1
        done = self.current_step >= self.max_steps
        return np.array([self.temperature, self.energy_usage, self.light_intensity]), reward, done
