import cirq
import numpy as np
import matplotlib.pyplot as plt
import sympy


# Define qubits and circuit
qubits = [cirq.GridQubit(0, i) for i in range(2)]
theta = sympy.Symbol("theta")
circuit = cirq.Circuit(
    cirq.H(qubits[0]),                # Apply Hadamard gate
    cirq.CNOT(qubits[0], qubits[1]),  # Create entanglement
    cirq.rx(theta).on(qubits[0])      # Rotation gate based on parameter theta
)

# Simulate the circuit
simulator = cirq.Simulator()

def evaluate_action(state, action, theta_val):
    """
    Simulates the quantum circuit for a given state-action pair with parameter theta_val.
    Returns the probability of the |0⟩ state as the Q-value proxy.
    """
    param_resolver = cirq.ParamResolver({theta: theta_val})
    result = simulator.simulate(circuit, param_resolver)
    q_value = abs(result.final_state_vector[0])**2  # Probability amplitude squared of |0⟩
    return q_value

# Initialize Q-table
num_states = 5
num_actions = 2
Q_table = np.zeros((num_states, num_actions))  # Q-table initialized to zeros

def update_q_table(state, action, reward, next_state, alpha=0.1, gamma=0.9):
    """
    Updates the Q-value for a given state-action pair using a quantum circuit for evaluation.
    """
    current_q = Q_table[state, action]
    max_future_q = np.max(Q_table[next_state])  # Maximum Q-value of the next state

    # Quantum-enhanced Q-value evaluation
    quantum_q_value = evaluate_action(state, action, theta_val=reward)

    # Q-learning update rule
    Q_table[state, action] = (1 - alpha) * current_q + alpha * (reward + gamma * quantum_q_value)

# Example environment setup
states = [0, 1, 2, 3, 4]  # Example states (e.g., temperature ranges)
actions = [0, 1]          # Example actions (e.g., turn HVAC on/off)
rewards = np.random.rand(len(states), len(actions))  # Random rewards for illustration

# Simulate the RL process
num_episodes = 10
for episode in range(num_episodes):
    state = np.random.choice(states)  # Start from a random state
    for step in range(10):  # Each episode has a fixed number of steps
        # Choose an action (e.g., epsilon-greedy policy)
        action = np.random.choice(actions)

        # Get the reward and next state
        reward = rewards[state, action]
        next_state = (state + 1) % len(states)  # Example transition logic

        # Update the Q-table
        update_q_table(state, action, reward, next_state)

        # Move to the next state
        state = next_state

# Print the final Q-table
print("Final Q-Table:")
print(Q_table)


# Plot the Q-table for visualization
plt.imshow(Q_table, cmap="coolwarm", interpolation="nearest")
plt.colorbar(label="Q-value")
plt.xlabel("Actions")
plt.ylabel("States")
plt.title("Final Q-Table Heatmap")
plt.show()
