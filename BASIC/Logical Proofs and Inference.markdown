# Propositional Logic

## Key Concepts
- **Propositions**: Statements that are either true (T) or false (F).
  - *Example*: "It is raining" (p), "The sun is shining" (q).
- **Logical Operators**:
  - **Conjunction (∧)**: `p ∧ q` is true if both `p` and `q` are true.
    - *Example*: "It is raining and the sun is shining" (`p ∧ q`).
  - **Disjunction (∨)**: `p ∨ q` is true if at least one of `p` or `q` is true.
    - *Example*: "It is raining or the sun is shining" (`p ∨ q`).
  - **Negation (¬)**: `¬p` is true if `p` is false.
    - *Example*: "It is not raining" (`¬p`).
  - **Implication (→)**: `p → q` is false only if `p` is true and `q` is false.
    - *Example*: "If it is raining, then I will stay inside" (`p → q`).
  - **Biconditional (↔)**: `p ↔ q` is true if `p` and `q` have the same truth value.
    - *Example*: "I will go out if and only if it is sunny" (`p ↔ q`).
- **Compound Propositions**: Combine propositions using logical operators.
  - *Example*: "It is raining and either the sun is shining or it is cold" (`p ∧ (q ∨ ¬r)`).
- **Precedence of Logical Operators**: `¬` > `∧` > `∨` > `→` > `↔`.

## Implication and Related Forms
- **Implication**: `p → q` (if p, then q).
- **Converse**: `q → p`.
- **Contrapositive**: `¬q → ¬p` (logically equivalent to `p → q`).
- **Inverse**: `¬p → ¬q`.
  - *Example*: For `p → q`: "If it is raining, then I will stay inside."
    - Converse: "If I stay inside, then it is raining."
    - Contrapositive: "If I don’t stay inside, then it is not raining."
    - Inverse: "If it is not raining, then I won’t stay inside."
- **Implicit Use of Biconditionals**: `p ↔ q` means `(p → q) ∧ (q → p)`.
  - *Example*: "I will go out if and only if it is sunny" is equivalent to "If it is sunny, I will go out, and if I go out, it is sunny."

## Logic and Bit Operations
- Logical operations correspond to bit operations:
  - `∧`: Bitwise AND (`1 ∧ 1 = 1`, else `0`).
  - `∨`: Bitwise OR (`0 ∨ 0 = 0`, else `1`).
  - `¬`: Bitwise NOT (flips `0` to `1`, `1` to `0`).
  - *Example*: For bits `a = 1`, `b = 0`:
    - `a ∧ b = 1 ∧ 0 = 0`
    - `a ∨ b = 1 ∨ 0 = 1`
    - `¬a = ¬1 = 0`

## Example: Boolean Search on Webpage
- **Search query**: "cats AND dogs NOT birds".
  - **Translation**: Find pages with "cats" AND "dogs" but NOT "birds".
  - **Logic**: `p ∧ q ∧ ¬r`, where `p = "cats"`, `q = "dogs"`, `r = "birds"`.
  - **Implementation**: Search engine returns pages where `p` and `q` are true, and `r` is false.
  - *Example*: A webpage with "cats" and "dogs" but no mention of "birds" satisfies the query.

# Propositional Equivalences

## Logical Equivalences
- **Identity Laws**:
  - `p ∧ T ≡ p`
  - `p ∨ F ≡ p`
  - *Example*: "It is raining ∧ True" ≡ "It is raining."
- **Domination Laws**:
  - `p ∨ T ≡ T`
  - `p ∧ F ≡ F`
  - *Example*: "It is raining ∨ True" ≡ True.
- **Idempotent Laws**:
  - `p ∨ p ≡ p`
  - `p ∧ p ≡ p`
  - *Example*: "It is raining ∨ It is raining" ≡ "It is raining."
- **Double Negation Law**:
  - `¬(¬p) ≡ p`
  - *Example*: `¬(¬"It is raining")` ≡ "It is raining."
- **Commutative Laws**:
  - `p ∨ q ≡ q ∨ p`
  - `p ∧ q ≡ q ∧ p`
  - *Example*: "It is raining ∨ It is sunny" ≡ "It is sunny ∨ It is raining."
- **Associative Laws**:
  - `(p ∨ q) ∨ r ≡ p ∨ (q ∨ r)`
  - `(p ∧ q) ∧ r ≡ p ∧ (q ∧ r)`
  - *Example*: `(p ∧ q) ∧ r ≡ p ∧ (q ∧ r)` for "It is raining ∧ It is sunny ∧ It is cold."
