import importlib, sys
mods = ["numpy", "pandas", "scipy", "sklearn", "yaml", "tqdm", "matplotlib"]
print("Python:", sys.version.split()[0])
for name in mods:
    m = importlib.import_module(name)
    print("IMPORT_OK", name, getattr(m, "__version__", "version-not-exposed"))
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
X = TfidfVectorizer().fit_transform(["alpha beta", "beta gamma"])
assert X.shape[0] == 2 and X.shape[1] > 0
assert f1_score([0,1],[0,1],average="macro") == 1.0
print("SMOKE_TEST_PASSED", X.shape)
