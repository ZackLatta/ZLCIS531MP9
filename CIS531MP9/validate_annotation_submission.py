import json
import os
from classifiers import LABELS

def validate_annotation_submission(
    raw_path="gold_raw.jsonl",
    adj_path="gold_adjudicated.jsonl",
    partner_path="gold_partner.jsonl",
    overlap_path="overlap_ids.txt",
):
    assert os.path.exists(raw_path), f"Missing {raw_path}"
    assert os.path.exists(adj_path), f"Missing {adj_path}"
    assert os.path.exists(overlap_path), f"Missing {overlap_path}"

    raw_rows = [json.loads(line) for line in open(raw_path)]
    adj_rows = [json.loads(line) for line in open(adj_path)]
    partner_rows = [json.loads(line) for line in open(partner_path)]
    overlap_ids = [line.strip() for line in open(overlap_path) if line.strip()]

    # Hard CI/CD Gate: strictly <= 50 rows
    assert 1 <= len(raw_rows) <= 50, f"CI GATE FAIL: {len(raw_rows)} > 50"
    assert len(adj_rows) == len(raw_rows), "Adjudicated row count mismatch"
    assert len(overlap_ids) == 20, f"Expected 20 overlap IDs, got {len(overlap_ids)}"

    raw_ids = {r["id"] for r in raw_rows}
    partner_ids = {r["id"] for r in partner_rows}
    assert set(overlap_ids).issubset(raw_ids), "Overlap IDs missing from gold_raw"
    assert set(overlap_ids).issubset(partner_ids), "Overlap IDs missing from partner"

    for r in adj_rows:
        assert r.get("source") == "gold", f"Invalid source tag: {r.get('source')}"
        assert r["label"] in LABELS, f"Out-of-ontology label: {r['label']}"

    print(
        f"[PASS] validate_annotation_submission: {len(raw_rows)} gold rows "
        f"(<=50 gate), {len(overlap_ids)} overlap IDs, all labels in PS 6 schema."
    )
    return True

if __name__ == "__main__":
    validate_annotation_submission()