- **Distributive Laws**:
  - `p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)`
  - `p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)`
  - *Example*: `p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)` for `p = "It is raining"`, `q = "It is sunny"`, `r = "It is cold"`.
- **De Morgan’s Laws**:
  - `¬(p ∧ q) ≡ ¬p ∨ ¬q`
  - `¬(p ∨ q) ≡ ¬p ∧ ¬q`
  - *Example*: `¬(p ∧ q) ≡ ¬p ∨ ¬q` for "It is not both raining and sunny" ≡ "It is not raining or it is not sunny."
- **Absorption Laws**:
  - `p ∨ (p ∧ q) ≡ p`
  - `p ∧ (p ∨ q) ≡ p`
  - *Example*: `p ∨ (p ∧ q) ≡ p` for "It is raining ∨ (It is raining ∧ It is sunny)" ≡ "It is raining."
- **Negation Laws**:
  - `p ∨ ¬p ≡ T`
  - `p ∧ ¬p ≡ F`
  - *Example*: "It is raining ∨ It is not raining" ≡ True.

## Equivalences Involving Conditionals
- `p → q ≡ ¬p ∨ q`
  - *Example*: "If it is raining, then I stay inside" ≡ "It is not raining or I stay inside."
- `p → q ≡ ¬q → ¬p` (contrapositive)
  - *Example*: "If it is raining, then I stay inside" ≡ "If I don’t stay inside, then it is not raining."
- `p ∨ q ≡ ¬p → q`
- `¬(p → q) ≡ p ∧ ¬q`
  - *Example*: `¬(p → q) ≡ p ∧ ¬q` for "It is raining and I don’t stay inside."
- `(p → q) ∧ (p → r) ≡ p → (q ∧ r)`
- `(p → r) ∧ (q → r) ≡ (p ∨ q) → r`
- `(p → q) ∨ (p → r) ≡ p → (q ∨ r)`

## Equivalences Involving Biconditionals
- `p ↔ q ≡ (p → q) ∧ (q → p)`
  - *Example*: "I go out if and only if it is sunny" ≡ `(p → q) ∧ (q → p)`.
- `p ↔ q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)`
- `¬(p ↔ q) ≡ p ↔ ¬q`

## Constructing New Logical Equivalences
- Use known equivalences to rewrite expressions.
  - *Example*: Prove `¬(p ∧ q) ∨ (p ∨ q) ≡ T`:
    - `¬(p ∧ q) ≡ ¬p ∨ ¬q` (De Morgan’s).
    - `¬p ∨ ¬q ∨ p ∨ q ≡ (¬p ∨ p) ∨ (¬q ∨ q) ≡ T ∨ T ≡ T`.

## Propositional Satisfiability
- A proposition is satisfiable if there exists an assignment of truth values that makes it true.
- **Example: Sudoku Solver**:
  - Represent Sudoku constraints as propositions (e.g., `P(i,j,k)`: "cell (i,j) has value k").
  - Use logical equivalences to ensure:
    - Each cell has exactly one value: `P(i,j,k) ∧ ¬P(i,j,m)` for `k ≠ m`.
    - Each row/column/subgrid has unique values.
  - Solve using satisfiability algorithms (e.g., backtracking or SAT solvers).

# Predicates and Quantifiers

## Predicates
- A predicate `P(x)` is a statement that becomes true or false when a value is assigned to `x`.
  - *Example*: `P(x)`: "x > 3" is true for `x = 4`, false for `x = 2`.
- Predicates can involve multiple variables.
  - *Example*: `P(x, y)`: "x + y = 5" is true for `x = 2`, `y = 3`.

## Quantifiers
- **Universal Quantifier (∀)**: `∀x P(x)` means "P(x) is true for all x in the domain."
  - *Example*: `∀x (x² ≥ 0)` means "For all x, x² is non-negative."
- **Existential Quantifier (∃)**: `∃x P(x)` means "There exists an x such that P(x) is true."
  - *Example*: `∃x (x² = 4)` means "There exists an x such that x² = 4."
- **Restricted Domains**: Quantifiers can be restricted.
  - *Example*: `∀x > 0 P(x)` means "for all x > 0, P(x) is true."

## Precedence and Binding
- Quantifiers have higher precedence than logical operators.
- Variables are bound by quantifiers; unbound variables are free.
  - *Example*: In `∀x (P(x) ∧ Q(y))`, `x` is bound, `y` is free.

## Logical Equivalences Involving Quantifiers
- `¬∀x P(x) ≡ ∃x ¬P(x)`
  - *Example*: `¬∀x (x > 0) ≡ ∃x (x ≤ 0)`.
