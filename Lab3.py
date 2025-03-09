class Automaton:
    def __init__(self):
        self.states = {"q0", "q1", "q2", "q3", "q4"}
        self.alphabet = {"C", "T", "A", "H", "OK"}
        self.transitions = {
            ("q0", "C"): "q1",
            ("q0", "T"): "q2",
            ("q0", "A"): "q3",
            ("q0", "H"): "q4",
            ("q1", "OK"): "q0",
            ("q2", "OK"): "q0",
            ("q3", "OK"): "q0",
            ("q4", "OK"): "q0",
        }
        self.initial_state = "q0"
        self.final_state = "q4"
        self.current_state = self.initial_state
    
    def transition(self, input_symbol):
        if (self.current_state, input_symbol) in self.transitions:
            self.current_state = self.transitions[(self.current_state, input_symbol)]
            return True
        return False
    
    def run(self):
        print("Automatul a pornit. Selectați o băutură: C (cafea), T (ceai), A (cappuccino), H (ciocolată caldă)")
        while True:
            user_input = input("Introduceți simbolul: ").upper()
            if user_input not in self.alphabet:
                print("Simbol invalid. Încercați din nou.")
                continue
            
            if self.transition(user_input):
                print(f"Tranziție efectuată: stare curentă -> {self.current_state}")
                if self.current_state == "q0":
                    print("Puteți selecta o altă băutură.")
            else:
                print("Tranziție invalidă, încercați din nou.")

if __name__ == "__main__":
    automat = Automaton()
    automat.run()
