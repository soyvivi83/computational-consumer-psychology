"""
choice_overload.py
==================
Computational simulation of Choice Overload & Dual-Process Theory
applied to e-commerce consumer behaviour.

Theory:  Kahneman (2011), Iyengar & Lepper (2000)
Author:  Behavioural Economics Researcher
GitHub:  https://github.com/YOUR_USERNAME/choice-overload-model
"""

# ── 0. IMPORTS ────────────────────────────────────────────────────────────────

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Fix randomness for reproducibility — essential in research
random.seed(42)
np.random.seed(42)


# ── 1. COGNITIVE LOAD ─────────────────────────────────────────────────────────
#
# How much does the assortment exhaust System 2?
# Based on Weber-Fechner Law: perceived difficulty grows logarithmically.
# Going from 6 to 12 products feels harder than going from 42 to 48.

def cognitive_load(n_products):
    """
    Returns a cognitive load value between 0 and 1.
    0 = no load, 1 = maximum cognitive overload.

    Parameters
    ----------
    n_products : int
        Number of products in the assortment.
    """
    return min(1.0, np.log(n_products) / np.log(100))


# ── 2. SYSTEM ACTIVATION ──────────────────────────────────────────────────────
#
# Which system does the consumer activate?
# P(S2) = NFC × (1 − cognitive_load)
# When load overwhelms NFC, System 2 collapses to 0 — System 1 takes over.

def activate_system(nfc, n_products):
    """
    Determines whether the consumer activates System 1 or System 2.

    Parameters
    ----------
    nfc : float
        Need for Cognition score [0, 1]. Higher = more likely to use S2.
    n_products : int
        Number of products in the assortment.

    Returns
    -------
    system : str
        "S1" or "S2"
    prob_s2 : float
        Probability of S2 activation.
    """
    load    = cognitive_load(n_products)
    prob_s2 = max(0, nfc * (1 - load))

    if random.random() < prob_s2:
        return "S2", prob_s2
    else:
        return "S1", prob_s2


# ── 3. PURCHASE DECISION ──────────────────────────────────────────────────────
#
# Three possible outcomes:
#   Overload  → abandoned  (S2 blocked + large assortment)
#   System 2  → purchased  (rational: maximise rating/price)
#   System 1  → purchased  (heuristic: cheapest / top_rated / first_seen)

def purchase_decision(system, prob_s2, products):
    """
    Simulates the consumer's purchase decision.

    Parameters
    ----------
    system : str
        "S1" or "S2" — output of activate_system()
    prob_s2 : float
        Probability of S2 activation — used to detect overload.
    products : list of dict
        Each product has keys: id, price, rating.

    Returns
    -------
    outcome : str
        "purchased" or "abandoned"
    item : dict or None
        The chosen product, or None if abandoned.
    """
    # Overload: S2 completely blocked AND assortment is large
    if prob_s2 < 0.05 and len(products) >= 24:
        return "abandoned", None

    if system == "S2":
        # Rational evaluation: maximise value-for-money
        best = max(products, key=lambda p: p["rating"] / p["price"])
        return "purchased", best

    else:  # System 1 — heuristic shortcut
        heuristic = random.choice(["cheapest", "top_rated", "first_seen"])

        if heuristic == "cheapest":
            chosen = min(products, key=lambda p: p["price"])
        elif heuristic == "top_rated":
            chosen = max(products, key=lambda p: p["rating"])
        else:  # first_seen — position bias
            chosen = products[0]

        return "purchased", chosen


# ── 4. CATALOGUE GENERATOR ────────────────────────────────────────────────────

def make_catalogue(n):
    """
    Generates a simulated product catalogue.

    Parameters
    ----------
    n : int
        Number of products to generate.

    Returns
    -------
    list of dict with keys: id, price (€10–100), rating (1–5)
    """
    return [
        {
            "id":     i + 1,
            "price":  round(random.uniform(10, 100), 2),
            "rating": round(random.uniform(1, 5), 1),
        }
        for i in range(n)
    ]


# ── 5. POPULATION SIMULATION ──────────────────────────────────────────────────

N           = 500
assortments = [6, 12, 24, 48]

# NFC follows a normal distribution — most consumers are average
# np.clip ensures values stay between 0 and 1
nfc_population = np.clip(
    np.random.normal(loc=0.5, scale=0.2, size=N), 0, 1
)

results = []

