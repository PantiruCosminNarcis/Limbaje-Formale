class MealyMachine:
    def __init__(self):
        self.transitions = {
            ("Q1", "X"): ("Q2", "O1"),
            ("Q1", "Y"): ("Q1", "O1"),
            ("Q2", "X"): ("Q1", "O2"),
            ("Q2", "Y"): ("Q2", "O2")
        }
        self.current_state = "Q1"

    def process_input(self, inputs):
        output_sequence = []
        for inp in inputs:
            if (self.current_state, inp) in self.transitions:
                next_state, output = self.transitions[(self.current_state, inp)]
                self.current_state = next_state
                output_sequence.append(output)
            else:
                output_sequence.append("Invalid")
        return output_sequence

mealy_machine = MealyMachine()
inputs = ["X", "Y", "X", "Y", "X"]
outputs = mealy_machine.process_input(inputs)

print("Input:", inputs)
print("Output:", outputs)