- `¬∃x P(x) ≡ ∀x ¬P(x)`
  - *Example*: `¬∃x (x² = -1) ≡ ∀x (x² ≠ -1)`.
- When is `¬∃x P(x)` true?: When `P(x)` is false for all `x` (i.e., no `x` makes `P(x)` true).
- When is `¬∀x P(x)` true?: When there exists an `x` such that `P(x)` is false.

## Translating English to Logical Expressions
- *Example*: "All lions are fierce" → `∀x (L(x) → F(x))`, where `L(x)` = "x is a lion," `F(x)` = "x is fierce."
- **Example from Lewis Carroll**:
  - Premises:
    - "All lions are fierce" (`∀x (L(x) → F(x))`).
    - "Some lions do not drink coffee" (`∃x (L(x) ∧ ¬C(x))`).
  - Conclusion: "Some fierce creatures do not drink coffee" (`∃x (F(x) ∧ ¬C(x))`).

## Logic Programming (Prolog)
- **Prolog Facts**: Define predicates.
  - *Example*: `lion(simba).` means Simba is a lion.
- **Prolog Rules**: Define new predicates using facts.
  - *Example*: `fierce(X) :- lion(X).` means if X is a lion, X is fierce.
- *Example*: Given `lion(simba).` and `fierce(X) :- lion(X).`, Prolog infers `fierce(simba)`.

# Nested Quantifiers

## Understanding Nested Quantifiers
- Nested quantifiers involve multiple variables.
  - *Example*: `∀x∃y P(x, y)` means "For every x, there exists a y such that P(x, y) is true."
- **Order Matters**:
  - `∀x∀y P(x, y)`: `P(x, y)` is true for every pair `(x, y)`.
    - *Example*: `∀x∀y (x + y = y + x)` is true for all real numbers `x`, `y`.
  - `∃x∀y P(x, y)`: There exists an `x` such that `P(x, y)` is true for all `y`.
    - *Example*: `∃x∀y (x + y = y)` is true for `x = 0`.
  - `∀x∃y P(x, y)`: For every `x`, there exists a `y` such that `P(x, y)` is true.
    - *Example*: `∀x∃y (x + y = 0)` is true for `y = -x`.
  - `∃x∃y P(x, y)`: There exists a pair `(x, y)` such that `P(x, y)` is true.
    - *Example*: `∃x∃y (x + y = 5)` is true for `x = 2`, `y = 3`.

## Translating Mathematical Statements
- *Example*: "For every real number x, there exists a real number y such that x + y = 0" → `∀x∃y (x + y = 0)`.
- **English to Logic**: "Every student has a favorite course" → `∀x∃y (S(x) → F(x, y))`, where `S(x)` = "x is a student," `F(x, y)` = "y is x’s favorite course."

## Negating Nested Quantifiers
- Apply De Morgan’s laws iteratively:
  - `¬∀x∀y P(x, y) ≡ ∃x∃y ¬P(x, y)`.
    - *Example*: `¬∀x∀y (x + y = 0) ≡ ∃x∃y (x + y ≠ 0)`.
  - `¬∃x∀y P(x, y) ≡ ∀x∃y ¬P(x, y)`.
    - *Example*: `¬∃x∀y (x + y = y) ≡ ∀x∃y (x + y ≠ y)`.

# Rules of Inference

## Valid Arguments in Propositional Logic
- An argument is valid if the conclusion follows from the premises using rules of inference.

## Key Rules of Inference
- **Modus Ponens**: `p, p → q ⊢ q`.
  - *Example*: "It is raining," "If it is raining, I stay inside" ⊢ "I stay inside."
- **Modus Tollens**: `¬q, p → q ⊢ ¬p`.
  - *Example*: "I don’t stay inside," "If it is raining, I stay inside" ⊢ "It is not raining."
- **Hypothetical Syllogism**: `p → q, q → r ⊢ p → r`.
  - *Example*: "If it is raining, I stay inside," "If I stay inside, I read" ⊢ "If it is raining, I read."
- **Disjunctive Syllogism**: `p ∨ q, ¬p ⊢ q`.
  - *Example*: "It is raining or sunny," "It is not raining" ⊢ "It is sunny."
- **Addition**: `p ⊢ p ∨ q`.
  - *Example*: "It is raining" ⊢ "It is raining or sunny."
- **Simplification**: `p ∧ q ⊢ p`.
  - *Example*: "It is raining and sunny" ⊢ "It is raining."
- **Conjunction**: `p, q ⊢ p ∧ q`.
  - *Example*: "It is raining," "It is sunny" ⊢ "It is raining and sunny."
