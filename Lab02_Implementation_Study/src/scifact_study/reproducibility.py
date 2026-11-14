import os, random
import numpy as np

def set_seed(seed:int=13):
    os.environ["PYTHONHASHSEED"]=str(seed)
    random.seed(seed)
    np.random.seed(seed)
