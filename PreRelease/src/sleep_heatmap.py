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

    # Moyenne des présences
    avg_attendance = df.groupby(["Motivation_Level", "Sleep_Hours_Int"])["Attendance"].mean().reset_index()
    avg_pivot = avg_attendance.pivot(index="Motivation_Level", columns="Sleep_Hours_Int", values="Attendance")
    avg_pivot = avg_pivot.reindex(ordered_levels)

    # Nombre d'étudiants
    counts = df.groupby(["Motivation_Level", "Sleep_Hours_Int"]).size().reset_index(name="Count")
    count_pivot = counts.pivot(index="Motivation_Level", columns="Sleep_Hours_Int", values="Count")
    count_pivot = count_pivot.reindex(ordered_levels)

    fig = go.Figure(data=go.Heatmap(
        z=avg_pivot.values,
        x=avg_pivot.columns.tolist(),
        y=avg_pivot.index.tolist(),
        customdata=count_pivot.values,
        colorscale="Blues",
        colorbar=dict(title="Average Attendance"),
        hovertemplate=(
            "Sleep Hours: %{x}<br>"
            "Motivation: %{y}<br>"
            "Avg Attendance: %{z:.2f}<br>"
            "Students: %{customdata}<extra></extra>"
        )
    ))

    fig.update_layout(
        title="Average Attendance by Sleep and Motivation",
        xaxis_title="Sleep Hours",
        yaxis_title="Motivation Level",
        height=600,
        width=800
    )

    return fig