- **Resolution**: `p ∨ q, ¬p ∨ r ⊢ q ∨ r`.

## Example: Argument Analysis
- **Premises**:
  - "It is not sunny and it is colder than yesterday" (`¬p ∧ q`).
  - "We will go swimming only if it is sunny" (`r → p`).
  - "If we do not go swimming, we will take a canoe trip" (`¬r → s`).
  - "If we take a canoe trip, we will be home by sunset" (`s → t`).
- **Conclusion**: "We will be home by sunset" (`t`).
- **Proof**:
  1. `¬p ∧ q` (Premise).
  2. `¬p` (Simplification).
  3. `r → p` (Premise).
  4. `¬r` (Modus Tollens: 2, 3).
  5. `¬r → s` (Premise).
  6. `s` (Modus Ponens: 4, 5).
  7. `s → t` (Premise).
  8. `t` (Modus Ponens: 6, 7).

## Fallacies
- Common errors:
  - **Affirming the consequent**: `p → q, q ⊢ p` (invalid).
    - *Example*: "If it is raining, I stay inside," "I stay inside" ⊢ "It is raining" (invalid).
  - **Denying the antecedent**: `p → q, ¬p ⊢ ¬q` (invalid).
    - *Example*: "If it is raining, I stay inside," "It is not raining" ⊢ "I don’t stay inside" (invalid).

# Introduction to Proofs

## Methods of Proving Theorems
- **Direct Proof**: Assume `p` is true, show `q` is true (for `p → q`).
  - *Example*: Prove "If n is odd, then n² is odd." Assume `n` is odd (`n = 2k + 1`), then `n² = (2k + 1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1`, which is odd.
- **Proof by Contraposition**: Prove `¬q → ¬p` instead of `p → q`.
  - *Example*: For "If n² is odd, then n is odd," prove "If n is even, then n² is even."
- **Vacuous Proof**: If `p` is always false, `p → q` is true.
  - *Example*: If `0 = 1`, then pigs fly (true because `0 ≠ 1`).
- **Trivial Proof**: If `q` is always true, `p → q` is true.
  - *Example*: If `n` is even, then `1 + 1 = 2` (true because `1 + 1 = 2` always).
- **Proof by Contradiction**: Assume the negation of the conclusion, derive a contradiction.
  - *Example*: Prove √2 is irrational. Assume `√2 = a/b` (`a`, `b` integers, `b ≠ 0`, coprime). Then `2 = a²/b²`, so `a² = 2b²`. Thus, `a` is even (`a = 2k`), so `4k² = 2b²`, `b² = 2k²`, `b` is even. Contradiction: `a`, `b` not coprime.
- **Proofs of Equivalence**: Show `p ↔ q` by proving `p → q` and `q → p`.
  - *Example*: Prove `n` is even ↔ `n²` is even by proving both directions.

## Mistakes in Proofs
- *Example*: "Proof" that `1 = 2`:
  - Steps:
    1. `a = b` (Given).
    2. `a² = ab` (Multiply by `a`).
    3. `a² − b² = ab − b²` (Subtract `b²`).
    4. `(a − b)(a + b) = b(a − b)` (Factor).
    5. `a + b = b` (Divide by `a − b`).
    6. `2b = b` (Since `a = b`).
    7. `2 = 1` (Divide by `b`).
  - **Error**: Division by `a − b` in step 5 is invalid since `a = b` implies `a − b = 0`.

## Mathematical Induction
- Prove a statement `P(n)` for all integers `n ≥ n₀`:
  - **Base Case**: Prove `P(n₀)` is true.
  - **Inductive Step**: Assume `P(k)` is true (inductive hypothesis), prove `P(k + 1)`.
- *Example*: Prove `∑(i=1 to n) i = n(n+1)/2` for `n ≥ 1`.
  - **Base Case**: For `n = 1`, `∑i = 1 = 1(1+1)/2 = 1` (true).
  - **Inductive Step**: Assume `∑(i=1 to k) i = k(k+1)/2`. Prove for `k + 1`:
    - `∑(i=1 to k+1) i = ∑(i=1 to k) i + (k+1) = k(k+1)/2 + (k+1) = (k+1)(k+2)/2`.

## Combinatorial Proofs
- Prove identities by counting the same set in two different ways.
- *Example*: Prove `(n choose k) = (n choose n−k)`:
  - Left: Number of ways to choose `k` items from `n`.
  - Right: Number of ways to choose `n−k` items from `n` (equivalent to choosing `k` items to exclude).