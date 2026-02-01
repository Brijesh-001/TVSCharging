# 🔋 EV Full-Charge Time Calculator (Streamlit)

A simple Streamlit app to estimate **when an EV will be fully charged**, based on:
- current battery charge (%)
- current time

The app uses **realistic EV charging behavior**, including **slowdown after 80%**.

---

## ✨ Features

- Input **current charge (%)**
- Input **current time**
- Calculates:
  - ⏱ Time required to reach 100%
  - 🕒 Exact clock time when charging completes
- Uses **tapered charging logic**:
  - 0–80% → fast charging
  - 80–90% → medium
  - 90–100% → slow (trickle)

Clean UI, no unnecessary inputs.

---

## ⚙️ Charging Logic Used

| Charge Range | Charging Rate |
|-------------|---------------|
| 0–80% | 0.30 % per minute |
| 80–90% | 0.18 % per minute |
| 90–100% | 0.10 % per minute |

These values are based on **real EV charging observations** and can be adjusted in code.

---

## 🖥️ How the App Works

Example:

- Current charge: **72%**
- Current time: **10:56 AM**

Output:

> Fully charged in **~3 hours**  
> Charging completes at **~1:55 PM**

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install streamlit