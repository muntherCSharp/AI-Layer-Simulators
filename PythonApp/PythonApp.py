import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.cluster import DBSCAN
import pandas as pd

# === 1) Confusion Matrix ===
y_test = ["Password","Network","Software","Password","Network","Software","Password","Software","Network"]
y_pred = ["Password","Network","Software","Password","Network","Software","Password","Password","Network"]

labels = ["Password","Network","Software"]
cm = confusion_matrix(y_test, y_pred, labels=labels)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
disp.plot(cmap=plt.cm.Blues, values_format='d')
plt.title("Confusion Matrix – ITSM AI Classifier")
plt.show()


# === 2) ITSM Evolution Plot (Automation → AI Layer) ===
stages = ["Automation Only", "With AI Layer"]
scores = [0.4, 0.85]

plt.figure(figsize=(6,4))
plt.plot(stages, scores, marker="o", linestyle="--", color="purple")
plt.ylim(0,1)
plt.ylabel("Intelligence Level (0–1)")
plt.title("ITSM Evolution: From Automation to AI-Enhanced")
for i, val in enumerate(scores):
    plt.text(i, val+0.03, f"{val*100:.0f}%", ha='center', fontsize=10)
plt.show()


# === 3) ITSM Alert Correlation (Unsupervised) ===
np.random.seed(42)
n_alerts = 150
times = np.cumsum(np.random.exponential(scale=2.0, size=n_alerts)).astype(int)
severity = np.random.randint(1, 6, size=n_alerts)
signature = np.random.choice([101, 102, 201, 301], size=n_alerts, p=[0.3, 0.3, 0.25, 0.15])


alerts_automation = len(times)

X = np.vstack([
    times / (times.max()+1),  
    severity / 5.0,
    signature / max(signature)
]).T

db = DBSCAN(eps=0.05, min_samples=3).fit(X)
labels = db.labels_
alerts_ai = len(set(labels) - {-1})

plt.figure(figsize=(6,4))
plt.bar(["Automation Only", "With AI Layer"], [alerts_automation, alerts_ai], color=["gray","purple"])
plt.ylabel("Number of Alerts / Incidents")
plt.title("ITSM Alert Handling: Automation vs AI Layer")
for i, val in enumerate([alerts_automation, alerts_ai]):
    plt.text(i, val+2, str(val), ha='center', fontsize=10)
plt.show()