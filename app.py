import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="EV Charge Time", page_icon="🔋", layout="centered")

st.title("🔋 EV Full-Charge Time Calculator")

st.divider()

# ---- INPUTS ----
current_charge = st.number_input(
    "Current charge (%)",
    min_value=0,
    max_value=100,
    value=72
)

current_time = st.time_input(
    "Current time",
    value=datetime.strptime("10:56", "%H:%M").time()
)

# ---- CHARGING RATES ----
RATE_FAST = 0.30      # 0–80%
RATE_80_90 = 0.18     # 80–90%
RATE_90_100 = 0.10    # 90–100%

# ---- CALCULATION ----
def time_to_full(soc):
    minutes = 0

    if soc < 80:
        minutes += (80 - soc) / RATE_FAST
        soc = 80

    if soc < 90:
        minutes += (90 - soc) / RATE_80_90
        soc = 90

    if soc < 100:
        minutes += (100 - soc) / RATE_90_100

    return int(minutes)

if st.button("Calculate Full Charge Time", use_container_width=True):
    mins_needed = time_to_full(current_charge)

    finish_time = (
        datetime.combine(datetime.today(), current_time)
        + timedelta(minutes=mins_needed)
    ).time()

    hrs = mins_needed // 60
    mins = mins_needed % 60

    st.success(
        f"🔌 Fully charged in **{hrs} hr {mins} min**\n\n"
        f"🕒 **Time: {finish_time.strftime('%I:%M %p')}**"
    )