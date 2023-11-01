import sys
import os
import yaml
import pickle

import pandas as pd
from xgboost import XGBClassifier

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython dt.py data-file model \n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("models", sys.argv[2])
os.makedirs(os.path.join("models"), exist_ok=True)

params = yaml.safe_load(open("params.yaml"))["train"]
p_n_estimators = params["n_estimators"]
p_max_depth = params["max_depth"]

df = pd.read_csv(f_input, header=None)
X = df.iloc[:, [i for i in range(6 + 1)]]
y = df.iloc[:, -1]

model = XGBClassifier(n_estimators=10_000,
                      max_depth=3,
                      learning_rate=0.01,
                      eval_metric="mlogloss")

model.fit(X, y, verbose=100)

with open(f_output, "wb") as fd:
    pickle.dump(model, fd)
