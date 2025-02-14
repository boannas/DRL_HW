import numpy as np

class SlotMachine:
    def __init__(self, win_prob):
        self.win_prob = win_prob
        self.wins = 0
        self.plays = 0

    def play(self):
        self.plays += 1
        if np.random.rand() < self.win_prob:
            self.wins += 1
            return 1  # Win
        return 0  # Lose

def simulate_slots(num_machines, win_probs, num_plays):
    machines = [SlotMachine(win_probs[i]) for i in range(num_machines)]
    history = {i: [] for i in range(num_machines)}

    for _ in range(num_plays):
        for i, machine in enumerate(machines):
            outcome = machine.play()
            history[i].append(machine.wins / machine.plays if machine.plays > 0 else 0)
    
    results = {i: (machines[i].wins, machines[i].plays) for i in range(num_machines)}
    return results, history

