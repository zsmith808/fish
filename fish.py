import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Sample data
fishing_spots = {
    "Lake Tahoe": ["Rainbow Trout", "Mackinaw", "Kokanee Salmon"],
    "Florida Keys": ["Tarpon", "Snook", "Bonefish"],
    "Columbia River": ["Chinook Salmon", "Sturgeon", "Smallmouth Bass"]
}

# Session state for storing catch logs
if "catches" not in st.session_state:
    st.session_state.catches = []

st.title("🎣 Fishing Companion App")

tab1, tab2, tab3 = st.tabs(["Fishing Spots", "Log a Catch", "My Catches"])

# ---- Fishing Spots ----
with tab1:
    st.header("📍 Popular Fishing Spots")
    for spot, species in fishing_spots.items():
        with st.expander(f"🌊 {spot}"):
            st.write("Common Fish Species:")
            for fish in species:
                st.markdown(f"- {fish}")

# ---- Log a Catch ----
with tab2:
    st.header("📝 Log Your Catch")
    with st.form("catch_form"):
        name = st.text_input("Fish Species", placeholder="e.g., Rainbow Trout")
        location = st.selectbox("Location", list(fishing_spots.keys()))
        size = st.number_input("Size (inches)", min_value=0.0, step=0.5)
        notes = st.text_area("Notes (optional)")
        submitted = st.form_submit_button("Log Catch")

        if submitted:
            st.session_state.catches.append({
                "species": name,
                "location": location,
                "size": size,
                "notes": notes,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            st.success(f"Caught a {name} at {location} logged!")

# ---- My Catches ----
with tab3:
    st.header("📘 Catch Log")
    if not st.session_state.catches:
        st.info("No catches logged yet.")
    else:
        for i, catch in enumerate(reversed(st.session_state.catches), 1):
            st.subheader(f"#{i}: {catch['species']}")
            st.write(f"**Location:** {catch['location']}")
            st.write(f"**Size:** {catch['size']} inches")
            st.write(f"**Date:** {catch['date']}")
            if catch['notes']:
                st.write(f"**Notes:** {catch['notes']}")
            st.markdown("---")





