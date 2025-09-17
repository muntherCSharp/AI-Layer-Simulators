# AI-Layer-Simulators

This repository demonstrates how an **AI Layer** can enhance enterprise workflows beyond traditional automation.  
It contains small simulators in **Python** that show how Artificial Intelligence can improve **IT Service Management (ITSM)**.

---

## Features

### 1. ITSM Ticket Classifier + Knowledge Recommendations
- Automatically classifies tickets into categories (*Password*, *Network*, *Software*).  
- Suggests relevant Knowledge Base (KB) articles.  
- Evaluation is shown with a **Confusion Matrix**.

### 2. ITSM Intelligence Evolution
- Compares **Automation only** vs. **AI Layer**.  
- Visualization shows the improvement in “intelligence level” when AI is added.  

### 3. ITSM Alert Correlation (Unsupervised)
- Demonstrates how raw alerts (Automation) can be clustered into incidents (AI Layer).  
- Shows the reduction in alert noise and the efficiency gained.  

---

## Example Outputs

Confusion Matrix (Ticket Classifier)  
<img width="640" height="480" alt="Confusion Matrix" src="https://github.com/user-attachments/assets/2fb00eb4-cb3b-4dd1-8cd0-600376d9c287" />


ITSM Evolution Plot  
<img width="600" height="400" alt="ITSM Evolution" src="https://github.com/user-attachments/assets/9b5f4755-5069-45d3-81b2-48de5079813a" />


Alert Correlation (Automation vs AI Layer)  
<img width="600" height="400" alt="Alert Correlation" src="https://github.com/user-attachments/assets/043c765e-2320-4f50-9e1c-1b5b6768b68c" />


---

## Requirements

- Python 3.9+
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `scikit-learn`

Install with:
pip install -r requirements.txt

## How to Run
Run the simulators directly:
python itsm_ai_simulators.py

## Research Background
These simulators are inspired by real-world enterprise challenges:

Ticket classification & KB recommendation → speeds up incident resolution.
Alert correlation (AIOps) → reduces noise for SOC teams.
Predictive intelligence → prepares ITSM for proactive operations.

## Author

Developed by Munther Kazem – AI Researcher & Developer
Part of the Ai-Solutions initiative.

LinkedIn: [Ai-Solutions](https://www.linkedin.com/company/ai-solutions-for-artificial-intelligence-research/?viewAsMember=true)

Medium: coming soon
