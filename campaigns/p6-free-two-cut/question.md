# 3P2-free 2-Cut → P6-free 2-Cut

Category: Complexity open

## Source

The source is a connected graph containing no induced disjoint union of three edges. Its outputs are nontrivial cuts with crossing degree at most two, or NO-SOLUTION.

## Target

Both endpoints are connected simple graphs and seek a nontrivial bipartition with at most two opposite neighbors per vertex. The source excludes three disjoint induced edges; the target excludes an induced six-vertex path.

## Required result

Construct deterministic polynomial-time maps F and G: F sends every legal source instance to a legal target instance, and G(x,y) is a valid source output for every valid output y of F(x). Preserve the stated threshold, domain and promises. The requested complexity conclusion is NP-hardness for the stated target problem.

## Acceptance

Give explicit construction and recovery algorithms, a general proof for every legal input and every valid target output, and polynomial runtime and encoding-size bounds. Specify finite output encodings and handle NO-SOLUTION outputs when applicable. Tests compare recovered source outputs with independent source solutions.

## Why it matters

Together with P5-free tractability, hardness here would identify an exact forbidden-path boundary.

## Difficulty

Adding vertices cannot remove an existing induced P6; densification consumes crossing budgets and can destroy valid cuts.

## Literature context

The cited work gives P5-free tractability and asks about the next forbidden-path case. Probe-graph results concern a larger class and do not settle ordinary P6-free graphs.

Literature checked 2026-09-14. This summarizes the archived literature search on the date above. Unpublished, unindexed and overlooked work remains outside coverage; no new novelty assessment was performed.

## References

- [Finding d-Cuts in Graphs of Bounded Diameter, Graphs of Bounded Radius and H-Free Graphs](https://eprints.cs.univie.ac.at/8514/1/Finding_d_cuts_in_Graphs_ALGORITMICA.pdf): - R1: Finding d-Cuts in Graphs of Bounded Diameter, Graphs of Bounded Radius and H-Free Graphs, Algorithmica 88:7 (2026), Theorems 5 and 13, Section 5, PDF page 25. - R11: Finding d-Cuts in Probe H-Free Graphs, May 2025, Theorem 1.1 on ordinary graphs versus the probe-class results.
- [Finding d-Cuts in Probe H-Free Graphs](https://arxiv.org/html/2505.22351): - R1: Finding d-Cuts in Graphs of Bounded Diameter, Graphs of Bounded Radius and H-Free Graphs, Algorithmica 88:7 (2026), Theorems 5 and 13, Section 5, PDF page 25. - R11: Finding d-Cuts in Probe H-Free Graphs, May 2025, Theorem 1.1 on ordinary graphs versus the probe-class results.

Fixed from board record `website/questions/p6-free-two-cut.json` in board checkout at 6c7d3bd9c0a8f595279969a9c0a4d1853a3f5c17; the record was copied from the current working tree.
