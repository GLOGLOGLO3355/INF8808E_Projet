import pandas as pd
import plotly.graph_objects as go
import preprocess
import numpy as np

def get_sleep_motivation_heatmap():
    df = preprocess.load_data()
    df = df.dropna(subset=["Sleep_Hours", "Motivation_Level", "Attendance"])
    df["Sleep_Hours_Int"] = df["Sleep_Hours"].round().astype(int)

    ordered_levels = ["Low", "Medium", "High"]
    df = df[df["Motivation_Level"].isin(ordered_levels)]
    df["Motivation_Level"] = pd.Categorical(df["Motivation_Level"], categories=ordered_levels, ordered=True)

    avg_attendance = df.groupby(["Motivation_Level", "Sleep_Hours_Int"])["Attendance"].mean().reset_index()
    avg_pivot = avg_attendance.pivot(index="Motivation_Level", columns="Sleep_Hours_Int", values="Attendance")
    avg_pivot = avg_pivot.reindex(ordered_levels)

    counts = df.groupby(["Motivation_Level", "Sleep_Hours_Int"]).size().reset_index(name="Count")
    count_pivot = counts.pivot(index="Motivation_Level", columns="Sleep_Hours_Int", values="Count")
    count_pivot = count_pivot.reindex(ordered_levels)

    avg_data = np.nan_to_num(avg_pivot.values, nan=0)
    count_data = np.nan_to_num(count_pivot.values, nan=0).astype(int)

    hovertext = []
    for i, y in enumerate(avg_pivot.index):
        row = []
        for j, x in enumerate(avg_pivot.columns):
            row.append(
                f"Sleep Duration (rounded): {x} h<br>"
                f"Motivation Level: {y}<br>"
                f"Average Attendance: {avg_data[i][j]:.2f}<br>"
                f"Number of Students: {count_data[i][j]}"
            )
        hovertext.append(row)

    fig = go.Figure(data=go.Heatmap(
        z=avg_data,
        x=avg_pivot.columns.tolist(),
        y=avg_pivot.index.tolist(),
        colorscale="Blues",
        colorbar=dict(title="Average Attendance"),
        hoverinfo="text",
        text=hovertext
    ))

    fig.update_layout(
        title="Average Attendance by Sleep and Motivation",
        xaxis_title="Sleep Hours",
        yaxis_title="Motivation Level",
        height=600,
        width=800
    )

    return fig
