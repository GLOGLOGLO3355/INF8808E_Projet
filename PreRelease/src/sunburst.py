import plotly.express as px
import preprocess

def get_sunburst():
    df = preprocess.load_data()

    df["Parental_Education_Level"] = df["Parental_Education_Level"].fillna("Other")
    df["Parental_Involvement"] = df["Parental_Involvement"].fillna("Other")

    fig = px.sunburst(
        df,
        path=["Parental_Education_Level", "Parental_Involvement"],
        title="Parental Involvement by Education Level, click on a category to select it",
        color="Parental_Involvement",
        hover_data={"Parental_Involvement": False, "Parental_Education_Level": False}
    )
    fig.update_traces(hovertemplate='%{label}<br>Count=%{value}<extra></extra>')
    fig.update_layout(margin=dict(t=40, l=0, r=0, b=0))
    return fig

