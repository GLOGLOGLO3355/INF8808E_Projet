from plotly.subplots import make_subplots
import plotly.graph_objects as go
import preprocess

def get_sunburst():
    df = preprocess.load_data()
    df = df.dropna(subset=["Parental_Education_Level", "Parental_Involvement"])
    df = df[df["Parental_Education_Level"].isin(["High School", "College", "Postgraduate"])]
    df = df[df["Parental_Involvement"] != "Other"]

    fig = make_subplots(
        rows=1,
        cols=3,
        specs=[[{"type": "domain"}, {"type": "domain"}, {"type": "domain"}]],
        subplot_titles=[
            "<b>High School</b>",
            "<b>College</b>",
            "<b>Postgraduate</b>"
        ],
        column_widths=[0.3, 0.3, 0.3]
    )

    for i, level in enumerate(["High School", "College", "Postgraduate"], start=1):
        sub_df = df[df["Parental_Education_Level"] == level]
        values = sub_df["Parental_Involvement"].value_counts()
        labels = values.index.tolist()

        fig.add_trace(
            go.Pie(
                labels=labels,
                values=values,
                name=level,
                hovertemplate='%{label}<br>Count=%{value}<extra></extra>',
                showlegend=(i == 1)
            ),
            row=1,
            col=i
        )

    fig.update_layout(
        title_text="Parental Involvement by Education Level",
        title_y=0.95,
        title_font_size=20,
        margin=dict(t=80, l=50, r=150, b=40),
        legend=dict(
            title="Parental Involvement",
            x=1.05,
            y=0.5,
            traceorder="normal"
        )
    )

    return fig
