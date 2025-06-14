# -*- coding: utf-8 -*-

import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import preprocess
import sunburst
import scatter_plot
import score_improvement
import numeric_heatmap

app = dash.Dash(__name__)
app.title = 'Pre-Release | INF8808'

app.layout = html.Div(
    children=[
        html.H1("Demo Release – INF8808E – Summer 2025"),

    html.Div([
    html.H2("Understanding Academic Performance: A Data-Driven Exploration"),
    html.P(
        "Academic performance is shaped by a wide range of personal, familial, and institutional factors. "
        "While some influences like study hours or past exam scores are direct and measurable, others (such as parental involvement, "
        "motivation, sleep, or socioeconomic background) may be harder to quantify but just as impactful."
    ),
    html.P([
        "This interactive dashboard explores these multifaceted relationships using synthetic but realistic student data. ",
        "The dataset, available on Kaggle, contains 6,607 entries and 20 variables, "
        "covering a wide range of academic, behavioral, and contextual features such as study habits, family income, school type, "
        "peer influence, parental education, and learning disabilities."
        ,
        html.Br(),
        html.A(" View the dataset on Kaggle",
               href="https://www.kaggle.com/datasets/lainguyn123/student-performance-factors",
               target="_blank",
               style={"textDecoration": "underline", "color": "#1a73e8"})
    ]),
    html.P(
        "Through a series of visualizations, we aim to answer a central question: "
        "to what extent do lifestyle, support systems, and external conditions influence students’ academic outcomes?"
    ),
    html.P(
        "Each section below highlights a different angle of this complex puzzle, from the role of parental education to the impact of sleep and tutoring. "
        "The goal of this exploratory analysis is not only to identify patterns, but also to encourage thoughtful reflection on how academic support strategies "
        "can be better targeted and personalized."
    )
], style={"maxWidth": "800px", "marginBottom": "60px"}),

        html.Div([
            html.H2("Parental Involvement and Education"),
            html.P(
                "This visualization investigates whether parental involvement is correlated with higher educational levels. "
                "The chart suggests a general pattern: a greater proportion of parents with a “High” involvement are found among those "
                "whose parents have attained a college or a postgraduate degree. Involvement of parents who have only completed high school "
                "tends to be more evenly distributed, with a higher share in the “Low” category. Furthermore, the visualization indirectly "
                "raises other questions regarding parental involvement. The larger the portion of the visualisation, the better the student’s "
                "academic performance. Overall, the chart suggests that more educated parents could directly or indirectly contribute to better "
                "academic performance in their children."
            )
        ], style={"maxWidth": "800px", "marginBottom": "30px"}),

        dcc.Graph(
            id='example-sunburst',
            figure=sunburst.get_sunburst()
        ),

        html.Div([
            html.H2("Study Effort and Tutoring Impact"),
            html.P(
                "This section examines how hours studied and tutoring sessions affect the evolution from previous to current exam scores. "
                "The scatter plot shows a strong positive correlation between previous and current exam scores, with students who study a "
                "higher number of hours demonstrating a noticeable improvement in their scores compared to those who study fewer hours. "
                "Tutoring further enhances this progression: students with no tutoring sessions show minimal improvement, while those with a "
                "substantial number of sessions exhibit a more significant increase in their scores. Notably, students who both study extensively "
                "and attend many tutoring sessions achieve the most marked improvement in their current scores compared to their previous scores. "
                "This suggests that combining extensive study with tutoring can significantly drive academic improvement, offering valuable insights "
                "for students, parents and school organizations aiming to optimize academic growth."
            ),
            dcc.Dropdown(
                id="tutoring-filter",
                options=[{"label": f"{i} sessions", "value": i} for i in range(9)],
                placeholder="Filter by number of tutoring sessions",
                style={"width": "50%", "marginBottom": "20px"}
            ),
            dcc.Graph(id="scatter-plot")
        ], style={"maxWidth": "1000px", "marginTop": "50px"}),

        html.Div([
            html.H2("Simplified View: Score Improvement Separately"),
            html.P(
                "These two graphs isolate the individual effects of tutoring and study hours on score improvement. "
                "We calculate the score difference (final - previous) and show how it varies depending on each factor."
            ),
            html.H3("Score Improvement by Tutoring Sessions"),
            dcc.Graph(figure=score_improvement.get_by_tutoring()),

            html.H3("Score Improvement by Study Hours"),
            dcc.Graph(figure=score_improvement.get_by_study_hours())
        ], style={"maxWidth": "1000px", "marginTop": "50px"}),

        html.Div([
        html.P(
            "Overall, the data suggests that the final exam may have been more challenging than the previous one, as the median score improvement is consistently negative "
            "across all study efforts and tutoring levels. However, despite this downward trend, a small but noticeable difference is observed: students who studied more hours "
            "tended to perform slightly better than those who did not. "
            "While this does not indicate a dramatic improvement, it highlights the value of consistent academic effort, even in more difficult contexts."
        )
    ], style={"maxWidth": "800px", "marginTop": "60px", "marginBottom": "60px"}),

    html.Div([
        html.H2("Tutoring Sessions and Disabilities: Unequal Outcomes"),
        html.P(
            "This section examines the relationship between tutoring sessions, grades and learning disabilities. "
            "The scatter plot reveals that students with learning disabilities generally participate in a higher number "
            "of tutoring sessions compared to their peers without disabilities, indicating a greater effort to seek support. "
            "However, despite this increased effort, their grades tend to be lower on average, with a wider spread, suggesting "
            "more variability in their academic outcomes. In contrast, students without learning disabilities show a more "
            "consistent trend of improved grades as tutoring sessions increase. This highlights that while students with learning "
            "disabilities may need to invest more effort in tutoring to address their challenges, the academic results they achieve "
            "can vary widely, underscoring the need for personalized support strategies to help them achieve more consistent and "
            "improved outcomes."
        ),
        dcc.Graph(figure=numeric_heatmap.get_binary_disability_heatmap())
    ], style={"maxWidth": "1000px", "marginTop": "50px"}),

    ],

    style={
        "display": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "justifyContent": "center",
        "textAlign": "center",
        "padding": "30px"
    }
)


@app.callback(
    Output("scatter-plot", "figure"),
    [Input("tutoring-filter", "value")]
)
def update_scatter(tutoring_value):
    return scatter_plot.get_scatter_plot(tutoring_value)


if __name__ == "__main__":
    app.run_server(debug=True)
