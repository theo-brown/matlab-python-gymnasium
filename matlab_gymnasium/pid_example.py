import matplotlib.pyplot as plt
import numpy as np

from matlab_gymnasium import MountainCarWrapper


class PID:
    def __init__(self, kp, ki, kd, integral_limit=np.inf):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral_limit = integral_limit
        self.error_sum = 0
        self.prev_error = 0

    def value(self, target, current):
        error = current - target
        self.error_sum = float(
            np.clip(
                self.error_sum + error,
                -self.integral_limit,
                self.integral_limit,
            )
        )
        error_diff = error - self.prev_error
        self.prev_error = error
        return np.atleast_1d(
            self.kp * error + self.ki * self.error_sum + self.kd * error_diff
        )

    def reset(self):
        self.error_sum = 0
        self.prev_error = 0


env = MountainCarWrapper()

pid = PID(kp=1, ki=1, kd=1, integral_limit=100)

observation = env.reset()
terminated = False
truncated = False

observations = []
rewards = []
max_steps = 1000

print("Running episode...")
for i in range(max_steps):
    action = pid.value(target=env.goal_position, current=observation[0])
    observation, reward, terminated, truncated, info = env.step(action)
    observations.append(observation)
    rewards.append(reward)

    if terminated or truncated:
        break

# Plot results
print("Plotting results...")
fig, axs = plt.subplots(1, 3)

axs[0].plot(np.array(observations)[:, 0])
axs[0].set_title("Position")

axs[1].plot(np.array(observations)[:, 1])
axs[1].set_title("Velocity")

axs[2].plot(np.cumsum(rewards))
axs[2].set_title("Cumulative reward")

plt.show()
