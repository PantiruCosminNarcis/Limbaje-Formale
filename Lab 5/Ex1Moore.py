class TrafficLightMoore:
    def __init__(self):
        self.state = "S0"
        self.output = {"S0": 1, "S1": 0}

    def transition(self, A, B):
        transitions = {
            "S0": {(0, 0): "S0", (0, 1): "S1", (1, 0): "S1", (1, 1): "S1"},
            "S1": {(0, 0): "S0", (0, 1): "S1", (1, 0): "S1", (1, 1): "S1"}
        }

        if (A, B) in transitions[self.state]:
            self.state = transitions[self.state][(A, B)]
        return self.output[self.state]

# Testare
automaton = TrafficLightMoore()
inputs = [(0, 0), (0, 1), (1, 0), (1, 1), (0, 0)]
for A, B in inputs:
    print(f"Intrare: {(A, B)}, Iesire: {automaton.transition(A, B)}, Stare: {automaton.state}")
