# Dataset acquisition

Candidate benchmark: AllenAI SciFact.
Official repository: https://github.com/allenai/scifact
Paper: https://aclanthology.org/2020.emnlp-main.609/

After the environment is verified, clone the official repository:
```bash
git clone https://github.com/allenai/scifact.git data/scifact-upstream
git -C data/scifact-upstream rev-parse HEAD > logs/scifact_commit.txt
find data/scifact-upstream -maxdepth 4 -type f | sort > logs/scifact_file_manifest.txt
```
Record SHA256 checksums for used data. The official test claims are unlabeled; do not invent test metrics. Inspect data and code licensing separately before redistribution. Never use gold labels/evidence to select corruption distractors.
