
import pickle
import pandas as pd
with open('model_pickle','rb') as f:
    mp = pickle.load(f)
data = pd.DataFrame([[55.0, 0,	7861,	0,	38,	0,	263358.03,	1.1,	136,	1,	0,	6]])
print(mp.predict(data))
