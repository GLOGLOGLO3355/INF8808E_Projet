import pandas as pd
import plotly.express as px
import preprocess


def get_extracurricular_boxplot():
    df = preprocess.load_data()
    df = df.dropna(subset=["Extracurricular_Activities", "Exam_Score"])

    fig = px.box(
        df,
        x="Extracurricular_Activities",
        y="Exam_Score",
        points="all",
        labels={
            "Extracurricular_Activities": "Participates in Extracurricular Activities",
            "Exam_Score": "Exam Score",
        },
        title="Exam Scores by Participation in Extracurricular Activities",
    )

    fig.update_layout(
        width=800, height=500, xaxis=dict(tickmode="array", tickvals=["Yes", "No"])
    )

    return fig
