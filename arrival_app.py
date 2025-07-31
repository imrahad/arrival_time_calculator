import streamlit as st
from datetime import datetime, timedelta

st.title("🚗 Arrival Time Calculator")
st.write("Calculate your expected arrival time based on when you start your journey.")

# Get user input
departure_input = st.time_input("Select your departure time:", value=datetime.strptime("06:30", "%H:%M").time())

def calculate_arrival(departure_time):
    # Convert to datetime for calculation
    now = datetime.now()
    departure_dt = datetime.combine(now.date(), departure_time)

    # Reference times
    base_time = departure_dt.replace(hour=7, minute=0)
    end_peak_time = departure_dt.replace(hour=9, minute=0)

    # Logic for travel time
    if departure_dt < base_time:
        travel_duration = timedelta(minutes=60)
        reason = "Travel started before 7:00 AM — 60 minutes travel time."
    elif base_time <= departure_dt < end_peak_time:
        minutes_late = int((departure_dt - base_time).total_seconds() // 60)
        extra_minutes = minutes_late * 5
        travel_duration = timedelta(minutes=60 + extra_minutes)
        reason = f"Travel between 7:00–9:00 AM — 60 + ({minutes_late} × 5) = {60 + extra_minutes} minutes."
    else:
        travel_duration = timedelta(minutes=90)
        reason = "Travel after 9:00 AM — 90 minutes travel time."

    # Calculate and return arrival time
    arrival_dt = departure_dt + travel_duration
    return arrival_dt.time(), reason

# Calculate
arrival_time, explanation = calculate_arrival(departure_input)

# Display result
st.subheader("🕓 Estimated Arrival Time:")
st.success(f"{arrival_time.strftime('%H:%M')}")

st.markdown("### 📋 Explanation:")
st.info(explanation)