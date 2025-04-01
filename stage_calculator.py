import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

st.title("📐 Stage Panel Calculator")

stage_width = st.number_input("Stage Width (ft)", min_value=1.0, value=12.0)
stage_height = st.number_input("Stage Height (ft)", min_value=1.0, value=16.0)

panel_width = 4
panel_height = 8

cols = math.ceil(stage_width / panel_width)
rows = math.ceil(stage_height / panel_height)
total_panels = cols * rows

st.write(f"### Total panels required: {total_panels}")

fig, ax = plt.subplots(figsize=(cols * 1.5, rows * 1.5))

panel_number = 1
for i in range(cols):
    for j in range(rows):
        x = i * panel_width
        y = j * panel_height
        rect = patches.Rectangle((x, y), panel_width, panel_height, edgecolor='black', facecolor='skyblue', lw=2)
        ax.add_patch(rect)
        ax.text(x + panel_width/2, y + panel_height/2, f'{panel_number}', 
                ha='center', va='center', fontsize=10, color='black')
        panel_number += 1

ax.set_xlim(0, cols * panel_width)
ax.set_ylim(0, rows * panel_height)
ax.set_aspect('equal')
ax.set_xlabel("Width (ft)")
ax.set_ylabel("Height (ft)")
ax.set_title("Stage Panel Layout")
ax.grid(True)

st.pyplot(fig)
