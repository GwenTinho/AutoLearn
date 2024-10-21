import string
from automata.fa.nfa import NFA

def is_subset(nfa1, nfa2):
    # In the following, we have nfa1 and nfa2 and want to determine whether
    # nfa1 is a subset of nfa2.

    # If taking the union of nfa2 with nfa1 is equal to nfa2 again,
    # nfa1 didn't accept any strings that nfa2 did not, so it is a subset.
    return nfa1.union(nfa2) == nfa2

alphabet = set(string.ascii_lowercase)

nfa1 = NFA.from_regex("abc", input_symbols=alphabet)
nfa2 = NFA.from_regex("(abc)|(def)", input_symbols=alphabet)
nfa3 = NFA.from_regex("a*bc", input_symbols=alphabet)

print(is_subset(nfa1, nfa2))  # True
print(is_subset(nfa1, nfa3))  # True
print(is_subset(nfa2, nfa3))  # False


from automata.fa.dfa import DFA

# DFA which matches all binary strings ending in an odd number of '1's
my_dfa = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)

my_dfa.show_diagram()
