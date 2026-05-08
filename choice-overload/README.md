# 🧠 Choice Overload & Dual-Process Theory
**A Computational Model of Consumer Behaviour in E-commerce**

This repository contains a Python simulation of Choice Overload (Iyengar & Lepper, 2000)
through the lens of Dual-Process Theory (Kahneman, 2011), applied to online consumer
decision-making. Part of an ongoing series modelling Behavioural Economics theories computationally.

---

## 📋 The Research Question

> *Does a larger product assortment always lead to more purchases?*

Standard economic theory says yes — more choice means more consumers find their ideal product.
Behavioural economics says no — beyond a threshold, more options overwhelm System 2,
push consumers toward System 1 heuristics, and increase cart abandonment.

This model tests that prediction computationally.

---

## 🔬 Model Architecture

```
BLOCK 1 — Cognitive Load
    cognitive_load(n_products) → [0, 1]
    Based on Weber-Fechner Law: perceived difficulty grows logarithmically

BLOCK 2 — System Activation
    activate_system(nfc, n_products) → ("S1" or "S2", probability)
    P(S2) = NFC × (1 − cognitive_load)

BLOCK 3 — Purchase Decision
    purchase_decision(system, prob_s2, products) → (outcome, item)
    S2 → maximises rating/price ratio
    S1 → heuristic: cheapest / top_rated / first_seen
    Overload → abandoned (prob_s2 < 0.05 and n_products ≥ 24)

BLOCK 4 — Population Simulation
    N = 500 agents, NFC ~ N(0.5, 0.2)
    4 assortment sizes: [6, 12, 24, 48]
    2,000 purchase decisions simulated

BLOCK 5 — Visualisation
    4 publication-ready figures
```

---

## 📊 Key Results (N = 500)

| Products | Conversion | Abandonment | S2 Rate | Avg Rating |
|----------|------------|-------------|---------|------------|
| 6        | 100%       | 0.0%        | 30.6%   | 3.90       |
| 12       | 100%       | 0.0%        | 22.2%   | 4.05       |
| 24       | 96.4%      | 3.6%        | 13.8%   | 3.78       |
| 48       | 83.2%      | 16.8%       | 10.0%   | 3.63       |

**Core finding:** Moving from 12 to 48 products reduces conversion by 17%
and cuts System 2 activation by more than half.

### By Consumer Profile (48 products)

| Profile    | Abandonment | Avg Rating |
|------------|-------------|------------|
| Intuitive  | 52.5%       | 3.47       |
| Average    | 0.0%        | 3.68       |
| Reflective | 0.0%        | 4.21       |

---

## 📁 Repository Structure

```
choice-overload-model/
├── README.md              ← this file
├── theory.txt             ← theoretical background & references
├── choice_overload.py     ← full simulation script
├── requirements.txt       ← dependencies
└── outputs/
    └── choice_overload_results.png
```

---

## ▶️ Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/choice-overload-model.git
cd choice-overload-model

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the simulation
python choice_overload.py
```

The script generates results in the terminal and saves `choice_overload_results.png`.

---

## 📦 Requirements

```
numpy>=1.24
pandas>=2.0
matplotlib>=3.7
```

Python 3.11+ recommended.

---

## 📚 References

- Iyengar, S. S., & Lepper, M. R. (2000). When choice is demotivating.
  *Journal of Personality and Social Psychology, 79*(6), 995–1006.
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Schwartz, B. (2004). *The Paradox of Choice*. Harper Collins.
- Cacioppo, J. T., & Petty, R. E. (1982). The need for cognition.
  *Journal of Personality and Social Psychology, 42*(1), 116–131.
- Frederick, S. (2005). Cognitive reflection and decision making.
  *Journal of Economic Perspectives, 19*(4), 25–42.

---

## 👤 Author

Researcher in Behavioural Economics
*Modelling BE theories computationally — one model at a time.*
