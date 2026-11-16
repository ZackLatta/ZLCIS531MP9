{
  "metadata": {
    "assignment": "MP 9",
    "track": "VDB Track",
    "commit": "3fe830a",
    "gold_row_count": 50,
    "overlap_row_count": 20,
    "silver_pool_count": 1200,
    "exemplar_pool_count": 368,
    "labels": [
      "Hustle_Narrative",
      "Regional_Authenticity",
      "Lyrical_Sovereignty",
      "Systemic_Critique",
      "Boom_Bap",
      "G_Funk",
      "Trap",
      "Chopper"
    ]
  },
  "inter_annotator_agreement": {
    "overlap_count": 20,
    "percent_agreement": 0.85,
    "cohens_kappa": 0.8286,
    "kappa_ci_95": [0.6396, 1.0000],
    "bootstrap_resamples": 1000,
    "confusion_matrix": [
      [2, 0, 0, 1, 0, 0, 0, 0],
      [0, 2, 0, 0, 0, 1, 0, 0],
      [0, 0, 2, 0, 1, 0, 0, 0],
      [0, 0, 0, 3, 0, 0, 0, 0],
      [0, 0, 0, 0, 2, 0, 0, 0],
      [0, 0, 0, 0, 0, 2, 0, 0],
      [0, 0, 0, 0, 0, 0, 2, 0],
      [0, 0, 0, 0, 0, 0, 0, 2]
    ],
    "adjudicated_disagreements": [
      {
        "id": "gold_01",
        "annotator_1": "Regional_Authenticity",
        "annotator_2": "G_Funk",
        "adjudicated": "Regional_Authenticity",
        "rule": "Boundary 1"
      },
      {
        "id": "gold_02",
        "annotator_1": "Lyrical_Sovereignty",
        "annotator_2": "Boom_Bap",
        "adjudicated": "Lyrical_Sovereignty",
        "rule": "Boundary 2"
      },
      {
        "id": "gold_08",
        "annotator_1": "Hustle_Narrative",
        "annotator_2": "Systemic_Critique",
        "adjudicated": "Hustle_Narrative",
        "rule": "Boundary 3"
      }
    ]
  },
  "weak_supervision": {
    "silver_pool_size": 1200,
    "source_tag": "silver",
    "grading_eligible": false,
    "labeling_functions": {
      "EmbeddingPrototypeClassifier": 0.45,
      "lf_dsp_acoustic": 0.25,
      "lf_regional_origin": 0.15,
      "lf_lexicon_keywords": 0.15
    },
    "silver_vs_gold_accuracy": 0.4200,
    "silver_vs_gold_accuracy_ci_95": [0.2800, 0.5600],
    "silver_vs_gold_macro_f1": 0.3427,
    "silver_vs_gold_macro_f1_ci_95": [0.2278, 0.4418],
    "silver_vs_gold_kappa": 0.3406
  },
  "retrieval_augmented_classification": {
    "index_type": "faiss.IndexFlatIP",
    "mp7_fixed_baseline": {
      "macro_f1": 0.2976,
      "macro_f1_ci_95": [0.1880, 0.3790]
    },
    "retrieval_k": {
      "3": {
        "p_at_k": 0.3667,
        "p_at_k_ci_95": [0.2730, 0.4530],
        "recall_at_k": 0.0257,
        "recall_at_k_ci_95": [0.0180, 0.0330],
        "rag_macro_f1": 0.4240,
        "rag_macro_f1_ci_95": [0.2800, 0.5350],
        "delta_vs_mp7_baseline": 0.1264
      },
      "5": {
        "p_at_k": 0.3920,
        "p_at_k_ci_95": [0.3120, 0.4720],
        "recall_at_k": 0.0441,
        "recall_at_k_ci_95": [0.0350, 0.0530],
        "rag_macro_f1": 0.5974,
        "rag_macro_f1_ci_95": [0.4250, 0.7040],
        "delta_vs_mp7_baseline": 0.2999
      },
      "10": {
        "p_at_k": 0.3420,
        "p_at_k_ci_95": [0.2720, 0.4100],
        "recall_at_k": 0.0754,
        "recall_at_k_ci_95": [0.0600, 0.0900],
        "rag_macro_f1": 0.4720,
        "rag_macro_f1_ci_95": [0.3090, 0.5860],
        "delta_vs_mp7_baseline": 0.1744
      }
    }
  },
  "cohort_convolution": {
    "cohort_axis": "generation_cohort := f(release_decade)",
    "decades": ["1990s", "2000s", "2010s", "2020s"],
    "chunks_per_decade": 300,
    "smoothing_kernel": [0.25, 0.5, 0.25],
    "first_diff_kernel": [-1, 1],
    "raw_trope_frequencies": {
      "1990s": [0.137, 0.047, 0.000, 0.010, 0.000, 0.003, 0.477, 0.327],
      "2000s": [0.143, 0.010, 0.003, 0.000, 0.000, 0.003, 0.570, 0.270],
      "2010s": [0.153, 0.000, 0.000, 0.000, 0.000, 0.003, 0.643, 0.200],
      "2020s": [0.180, 0.023, 0.000, 0.000, 0.000, 0.000, 0.667, 0.130]
    },
    "first_diff_drift": {
      "2010s->2020s": {
        "Hustle_Narrative": {"drift": 0.0267, "ci_95": [-0.0333, 0.0867]},
        "Regional_Authenticity": {"drift": 0.0233, "ci_95": [0.0067, 0.0400]},
        "Lyrical_Sovereignty": {"drift": 0.0000, "ci_95": [0.0000, 0.0000]},
        "Systemic_Critique": {"drift": 0.0000, "ci_95": [0.0000, 0.0000]},
        "Boom_Bap": {"drift": 0.0000, "ci_95": [0.0000, 0.0000]},
        "G_Funk": {"drift": -0.0033, "ci_95": [-0.0100, 0.0000]},
        "Trap": {"drift": 0.0233, "ci_95": [-0.0567, 0.1033]},
        "Chopper": {"drift": -0.0700, "ci_95": [-0.1267, -0.0067]}
      }
    },
    "pytorch_1d_conv": {
      "architecture": "nn.Conv1d(1, 1, kernel_size=2)",
      "seed": 42,
      "device": "cpu",
      "learned_weights": [0.1245, 0.8881],
      "learned_bias": -0.0016,
      "heldout_2020s_forecast_mse": {
        "learned_conv1d": 0.000016,
        "fixed_first_diff_extrap": 0.000489,
        "fixed_persistence": 0.000839,
        "fixed_smoothing_025_05_025": 0.000865
      }
    }
  }
}