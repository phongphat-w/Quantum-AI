# Smart Building Reinforcement Learning with Quantum Policies

This project implements a **Reinforcement Learning (RL)** system for optimizing smart building operations using quantum-enhanced policies. It evaluates four quantum computing libraries:
- **IBM Qiskit**
- **Google Cirq**
- **Pasqal Pulser**
- **Xanadu PennyLane**

The goal is to compare the performance of quantum policies in an RL environment simulating energy optimization, HVAC management, and lighting control for smart buildings.

---

## **Project Structure**
```
smart_building_rl/
├── environment/
│   ├── __init__.py
│   ├── smart_building_env.py       # Environment class
├── policies/
│   ├── __init__.py
│   ├── qiskit_policy.py            # IBM Qiskit policy
│   ├── cirq_policy.py              # Google Cirq policy
│   ├── pulser_policy.py            # Pasqal Pulser policy
│   ├── pennylane_policy.py         # Xanadu PennyLane policy
├── utils/
│   ├── __init__.py
│   ├── policy_comparator.py        # RL loop to evaluate and compare policies
├── main.py                         # Main entry point for the project
```
---

## **Features**
1. **Environment**:
   - Simulates a smart building with state variables:
     - **Temperature**
     - **Energy Usage**
     - **Light Intensity**
   - Provides rewards based on energy efficiency.

2. **Quantum Policies**:
   - **IBM Qiskit**: Parameterized quantum circuit for action selection.
   - **Google Cirq**: Quantum circuit using symbolic parameters for policy evaluation.
   - **Pasqal Pulser**: Pulse-based decision-making for neutral atom processors.
   - **Xanadu PennyLane**: Hybrid quantum-classical policy integrated with QNodes.

3. **Policy Comparator**:
   - Compares total rewards of all policies.
   - Identifies the best-performing policy.

---

## **Installation**

### **Prerequisites**
- Python 3.11 or higher
- pip

### **Required Libraries**
Install the required libraries:
```bash
pip install -r requirements.txt
