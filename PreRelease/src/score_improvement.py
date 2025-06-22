import plotly.express as px
import preprocess

def get_by_tutoring():
    df = preprocess.load_data()
    df = df.dropna(subset=["Previous_Scores", "Exam_Score", "Tutoring_Sessions"])
    df["Score_Improvement"] = df["Exam_Score"] - df["Previous_Scores"]

    fig = px.box(
        df,
        x="Tutoring_Sessions",
        y="Score_Improvement",
        points="all",
        title="Score Improvement by Number of Tutoring Sessions",
        hover_data={
            "Tutoring_Sessions": True,
            "Score_Improvement": True,
            "Exam_Score": True,
            "Previous_Scores": True,
            "Hours_Studied": False
        },
        labels={
            "Tutoring_Sessions": "Monthly Tutoring Sessions",
            "Score_Improvement": "Improvement in Score",
            "Exam_Score": "Final Exam Score",
            "Previous_Scores": "Previous Test Score"
        }
    )

    fig.update_layout(
        xaxis_title="Tutoring Sessions per Month",
        yaxis_title="Score Improvement (Exam - Previous)"
    )

    return fig


def get_by_study_hours():
    df = preprocess.load_data()
    df = df.dropna(subset=["Previous_Scores", "Exam_Score", "Hours_Studied"])
    df["Score_Improvement"] = df["Exam_Score"] - df["Previous_Scores"]

    fig = px.box(
        df,
        x="Hours_Studied",
        y="Score_Improvement",
        points="all",
        title="Score Improvement by Weekly Study Hours",
        hover_data={
            "Hours_Studied": True,
            "Score_Improvement": True,
            "Exam_Score": True,
            "Previous_Scores": True,
            "Tutoring_Sessions": False 
        },
        labels={
            "Hours_Studied": "Weekly Study Hours",
            "Score_Improvement": "Improvement in Score",
            "Exam_Score": "Final Exam Score",
            "Previous_Scores": "Previous Test Score"
        }
    )

    fig.update_layout(
        xaxis_title="Hours Studied per Week",
        yaxis_title="Score Improvement (Exam - Previous)"
    )

    return fig
