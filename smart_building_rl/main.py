from environment.smart_building_env import SmartBuildingEnv
from policies.qiskit_policy import QiskitPolicy
from policies.cirq_policy import CirqPolicy
from policies.pulser_policy import PulserPolicy
from policies.pennylane_policy import PennyLanePolicy
from utils.policy_comparator import compare_policies

def main():
    env = SmartBuildingEnv()
    policies = {
        "Qiskit": QiskitPolicy(),
        "Cirq": CirqPolicy(),
        "Pulser": PulserPolicy(),
        "PennyLane": PennyLanePolicy(),
    }

    results, best_policy = compare_policies(env, policies)

    print("\nResults:")
    for policy_name, reward in results.items():
        print(f"{policy_name}: Total Reward = {reward}")

    print(f"\nBest Policy: {best_policy} with Reward: {results[best_policy]}")

if __name__ == "__main__":
    main()
