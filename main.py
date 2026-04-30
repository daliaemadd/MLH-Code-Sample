from z3 import *

def solve_puzzle(name, solver):
    print(f"--- {name} ---")
    # result = s.check() returns sat or unsat
    if solver.check() == sat:
        m = solver.model()
        print(m)
    else:
        print("No solution exists")
    print()

# =================================================================
# PUZZLE 1 
# =================================================================
# Ted: "Of the two of us, exactly one is a knight."
# Zippy: "Ted is a knave."
# Logic: 
# Ted (T) is a knight iff (T is Knight AND Zippy is Knave) OR (T is Knave AND Zippy is Knight)
# Zippy (Z) is a knight iff Ted is NOT a knight
# T <=> ((T ^ !Z) v (!T ^ Z))
# Z <=> !T
# =================================================================
t_s = Solver()
T, Z = Bools('Ted Zippy')
t_s.add(T == Or(And(T, Not(Z)), And(Not(T), Z))) # Biconditional X <=> S
t_s.add(Z == Not(T))
solve_puzzle("Puzzle 1", t_s)

# =================================================================
# PUZZLE 2 
# =================================================================
# B: Carl is knave ^ Sue is knight  => B <=> (!C ^ S)
# M: Betty is knight ^ Homer is knave => M <=> (B ^ !H)
# H: Sue is knight ^ Marge is knave => H <=> (S ^ !M)
# C: Homer and Betty are knaves => C <=> (!H ^ !B)
# S: Neither Carl nor Homer is a knave => S <=> (C ^ H)
# =================================================================
m_s = Solver()
B, M, H, C, S = Bools('Betty Marge Homer Carl Sue')
m_s.add(B == And(Not(C), S))
m_s.add(M == And(B, Not(H)))
m_s.add(H == And(S, Not(M)))
m_s.add(C == And(Not(H), Not(B)))
m_s.add(S == And(C, H))
solve_puzzle("Puzzle 2", m_s)

# =================================================================
# PUZZLE 3 
# =================================================================
# Peggy (P): Alice is knight ^ Bozo is knave => P <=> (A ^ !Bo)
# Mel (M): "Peggy could say Joe is a knight" => M <=> (P <=> J)
# Betty (B): "Alice could claim Betty is a knave" => B <=> (A <=> !B)
# Bozo (Bo): Peggy is knave v Joe is knave => Bo <=> (!P v !J)
# Bart (Ba): "Only a knave would say Joe is a knave" => Ba <=> J
# Joe (J): Neither Betty nor Alice is knight => J <=> (!B ^ !A)
# Sally (S): "Alice would tell you Mel is a knight" => S <=> (A <=> Mel)
# Alice (A): "It is false that Sally is a knave" => A <=> S
# =================================================================
e_s = Solver()
P, Mel, B, Bo, Ba, J, Sal, A = Bools('Peggy Mel Betty Bozo Bart Joe Sally Alice')
e_s.add(P == And(A, Not(Bo)))
e_s.add(Mel == (P == J))       # "could say" hint
e_s.add(B == (A == Not(B)))    # "could claim" hint
e_s.add(Bo == Or(Not(P), Not(J)))
e_s.add(Ba == J)               # "Only a knave would say..." hint
e_s.add(J == And(Not(B), Not(A)))
e_s.add(Sal == (A == Mel))     
e_s.add(A == Sal)              
solve_puzzle("Puzzle 3", e_s)

# =================================================================
# CHALLENGE PUZZLE
# =================================================================
# Xavier: "If Yara is a knight, then Zane could say that I am a knave."
# Yara: "Zane and Xavier are the same type."
# Zane: "Only a knave would say that Xavier and Yara are both knights."
# Logic:
# X <=> (Y => (Z <=> !X))
# Y <=> (X <=> Z)
# Z <=> !(X ^ Y)
# =================================================================
c_s = Solver()
X, Y, Zane = Bools('Xavier Yara Zane')
c_s.add(X == Implies(Y, (Zane == Not(X)))) 
c_s.add(Y == (X == Zane))
c_s.add(Zane == Not(And(X, Y)))
solve_puzzle("Challenge Puzzle", c_s)
