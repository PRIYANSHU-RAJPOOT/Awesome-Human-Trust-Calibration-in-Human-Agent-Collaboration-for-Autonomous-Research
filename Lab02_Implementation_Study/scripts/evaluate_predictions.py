#!/usr/bin/env python3
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

REQ = {"method","run_id","claim_id","split","y_true","y_pred"}
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True)
    p.add_argument("--outdir",default="results/evaluation")
    p.add_argument("--expected-split",default=None)
    a=p.parse_args()
    df=pd.read_csv(a.input)
    missing=REQ-set(df.columns)
    if missing: raise ValueError(f"Missing columns: {sorted(missing)}")
    if df[list(REQ)].isna().any().any(): raise ValueError("Missing required values")
    for c in ["method","run_id","claim_id","split"]:
        df[c]=df[c].astype(str).str.strip()
        if (df[c]=="").any(): raise ValueError(f"Blank values in {c}")
    if a.expected_split and set(df.split)!={a.expected_split}:
        raise ValueError(f"Unexpected split values: {sorted(set(df.split))}")
    if df.duplicated(["method","run_id","claim_id"]).any():
        raise ValueError("Duplicate method/run/claim rows")
    if (df.groupby(["split","claim_id"]).y_true.nunique()>1).any():
        raise ValueError("Ground truth label disagreement across comparators")
    ref=None
    for key,g in df.groupby(["method","run_id"]):
        ids=set(zip(g.split,g.claim_id))
        if ref is None: ref=(key,ids)
        elif ids!=ref[1]: raise ValueError(f"Claim-ID mismatch in {key} vs {ref[0]}")
    out=[]
    for (m,r,s),g in df.groupby(["method","run_id","split"]):
        y,yp=g.y_true,g.y_pred
        out.append(dict(method=m,run_id=r,split=s,n_claims=len(g),
            accuracy=accuracy_score(y,yp),
            macro_f1=f1_score(y,yp,average="macro",zero_division=0),
            weighted_f1=f1_score(y,yp,average="weighted",zero_division=0),
            macro_precision=precision_score(y,yp,average="macro",zero_division=0),
            macro_recall=recall_score(y,yp,average="macro",zero_division=0),
            error_rate=float(np.mean(np.asarray(y)!=np.asarray(yp)))))
    res=pd.DataFrame(out)
    od=Path(a.outdir); od.mkdir(parents=True,exist_ok=True)
    res.to_csv(od/"results.csv",index=False)
    res.groupby("method").agg({"macro_f1":["mean","std","count"],"error_rate":["mean","std","count"]}).to_csv(od/"method_summary.csv")
    print("VALIDATION_PASSED")
    print(res.to_string(index=False))
    print("Saved",od/"results.csv","and",od/"method_summary.csv")
if __name__=="__main__": main()
