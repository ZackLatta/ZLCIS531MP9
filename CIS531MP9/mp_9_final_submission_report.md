# MP 9: Retrieval-Augmented Classification & Convolutions

**Track:** VDB Track (CIS 731 Custom PS 6 Ontology) | **Commit:** `3fe830a`

## Codebook and Attestation

- **Codebook (`codebook.md`):** Extends the PS 6 8-class ontology (`schema/ontology_instances.json` & `ontology.schema.json`) into mutually exclusive operational rules, 3 boundary precedence rules, and concrete labeled exemplars (`gold_00`–`gold_07`) drawn from `gold_adjudicated.jsonl`.
- **Pathway & CI Gate:** Constructed under **Pathway A** (third-party ground-truth audit of RateYourMusic `master_ontology_mapped.csv` genres/tropes and capstone DSP metadata; zero verbatim copyrighted lyrics persisted). `gold_raw.jsonl` contains exactly **50 rows** (`source=gold`), passing `validate_annotation_submission` ($\le 50$-row hard CI ceiling).
- **Attestation (`attestation.md`):** Independent audit by Arron Weber (Annotator 1) and Zack Latta (Annotator 2 on 20-item `overlap_ids.txt`: `gold_00`–`gold_19`). Session window: `2026-11-15T22:15:00Z` to `2026-11-15T22:55:00Z` (**0.67 hours** $\le 2.00$-hour ceiling).

## Inter-Annotator Agreement and Adjudication

On the 20-object partner overlap (`overlap_ids.txt`), Arron and Zack achieved **85.00%** raw agreement (17/20 exact matches) and Cohen's $\kappa =$ **0.8286** (95% bootstrap CI: **[0.6396, 1.0000]**, $B=1,000$ resamples).

### 8x8 Overlap Confusion Matrix (Rows = Arron, Columns = Zack)

| A1 \ A2 | Hustle | Region | Lyric | Critiq | BoomBp | GFunk | Trap | Chopp |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hustle** | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| **Region** | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 |
| **Lyric** | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 |
| **Critiq** | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| **BoomBp** | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| **GFunk** | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| **Trap** | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| **Chopp** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |

- **Adjudication Protocol:** All 3 disagreements (`gold_01`: `Regional_Authenticity` vs. `G_Funk`; `gold_02`: `Lyrical_Sovereignty` vs. `Boom_Bap`; `gold_08`: `Hustle_Narrative` vs. `Systemic_Critique`) were resolved using Codebook Section 2 boundary rules (requiring explicit sonic or institutional markers before overriding primary tags) and saved in `gold_adjudicated.jsonl`.

## Weak-Supervision Agreement Analysis

- **Labeling Functions & Weighted Vote:** Expanded **1,200** stratified capstone track-chunk records (`silver_pool.jsonl`, 300/decade, tagged `source=silver` in `silver_labeled.jsonl`) via weighted voting across 4 signals: (1) MP 7 `EmbeddingPrototypeClassifier` ($w=0.45$), (2) `lf_dsp_acoustic` BPM/sub-bass rules ($w=0.25$), (3) `lf_regional_origin` geography cues ($w=0.15$), and (4) `lf_lexicon_keywords` thematic terms ($w=0.15$).
- **Silver-vs-Gold Agreement ($n=50$):** Evaluated on `gold_adjudicated.jsonl` (`grading_eligible=False` for silver pool), achieving Accuracy = **0.4200** (95% CI: [0.2800, 0.5600]), Macro-F1 = **0.3427** ([0.2278, 0.4418]), and $\kappa =$ **0.3406**.
- **Failure Modes:** (1) *Domain shift between RYM artist summaries and track-level DSP metadata* lowers recall on lyrical classes (`Lyrical_Sovereignty`, `Systemic_Critique`) where acoustic BPM/bass LFs abstain; (2) *Regional-to-subgenre conflation* causes Southern/West Coast tracks lacking explicit `808`/`Moog` cues to default to `Trap` or `G_Funk`.

## Retrieval-Augmented Classification Results

Top-$k$ exemplars ($k \in \{3, 5, 10\}$) were retrieved via exact inner-product search (`faiss.IndexFlatIP`) over the disjoint 368-item exemplar pool (`mp9_exemplar_pool.jsonl`) to condition classification on `gold_adjudicated.jsonl` ($n=50$), compared against the MP 7 fixed baseline (`FixedDemonstrationLLMClassifier`, 8 balanced fixed demos):

