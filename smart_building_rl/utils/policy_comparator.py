def compare_policies(env, policies):
    results = {}

    for policy_name, policy in policies.items():
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = policy.evaluate(state)
            next_state, reward, done = env.step(action)
            total_reward += reward
            state = next_state

        results[policy_name] = total_reward

    best_policy = max(results, key=results.get)
    return results, best_policy
