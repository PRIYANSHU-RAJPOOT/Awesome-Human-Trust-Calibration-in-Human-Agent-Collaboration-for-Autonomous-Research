from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_retrieve(claim_texts, abstract_texts):
    """Generic sparse TF-IDF utility; not the complete official SciFact pipeline."""
    if not claim_texts or not abstract_texts:
        raise ValueError("claims and abstracts must both be non-empty")
    vectorizer = TfidfVectorizer()
    doc_matrix = vectorizer.fit_transform(abstract_texts)
    claim_matrix = vectorizer.transform(claim_texts)
    return cosine_similarity(claim_matrix, doc_matrix)
