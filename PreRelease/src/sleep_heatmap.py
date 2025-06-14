import pandas as pd
import plotly.graph_objects as go
import preprocess

def get_sleep_motivation_heatmap():
    df = preprocess.load_data()
    df = df.dropna(subset=["Sleep_Hours", "Motivation_Level", "Attendance"])
    df["Sleep_Hours_Int"] = df["Sleep_Hours"].round().astype(int)

    ordered_levels = ["Low", "Medium", "High"]
    df = df[df["Motivation_Level"].isin(ordered_levels)]
    df["Motivation_Level"] = pd.Categorical(df["Motivation_Level"], categories=ordered_levels, ordered=True)

    grouped = df.groupby(["Motivation_Level", "Sleep_Hours_Int"])["Attendance"].sum().reset_index()
    pivot = grouped.pivot(index="Motivation_Level", columns="Sleep_Hours_Int", values="Attendance")
    pivot = pivot.reindex(ordered_levels)

    fig = go.Figure(data=go.Heatmap(
        z=pivot.values,
        x=pivot.columns.tolist(),
        y=pivot.index.tolist(),
        colorscale="Blues",
        colorbar=dict(title="Total Attendance"),
        hovertemplate="Sleep Hours: %{x}<br>Motivation: %{y}<br>Total Attendance: %{z}<extra></extra>"
    ))

    fig.update_layout(
        title="Total Attendance by Sleep and Motivation",
        xaxis_title="Sleep Hours",
        yaxis_title="Motivation Level",
        height=600,
        width=800
    )

    return fig
