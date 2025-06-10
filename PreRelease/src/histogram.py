# histogram.py

import plotly.express as px
import preprocess

def get_histogram():
    df = preprocess.load_data()

    fig = px.histogram(
        df,
        x="Motivation_Level",  # corrigé
        title="Distribution of Motivation Levels",
        color="Motivation_Level",
        text_auto=True
    )

    fig.update_layout(
        xaxis_title="Motivation Level",
        yaxis_title="Number of Students"
    )

    return fig
