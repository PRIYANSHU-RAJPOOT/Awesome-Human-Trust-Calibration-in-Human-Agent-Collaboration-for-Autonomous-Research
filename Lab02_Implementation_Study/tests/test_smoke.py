import unittest
from src.scifact_study.retrieval import tfidf_retrieve

class SmokeTests(unittest.TestCase):
    def test_shared_tfidf_space(self):
        scores=tfidf_retrieve(["aspirin platelet aggregation"],["aspirin reduces platelet aggregation","vitamin c collagen"])
        self.assertEqual(scores.shape,(1,2))
        self.assertGreater(scores[0,0],scores[0,1])
    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            tfidf_retrieve([],["some abstract"])
if __name__=="__main__": unittest.main()
