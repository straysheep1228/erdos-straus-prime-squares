# The least denominator offset in the Erdős–Straus equation on prime squares

**Qichao Liu** · Research note · 26 November 2026

[English paper (PDF)](paper/manuscript.pdf) · [LaTeX source](paper/manuscript.tex) · [中文论文 (PDF)](paper/manuscript-zh.pdf) · [中文可编辑稿 (Word)](paper/manuscript-zh.docx)

For an odd prime $p$, how far above $p^2/4$ must one look to find the first denominator in a three-term unit-fraction decomposition of $4/p^2$? The note studies the offset $T(p)=4x-p^2$, where $x$ is the least first denominator among all ordered decompositions. Set $T(p)=\infty$ if there is no decomposition.

Form a single increasing sequence from the primes $q\equiv3\pmod4$ and the numbers $3q$ with $q$ prime and $q\equiv1\pmod4$. Theorem 1 gives the $j$-th term relative density $2^{-j}$ as a value of $T(p)$ among odd primes. For example, the first four terms are 3, 7, 11 and 15. Their densities are 1/2, 1/4, 1/8 and 1/16, respectively.

Proposition 3 is the main step. For each fixed candidate offset, it gives a necessary Jacobi-symbol condition and proves sufficiency outside a set of relative density zero in each admissible residue class. The paper also constructs progressions of primes with a prescribed first prime offset. Its results concern square inputs to the Erdős–Straus equation.

## Reproduce the finite calculation

From the repository root, run the following with Python 3.9 or later. The script uses the standard library.

```sh
python code/verify.py
```

The script applies the divisor criterion in Lemma 2 to all 1,217 primes in $41\le p<10{,}000$. For each prime it tests offsets in increasing order through 31. It also verifies the exact fraction identity for $p=43$ and the failed offset $t=19$ for $p=29$.

| First feasible offset | 3 | 7 | 11 | 15 | 19 | 23 | 27 | 31 | None through 31 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Number of primes | 611 | 309 | 154 | 76 | 31 | 24 | 0 | 9 | 3 |

The limiting densities are derived in Sections 2 and 3 of the paper.

## Build the English paper

The bibliography is included in the TeX source. The following commands build the PDF with Tectonic.

```sh
cd paper
tectonic manuscript.tex
```

## AI contribution and review status

OpenAI Codex proposed the problem, developed the statements and proofs, searched for related work, drafted both language versions and wrote the numerical verification code. The finite calculation has been reproduced. The general arguments and their priority await independent scholarly assessment.

Comments on the density-one implication in Proposition 3 and references to earlier treatments of the same statistic are especially welcome. When reporting a mathematical issue, please identify the relevant proposition, hypothesis or step. The [annotated references](references.md) describe the role of the five works cited in the manuscript.

## 中文简介

对每个奇素数 $p$，从 $p^2/4$ 右边开始，寻找能使 $4/p^2$ 分解成三个单位分数的第一个分母 $x$。本文给出偏移 $4x-p^2$ 在奇素数中的极限分布，也构造出首个偏移恰为指定素数的无穷多个例子。中文稿保留全部证明、算例和数值表。此稿由 AI 参与推导与写作，公开征求同行审阅。
