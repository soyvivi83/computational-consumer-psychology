# 🧠 Computational Consumer Psychology
**Python simulations of Behavioural Economics theories applied to consumer decision-making**

This repository is a growing collection of computational models that translate
Behavioural Economics and Consumer Psychology theories into working Python simulations.
Each model includes the theoretical background, documented code, and publication-ready figures.

---

## 🎯 Philosophy

Standard economics assumes rational agents. Behavioural economics says otherwise.
This project tests that claim computationally — building models that simulate
how real consumers think, choose, and sometimes fail to choose at all.

Every model follows the same structure:
- **Theory first** — grounded in peer-reviewed literature
- **Code second** — clean, documented, reproducible
- **Figures third** — publication-ready visualisations

---

## 📂 Models

### 01 · Choice Overload & Dual-Process Theory
> *Why does a larger assortment sometimes lead to fewer purchases?*

Simulates 500 online consumers with heterogeneous cognitive profiles across
4 assortment sizes (6, 12, 24, 48 products). Models the interplay between
System 1/System 2 activation, Need for Cognition, and cart abandonment.

**Key finding:** Moving from 12 to 48 products reduces conversion by 17%
and cuts System 2 activation by more than half.

📁 [`choice-overload/`](./choice-overload/) &nbsp;·&nbsp;
Theory: Kahneman (2011), Iyengar & Lepper (2000)

![Choice Overload Results](choice-overload/outputs/choice_overload_results.png)

---

*More models coming soon:*

| Model | Theory | Status |
|-------|--------|--------|
| Prospect Theory | Kahneman & Tversky (1979) | 🔜 Coming soon |
| Hyperbolic Discounting | Laibson (1997) | 🔜 Coming soon |
| Anchoring in Pricing | Tversky & Kahneman (1974) | 🔜 Coming soon |
| Default Effects & Nudges | Thaler & Sunstein (2008) | 🔜 Coming soon |

---

## 🛠️ Stack

```
Python 3.11+
numpy       — numerical computing & distributions
pandas      — data analysis & aggregation
matplotlib  — publication-ready visualisation
```

Install all dependencies:
```bash
pip install numpy pandas matplotlib
```

---

## 📁 Repository Structure

```
computational-consumer-psychology/
├── README.md                        ← you are here
├── LICENSE                          ← MIT
└── choice-overload/
    ├── choice_overload.py           ← simulation script
    ├── theory.txt                   ← theoretical background
    ├── requirements.txt             ← dependencies
    └── outputs/
        └── choice_overload_results.png
```

---

## ▶️ Quickstart

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/computational-consumer-psychology.git

# Run the Choice Overload model
cd computational-consumer-psychology/choice-overload
pip install -r requirements.txt
python choice_overload.py
```

---

## 📚 Core References

- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Iyengar, S. S., & Lepper, M. R. (2000). When choice is demotivating.
  *Journal of Personality and Social Psychology, 79*(6), 995–1006.
- Tversky, A., & Kahneman, D. (1979). Prospect theory.
  *Econometrica, 47*(2), 263–291.
- Thaler, R. H., & Sunstein, C. R. (2008). *Nudge*. Yale University Press.
- Cacioppo, J. T., & Petty, R. E. (1982). The need for cognition.
  *Journal of Personality and Social Psychology, 42*(1), 116–131.

---

## 👤 Author

Researcher in Behavioural Economics & Consumer Psychology
*Modelling how real consumers think — one theory at a time.*

---

## 📄 License

MIT License — see [`LICENSE`](./LICENSE) for details.
