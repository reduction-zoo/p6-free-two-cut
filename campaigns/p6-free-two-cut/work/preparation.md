# Preparation evidence

Prepared on 2026-09-26 before construction. The fixed corpus has 112
distinct legal connected 3P2-free graphs: 12 hand-labelled edge cases and
100 seeded random cases, with 70 YES and 42 NO decisions and one to eight
vertices. `generate_cases.py` retains the generator and seeds; `cases.json`
stores checked cuts or NO-SOLUTION. Source legality is checked by testing
every triple of disjoint graph edges for the required induced six-vertex
matching. Z3 4.16.0 assigns one Boolean side per vertex, requires both
sides nonempty, and bounds each crossing degree by two. Returned cuts are
checked by direct neighbor counting; UNSAT is conclusive and unknown is
an error. Exhaustive side assignments agreed on all 112 source cases.

The target promise is checked by growing induced paths while excluding
chords. The same Z3 cut encoding is used, with target legality checked
separately. Independent exhaustive side assignments agreed with Z3 on
111 distinct P6-free connected target graphs with up to eight vertices.
Hand fixtures cover YES on K4, NO on K5, a source-legal path that violates
the target P6 promise, a disconnected illegal graph and an invalid cut.

Reproduce from the repository root:

```sh
uv sync --locked
uv run --locked python campaigns/p6-free-two-cut/work/check.py --self-test
```

The self-test starts with the corpus gate, regenerates seeded graphs,
rechecks source labels and witnesses, and compares target decisions to
exhaustive enumeration. The candidate runner uses separate forward and
recovery subprocesses and up to three target cuts per source. An incorrect
injected candidate was rejected after target solving and source validation.
No actual reduction candidate exists; finite checks do not establish
hardness or a general reduction.
