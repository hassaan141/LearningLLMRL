# plot.py
# Plot reward over training steps.
# A rising curve = the LLM is learning.

import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

with open("reward_log.json") as f:
    rewards = json.load(f)

# Smooth the curve for readability
def smooth(values, window=5):
    if len(values) < window:
        return values
    kernel = np.ones(window) / window
    return np.convolve(values, kernel, mode='valid')

steps = list(range(len(rewards)))
smoothed = smooth(rewards)

fig, ax = plt.subplots(figsize=(10, 5))

# Raw rewards
ax.plot(steps, rewards, alpha=0.3, color='#4A9EFF', linewidth=1, label='Raw reward')

# Smoothed
smooth_steps = list(range(len(smoothed)))
ax.plot(smooth_steps, smoothed, color='#4A9EFF', linewidth=2.5, label='Smoothed reward')

# Reference lines
ax.axhline(y=1.0, color='green', linestyle='--', alpha=0.4, label='Perfect (1.0)')
ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.3, label='Random baseline (0.5)')

ax.set_xlabel("Training Step", fontsize=12)
ax.set_ylabel("Average Reward (0=fail, 1=pass)", fontsize=12)
ax.set_title("RLVR Training: LLM Learning to Answer ML Questions\n(Reward should trend upward as model improves)", fontsize=13)
ax.legend()
ax.set_ylim(0, 1.1)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.1f}'))

plt.tight_layout()
plt.savefig("reward_curve.png", dpi=150)
print("Plot saved to reward_curve.png")
plt.show()
