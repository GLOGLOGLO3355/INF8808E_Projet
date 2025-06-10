import plotly.express as px
import preprocess

def get_sunburst():
    df = preprocess.load_data()

    df = df.dropna(subset=["Parental_Education_Level", "Parental_Involvement"])

    fig = px.sunburst(
        df,
        path=["Parental_Education_Level", "Parental_Involvement"],
        title="Parental Involvement by Education Level",
        color="Parental_Involvement"
    )

    fig.update_layout(margin=dict(t=40, l=0, r=0, b=0))
    return fig

