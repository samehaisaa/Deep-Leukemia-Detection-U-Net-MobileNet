import streamlit as st
import plotly.graph_objects as go

import time
import numpy as np
import random

random_progress = random.randint(0, 15)

camera = {
    'eye': {'x': 0, 'y': 0, 'z': 2.4},  # Position of the camera
    'up': {'x': 1, 'y': 0, 'z': 0},   # Which direction is 'up'
    'center': {'x': 0, 'y': 0, 'z': 0} # The focus point of the camera
}


def visualize_mesh(vertices, faces, sum_distances,diff_distances, seeds, target_distances_sum, target_distances_diff, tolerance, selected_distance):
    if selected_distance :
        intensity = sum_distances
        colorscale = 'Viridis'
    else:
        intensity = diff_distances
        colorscale = 'Viridis'

    fig = plot_bipolar_contours(vertices, faces, sum_distances, diff_distances, seeds, target_distances_sum, target_distances_diff, tolerance, intensity, colorscale)
    return fig


    return fig

st.title("Représentation tripolaire équivariante")
with st.expander("Paramètres",expanded=False):
#expander code here etcc. .
with col2:
#second coloumn code here etc .. 

loading_message.text("loading keras model ....")
st.plotly_chart(fig)
