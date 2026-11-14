# Debugging log
## DBG-001 — Independent TF-IDF vectorizer spaces (synthetic example)
Symptom: claim and document vectors created with independently fitted vocabularies cannot be compared in one shared feature space.
Correction: fit one vectorizer on document abstracts and transform claims with the same fitted object.
Edge case: empty query or corpus raises ValueError.
Status: constructed teaching example; not a real observed Colab failure. Any previous results using separate vocabularies must be rerun.