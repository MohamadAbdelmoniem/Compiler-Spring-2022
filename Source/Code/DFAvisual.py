from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

dfa = VisualDFA(
    states={"stmt-seq", "statement", "assign-stmt", "if-stmt", "if", "number", "then", "end", "identifier", "factor", ":=", "number", ";"},
    input_symbols={"0","if","number","then","stmt-seq","end","statement","assign-stmt","identifier"}, #alphabets
    transitions={
        "stmt-seq": {"0": "statement"},
        "q1": {"0": "q3"},
        "q2": {"0": "q3"},
        "q3": {"0": "q4", "1": "q1"},
        "q4": {"0": "q4", "1": "q1"},
    },
    initial_state="stmt-seq",

)

dfa.show_diagram("1000" , view=True)
#minimal_dfa = VisualDFA.minify(dfa)   #method to optimize dfa
#minimal_dfa.show_diagram(view=True)
