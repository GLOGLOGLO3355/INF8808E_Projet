import pandas as pd
import preprocess
import plotly.graph_objects as go

def get_binary_disability_heatmap():
    df = preprocess.load_data()
    df = df.dropna(subset=["Tutoring_Sessions", "Exam_Score", "Learning_Disabilities"])

    df["Disability_Status"] = df["Learning_Disabilities"].map({
        "Yes": "Disability",
        "No": "No Disability"
    })

    df["Tutoring_Sessions"] = df["Tutoring_Sessions"].astype(int)
    df["Exam_Score_Bin"] = (df["Exam_Score"] // 5) * 5

    grouped = df.groupby(["Tutoring_Sessions", "Exam_Score_Bin", "Disability_Status"]).size().unstack(fill_value=0).reset_index()

    grouped["Dominant"] = grouped.apply(
        lambda row: "Disability" if row.get("Disability", 0) > row.get("No Disability", 0)
        else "No Disability" if row.get("Disability", 0) < row.get("No Disability", 0)
        else "Equal", axis=1
    )

    pivot = grouped.pivot(index="Exam_Score_Bin", columns="Tutoring_Sessions", values="Dominant")
    pivot = pivot.sort_index(ascending=True)

    category_to_value = {"Disability": 0, "No Disability": 1, "Equal": 2}
    z_matrix = pivot.replace(category_to_value).values[::-1]
    y_labels = list(pivot.index[::-1])
    x_labels = list(pivot.columns)

    hover_text = []
    for y in y_labels:
        row = []
        for x in x_labels:
            dominant = pivot.at[y, x] if x in pivot.columns else "N/A"
            interval = f"{y-2.5}-{y+2.5}"
            row.append(f"Tutoring: {x}<br>Score: {interval}<br>Dominant: {dominant}")
        hover_text.append(row)

    color_scale = [
        [0.0, "crimson"],
        [0.33, "crimson"],
        [0.34, "royalblue"],
        [0.66, "royalblue"],
        [0.67, "lightgrey"],
        [1.0, "lightgrey"]
    ]

    heatmap = go.Heatmap(
        z=z_matrix,
        x=x_labels,
        y=y_labels,
        colorscale=color_scale,
        showscale=False,
        text=hover_text,
        hoverinfo="text"
    )

    legend_items = [
        go.Scatter(x=[None], y=[None], mode='markers', marker=dict(size=10, color="crimson"), name="Disability"),
        go.Scatter(x=[None], y=[None], mode='markers', marker=dict(size=10, color="royalblue"), name="No Disability"),
        go.Scatter(x=[None], y=[None], mode='markers', marker=dict(size=10, color="lightgrey"), name="Equal")
    ]

    fig = go.Figure(data=[heatmap] + legend_items)

    fig.update_layout(
        title="Dominant Group by Tutoring Sessions and Exam Score",
        xaxis_title="Tutoring Sessions",
        yaxis_title="Exam Score",
        height=600,
        width=1000,
        xaxis=dict(
            tickmode="array",
            tickvals=list(range(0, 9)),
            ticktext=[str(i) for i in range(0, 9)],
            range=[-0.5, 8.5]
        ),
        yaxis=dict(
            tickmode="array",
            tickvals=list(range(50, 105, 5))[::-1],
            ticktext=[str(y) for y in range(50, 105, 5)][::-1],
            range=[53, 102],
            autorange=False
        ),
        legend=dict(
            orientation="v",
            yanchor="top",
            y=0.98,
            xanchor="left",
            x=1.02
        )
    )

    return fig