for n_products in assortments:
    catalogue = make_catalogue(n_products)

    for i, nfc in enumerate(nfc_population):
        system, prob    = activate_system(nfc, n_products)
        outcome, item   = purchase_decision(system, prob, catalogue)

        results.append({
            "consumer_id":   i,
            "nfc":           round(nfc, 3),
            "profile":       "reflective" if nfc > 0.6
                             else "average" if nfc > 0.4
                             else "intuitive",
            "n_products":    n_products,
            "system":        system,
            "outcome":       outcome,
            "rating_chosen": item["rating"] if item else None,
            "price_chosen":  item["price"]  if item else None,
        })

df = pd.DataFrame(results)


# ── 6. ANALYSIS ───────────────────────────────────────────────────────────────

summary = df.groupby("n_products").agg(
    conversion_rate  = ("outcome", lambda x: (x == "purchased").mean()),
    abandonment_rate = ("outcome", lambda x: (x == "abandoned").mean()),
    s2_rate          = ("system",  lambda x: (x == "S2").mean()),
    avg_rating       = ("rating_chosen", "mean"),
).round(3)

by_profile = df.groupby(["n_products", "profile"]).agg(
    conversion_rate  = ("outcome", lambda x: (x == "purchased").mean()),
    abandonment_rate = ("outcome", lambda x: (x == "abandoned").mean()),
).round(3)

print("=" * 55)
print(f"  CHOICE OVERLOAD SIMULATION — N = {N}")
print("=" * 55)
print("\n── Results by assortment size ─────────────────────────")
print(summary.to_string())
print("\n── Results by consumer profile ────────────────────────")
print(by_profile.to_string())


# ── 7. VISUALISATION ──────────────────────────────────────────────────────────

plt.rcParams.update({
    "font.family":       "serif",
    "font.size":         10,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "figure.dpi":        150,
})

fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle(
    "Choice Overload & Dual-Process Theory — E-commerce Simulation (N=500)",
    fontsize=12, fontweight="bold"
)

colors = {
    "intuitive":  "#E8673A",
    "average":    "#F5C842",
    "reflective": "#3A7EC8"
}

# Plot 1: Conversion rate by assortment size
ax1 = axes[0, 0]
conv = summary["conversion_rate"] * 100
ax1.plot(assortments, conv.values, marker="o", color="#3A7EC8",
         linewidth=2, markersize=7)
ax1.set_title("Conversion Rate by Assortment Size", pad=10)
ax1.set_xlabel("Number of products")
ax1.set_ylabel("Conversion rate (%)")
ax1.set_xticks(assortments)
ax1.set_ylim(75, 105)

# Plot 2: Abandonment rate by consumer profile
ax2 = axes[0, 1]
for profile, color in colors.items():
    data = df[df["profile"] == profile].groupby("n_products").agg(
        abandonment=("outcome", lambda x: (x == "abandoned").mean())
    ) * 100
    ax2.plot(assortments, data["abandonment"].values, marker="o",
             label=profile, color=color, linewidth=2, markersize=7)
ax2.set_title("Abandonment Rate by Consumer Profile", pad=10)
ax2.set_xlabel("Number of products")
ax2.set_ylabel("Abandonment rate (%)")
ax2.set_xticks(assortments)
ax2.legend(frameon=False)

# Plot 3: System 2 activation rate
ax3 = axes[1, 0]
s2 = summary["s2_rate"] * 100
ax3.bar(assortments, s2.values, color="#3A7EC8",
        alpha=0.8, width=3, edgecolor="white")
ax3.set_title("System 2 Activation Rate", pad=10)
ax3.set_xlabel("Number of products")
ax3.set_ylabel("% consumers using S2")
ax3.set_xticks(assortments)

# Plot 4: Choice quality — System 1 vs System 2
ax4 = axes[1, 1]
s1_ratings = (df[df["system"] == "S1"]
              .groupby("n_products")["rating_chosen"].mean())
s2_ratings = (df[df["system"] == "S2"]
              .groupby("n_products")["rating_chosen"].mean())

x     = np.arange(len(assortments))
width = 0.35

ax4.bar(x - width/2, s1_ratings.values, width=width,
        color="#E8673A", alpha=0.85, label="System 1", edgecolor="white")
ax4.bar(x + width/2, s2_ratings.values, width=width,
        color="#3A7EC8", alpha=0.85, label="System 2", edgecolor="white")
ax4.set_title("Choice Quality: S1 vs S2", pad=10)
ax4.set_xlabel("Number of products")
ax4.set_ylabel("Avg rating of chosen product")
ax4.set_xticks(x)
ax4.set_xticklabels(assortments)
ax4.set_ylim(3, 5)
ax4.legend(frameon=False)

plt.tight_layout(rect=[0, 0, 1, 0.95], h_pad=3.5)
plt.savefig("choice_overload_results.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n✓ Figure saved as choice_overload_results.png")
