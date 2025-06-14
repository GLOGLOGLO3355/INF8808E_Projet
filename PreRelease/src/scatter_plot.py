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
        hover_data=["Previous_Scores", "Exam_Score", "Hours_Studied", "Tutoring_Sessions"]
    )

    fig.update_layout(
        xaxis_title="Current Exam Score",
        yaxis_title="Previous Exam Score",
        coloraxis_colorbar=dict(title="Hours Studied")
    )

    return fig
