from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

class Oracle:
  def __init__(self,lang, alphabet):
    self.lang = lang
    self.alphabet = alphabet
    self.representation = DFA.from_nfa(NFA.from_regex(lang, input_symbols=alphabet))

  def membership(self, word):
    return self.representation.accepts_input(word)

  def equivalence(self, dfa):
    return self.representation == dfa

class ObservationTable:
  def __init__(self, alphabet, states, experiments, red, oracle : Oracle):
    self.states = states
    self.experiments = experiments
    self.red = red
    self.blue = [] # TODO
    self.alphabet = alphabet
    self.oracle = oracle

  def ot(self, u : str, e : str):
    return 1 if self.oracle.membership(u + e) else 0

  def is_complete(self):
    for state in self.states:
      for experiment in self.experiments:
        if self.ot(state, experiment) == 2:
          return False
    return True

  def equivalent_row(self, u, v):
    return all( self.ot(u, e) == self.ot(v, e) for e in self.experiments)

  def closed(self):
    for u in self.blue:
      found = False
      for v in self.red:
        found = self.equivalent_row(u,v)
        if found:
          break
      if not found:
        return False
    return True

  def close(self):
    # close table: promote u ∈ BLUE to RED and add all ua to BLUE ,
    # iterate
    return None

  def consistent(self):
    for u in self.red:
        for v in self.red:
          for a in self.alphabet:
            if self.equivalent_row(u, v):
              if not self.equivalent_row(u + a, v + a):
                return False
    return True

  def to_consistent(self):
    # Make table consistent: add ae to EXP if e separates ua and va
    return None

  def build(self) -> DFA :
    tr = dict()

    for s in self.states:
      tr[s] = { a : s + a for a in self.alphabet if self.equivalent_row(s, s + a) }

    return DFA(
    states=set(self.states),
    input_symbols=set(self.alphabet),
    transitions=tr,
    initial_state='',
    final_states= { y for y in self.states if self.ot(y, '') == 1 }
    )



