import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# 1) Carrega os dados
df = pd.read_csv('base_treino.csv')

# 2) Converte colunas categóricas para numéricas
le = LabelEncoder()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = le.fit_transform(df[col].astype(str))

# 3) Colunas de defeito (one-hot → binário)
label_cols = [
    'trinca_transversal',
    'trinca_longit_face_media',
    'trinca_canto',
    'fissura_borda',
    'trinca_longitud_canto',
    'trinca_fora_canto',
    'falha_outros'
]
def binarize(x):
    s = str(x).strip().lower()
    return 1 if s in ('true','sim','1','t','y','yes') else 0

for col in label_cols:
    df[col] = df[col].apply(binarize)

# 4) Gera a coluna única de classe
df['defeito'] = df[label_cols].idxmax(axis=1)

# 5) Agora sim: seleciona **todas** as colunas numéricas (int, float, bool) como features,
#    menos 'id' e menos as 7 de defeito
numeric_cols = df.select_dtypes(include=[np.number, bool]).columns.tolist()
feature_cols = [c for c in numeric_cols if c not in label_cols + ['id','defeito']]

X = df[feature_cols].fillna(df[feature_cols].median())
y = df['defeito']

# 6) Split treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# 7) Treina o Random Forest
clf = RandomForestClassifier(
    n_estimators=100,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)

clf.fit(X_train, y_train)

# 8) Avaliação
y_pred = clf.predict(X_test)
print("=== Classification Report ===")
print(classification_report(y_test, y_pred))
print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))
