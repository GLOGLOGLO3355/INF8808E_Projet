import plotly.express as px
import preprocess

def get_scatter_plot(tutoring_filter=None):
    df = preprocess.load_data()
    df = df.dropna(subset=["Previous_Scores", "Exam_Score", "Hours_Studied", "Tutoring_Sessions"])

    if tutoring_filter is not None:
        df = df[df["Tutoring_Sessions"] == tutoring_filter]

    fig = px.scatter(
        df,
        x="Exam_Score",
        y="Previous_Scores",
        color="Hours_Studied",
        color_continuous_scale="Blues",
        title="Impact of Study Hours and Tutoring on Score Improvement",
        hover_data={
            "Exam_Score": True,
            "Previous_Scores": True,
            "Hours_Studied": True,
            "Tutoring_Sessions": True
        },
        labels={
            "Exam_Score": "Final Exam Score",
            "Previous_Scores": "Previous Test Score",
            "Hours_Studied": "Weekly Study Hours",
            "Tutoring_Sessions": "Monthly Tutoring Sessions"
        }
    )

    fig.update_layout(
        xaxis_title="Final Exam Score",
        yaxis_title="Previous Test Score",
        coloraxis_colorbar=dict(title="Weekly Study Hours")
    )

    return fig