| Method | P@k [95% CI] | Recall@k [95% CI] | Macro-F1 [95% CI] | $\Delta$ F1 vs. MP 7 |
| :--- | :---: | :---: | :---: | :---: |
| **MP 7 Fixed Baseline** | — | — | 0.2976 [0.188,0.379] | `0.0000` |
| **FAISS RAG (k=3)** | 0.3667 [0.273,0.453] | 0.0257 [0.018,0.033] | 0.4240 [0.280,0.535] | `+0.1264` |
| **FAISS RAG (k=5)** | **0.3920 [0.312,0.472]** | 0.0441 [0.035,0.053] | **0.5974 [0.425,0.704]** | **`+0.2999`** |
| **FAISS RAG (k=10)** | 0.3420 [0.272,0.410] | 0.0754 [0.060,0.090] | 0.4720 [0.309,0.586] | `+0.1744` |

Dynamic top-$k$ retrieval outperforms the MP 7 fixed baseline across all $k$, peaking at **$k=5$** (`Macro-F1 = 0.5974`, `P@5 = 0.3920`), whereas expanding to $k=10$ introduces cross-genre neighbor dilution (`F1 = 0.4720`).

## Cohort Convolution Analysis

- **Cohort Axis & Kernels:** Silver chunks ($N=1,200$) were binned along the VDB ordered axis `generation_cohort := f(release_decade)` across `1990s`, `2000s`, `2010s`, and `2020s` (300 chunks/decade). Per-cohort 8-class trope-frequency vectors were convolved with smoothing kernel $[0.25, 0.50, 0.25]$ (replicate padding) and first-difference drift kernel $[-1, 1]$ with 1,000-resample bootstrap 95% CIs:

| Trope / Subgenre | 1990s | 2000s | 2010s | 2020s | Drift (2010s->2020s) [95% CI] |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `Hustle_Narrative` | 0.137 | 0.143 | 0.153 | 0.180 | +0.0267 [-0.0333, +0.0867] |
| `Regional_Authenticity` | 0.047 | 0.010 | 0.000 | 0.023 | +0.0233 [+0.0067, +0.0400] |
| `Lyrical_Sovereignty` | 0.000 | 0.003 | 0.000 | 0.000 | +0.0000 [+0.0000, +0.0000] |
| `Systemic_Critique` | 0.010 | 0.000 | 0.000 | 0.000 | +0.0000 [+0.0000, +0.0000] |
| `Boom_Bap` | 0.000 | 0.000 | 0.000 | 0.000 | +0.0000 [+0.0000, +0.0000] |
| `G_Funk` | 0.003 | 0.003 | 0.003 | 0.000 | -0.0033 [-0.0100, +0.0000] |
| `Trap` | 0.477 | 0.570 | 0.643 | 0.667 | +0.0233 [-0.0567, +0.1033] |
| `Chopper` | 0.327 | 0.270 | 0.200 | 0.130 | -0.0700 [-0.1267, -0.0067] |

- **CIS 731 PyTorch 2.x 1-D Convolutional Kernel Comparison:** Trained a causal 2-tap `nn.Conv1d(1, 1, kernel_size=2)` on historical decade transitions (`1990s->2000s->2010s`, CPU-only, seed 42; learned weights `[0.1245, 0.8881]`, bias `-0.0016`) and evaluated held-out `2020s` forecast MSE against fixed baselines:
  - **Learned PyTorch `Conv1d` MSE:** **`0.000016`** (lowest forecast error)
  - **Fixed First-Difference Extrapolation (`[-1, 1]`) MSE:** `0.000489`
  - **Fixed Persistence MSE:** `0.000839`
  - **Fixed Smoothing (`[0.25, 0.50, 0.25]`) MSE:** `0.000865`

## GenAI Audit

The Generative AI Kit (v3.3 Tollbooth Procedure) was used to structure `codebook.md`, verify `validate_annotation_submission` CI gate assertions, and audit the PyTorch 1-D convolution harness (`GenAI.pdf`). All gold labels were audited under Pathway A without AI label assignment, and all metrics in `report.md` were re-derived from `results.json`.