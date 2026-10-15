import Challenge
open P6FreeTwoCut
example : legalSource ⟨6, [(0,1),(1,2),(2,3),(3,4),(4,5)]⟩ = true := by native_decide
example : legalTarget ⟨6, [(0,1),(1,2),(2,3),(3,4),(4,5)]⟩ = false := by native_decide
