class MooreMachine:
    def __init__(self):
        self.states = {
            "S1": "O1",
            "S2": "O2"
        }
        self.transitions = {
            ("S1", "A"): "S1",
            ("S1", "B"): "S2",
            ("S2", "A"): "S1",
            ("S2", "B"): "S2"
        }
        self.current_state = "S1"

    def process_input(self, inputs):
        output_sequence = []
        for inp in inputs:
            self.current_state = self.transitions.get((self.current_state, inp), self.current_state)
            output_sequence.append(self.states[self.current_state])
        return output_sequence

moore_machine = MooreMachine()
inputs = ["A", "B", "A", "B", "A", "A"]
outputs = moore_machine.process_input(inputs)

print("Input:", inputs)
print("Output:", outputs)
