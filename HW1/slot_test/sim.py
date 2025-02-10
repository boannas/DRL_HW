import matplotlib.pyplot as plt
from tesa import simulate_slots
num_machines = 3
win_probs = [0.1, 0.05, 0.006]  
num_plays = 500  

results, history = simulate_slots(num_machines, win_probs, num_plays)

for i in range(num_machines):
    print(f"Machine {i+1}: Wins={results[i][0]}, Plays={results[i][1]}, Win Rate={results[i][0]/results[i][1]:.2f}")

plt.figure(figsize=(10, 6))
for i in range(num_machines):
    plt.plot(history[i], label=f"Machine {i+1} (p={win_probs[i]})")

plt.xlabel("Plays")
plt.ylabel("Win Rate")
plt.title("Slot Machine Simulation")
plt.legend()
plt.show()
