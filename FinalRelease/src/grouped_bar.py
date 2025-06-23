import plotly.express as px
import preprocess


def get_grouped_bar_chart():
    df = preprocess.load_data()
    df = df.dropna(subset=["Parental_Education_Level", "Parental_Involvement"])
    df = df[
        df["Parental_Education_Level"].isin(["High School", "College", "Postgraduate"])
    ]
    df = df[df["Parental_Involvement"] != "Other"]

    display_labels = {
        "High School": "High School",
        "College": "University",
        "Postgraduate": "Postgraduate",
    }

    df["Education_Label"] = df["Parental_Education_Level"].map(display_labels)

    counts = (
        df.groupby(["Education_Label", "Parental_Involvement"])
        .size()
        .reset_index(name="Count")
    )
    total_per_edu = counts.groupby("Education_Label")["Count"].transform("sum")
    counts["Percentage"] = (counts["Count"] / total_per_edu * 100).round(1)

    fig = px.bar(
        counts,
        x="Parental_Involvement",
        y="Percentage",
        color="Education_Label",
        barmode="group",
        category_orders={
            "Education_Label": ["High School", "University", "Postgraduate"]
        },
        labels={
            "Parental_Involvement": "Parental Involvement",
            "Percentage": "Percentage (%)",
            "Education_Label": "Education Level",
        },
        title="Parental Involvement by Education Level (in %)",
    )

    fig.update_layout(
        margin=dict(t=80, l=50, r=50, b=40),
        legend=dict(x=1.05, y=1),
        xaxis_title="Type of Involvement",
        yaxis_title="Percentage (%)",
        yaxis=dict(ticksuffix="%"),
    )

    return fig
