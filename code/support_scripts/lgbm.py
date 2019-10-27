import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# Encoding library
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv("/home/nishant/Desktop/IDA Project/mod_data/train.csv")

# Label encode
le = LabelEncoder()
train['card_type'] = le.fit_transform(train.card_type)

# X and y
y = train.default_ind.values
X = train.drop(['application_key', 'default_ind'], axis=1).values

# Split into train and eval
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, stratify=y, random_state=123)

# XGB
model = LGBMClassifier(max_depth=4,
                      learning_rate=0.01,
                      n_estimators=200,
                      objective='binary',
                      scale_pos_weight=2,
                      random_state=123)
model.fit(X_train, y_train)

# Prediction
preds = model.predict(X_val)

# Scoring
score = roc_auc_score(y_val, preds)
print("ROC AUC Score: {}".format(score))

