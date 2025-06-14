# -*- coding: utf-8 -*-

import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import sunburst
import scatter_plot
import score_improvement
import numeric_heatmap
import dendrogram
import extracurricular_boxplot
import alluvial_diagram
import sleep_heatmap

app = dash.Dash(__name__)
app.title = 'Pre-Release | INF8808'

app.layout = html.Div(
    children=[
        html.H1("Demo Release – INF8808E – Summer 2025"),

    html.Div([
        html.H2("Understanding Academic Performance: A Data-Driven Exploration"),
        html.P(
            "Sometimes harder to put a value on are factors that shape academic performance. "
            "Where some influences such as study hours or past exam scores work directly and measurably, "
            "other factors—could be parental support, motivation, sleep, or socioeconomic background—are equally influential."
        ),
        html.P([
            "This interactive dashboard explores these multifaceted relationships with synthetic and yet plausible student data. "
            "The dataset, found here on Kaggle, comprises 6,607 entries and 20 variables that reflect a wide range of academic, "
            "behavioral, and contextual traits into study habits, family income, school type, peer influence, parental education, "
            "and learning disabilities.",
            html.Br(),
            html.A(" View the dataset on Kaggle",
                href="https://www.kaggle.com/datasets/lainguyn123/student-performance-factors",
                target="_blank",
                style={"textDecoration": "underline", "color": "#1a73e8"})
        ]),
        html.P(
            "The objective of the set of visualizations is to answer this main question: do lifestyle, support, and other external "
            "conditions affect students' academic outcomes and to what extent?"
        ),
        html.P(
            "The sections below explore various horizons in this multi-faceted puzzle, from parental education to the influence of sleep and tutoring. "
            "This exploratory investigation aims not only to identify trends that support academic achievement, but also to stimulate further musings about "
            "how academic support strategies can be refined and made more effective."
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
            html.H3("Simplified View: Score Improvement Separately"),
            html.P(
                "These two graphs isolate the individual effects of tutoring and study hours on score improvement. "
                "We calculate the score difference (final - previous) and show how it varies depending on each factor."
            ),
            html.H4("Score Improvement by Tutoring Sessions"),
            dcc.Graph(figure=score_improvement.get_by_tutoring()),

            html.H4("Score Improvement by Study Hours"),
            dcc.Graph(figure=score_improvement.get_by_study_hours())
        ], style={"maxWidth": "1000px", "marginTop": "50px"}),

        html.Div([
        html.P(
            "Overall, the data indicate that the final exam might have been more difficult than the previous one, "
            "with median score improvement consistently negative across the range of study efforts and levels of tutoring. "
            "But along this downward trend, a small, noticeable difference appears, where students who studied more hours tended "
            "to do a little better than those who did not. This nuance does not imply that they performed drastically better, "
            "instead emphasizing the importance of consistent academic effort, even in a more difficult environment."
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

    html.Div([
    html.H2("Visualizing Motivation Through Social and Environmental Factors"),
    html.P(
        "This dendrogram visualizes the similarity between students based on key performance indicators such as study hours, "
        "past exam scores, and tutoring sessions. It helps identify natural clusters or groups of students with similar academic behaviors."
    ),
    html.Div([
        dcc.Graph(figure=dendrogram.get_tree_plot())
    ], style={"display": "flex", "justifyContent": "center"}),
    html.P(
        "This section examines the impact of peer influence and distance on student motivation. "
        "This linear dendrogram reveals that students with positive peer influence and living near their school are more likely "
        "to exhibit high motivation, compared to those with negative peer influence and far distances, where a very small percentage "
        "show high motivation. Moderate distances and neutral influence result in a balanced distribution, with medium motivation dominating. "
        "The thicker lines for near distances with positive influence highlight a stronger clustering of high motivation, suggesting that "
        "proximity to school and supportive peers significantly boost motivation. This insight is valuable for parents considering school "
        "location and for schools fostering positive peer environments."
    )], style={"maxWidth": "1000px", "marginTop": "50px"}),
    html.Div([
        html.H2("Academic Performance and Extracurricular Activities"),
        html.P(
            "This chart explores whether involvement in extracurricular activities correlates with improved academic performance. "
            "The box plot shows that the median score for students who participate in extracurricular activities is slightly higher (70) "
            "than for those who do not (69). The interquartile range is almost identical for both sides, it measures the spread of the middle 50% of scores, "
            "between the 25th and the 75th percentiles. The similarity in this value, around 12.5 for both, shows that the students’ scores are similarly distributed "
            "regardless of extracurricular participation. While there is a  difference in the median, the distribution suggests that participation in extracurricular activities "
            "does not negatively affect academic performance and might even offer a very slight advantage."
        ),
    html.Div([
        dcc.Graph(figure=extracurricular_boxplot.get_extracurricular_boxplot())
    ], style={"display": "flex", "justifyContent": "center"}),

    html.Div([
        html.H2("School Type, Resources and Exam Scores"),
        html.P(
            "This Alluvial diagram shows how family income and school type affect teacher quality and ultimately academic performance. "
            "To improve readability, exam scores have been grouped into categories such as Excellent, Good, or Pass. "
            "This allows us to better understand patterns without being overwhelmed by too much detail."
        ),
        dcc.Graph(figure=alluvial_diagram.get_alluvial_diagram()),
        html.P(
            "We can observe that students from high-income families are more likely to attend private schools, whereas students from low-income families "
            "tend to attend public schools, highlighting a clear socioeconomic divide in access to educational institutions. Private schools are associated "
            "with a diverse range of teacher quality, while public schools exhibit a broader mix including more medium and low-quality teaching. The quality "
            "of teaching influences final grades, with varying exam scores resulting from different teacher quality levels. The flow lines in the diagram "
            "illustrate this dynamic, showing that thicker flows from various teacher qualities span the exam score range, suggesting that while teacher quality "
            "plays a role, other factors also contribute to student success."
        )
    ], style={"maxWidth": "1000px", "marginTop": "50px"}),
    html.Div([
        html.H2("Attendance Based on Sleep and Motivation"),
        html.P(
            "We can see that students with medium motivation and 7 hours of sleep show the highest attendance levels, "
            "which is indicated by the darkest blue segment in that column. Additionally, students with extremely high or "
            "extremely low motivation do not outperform those in the medium range. Furthermore, attendance declines significantly "
            "at the extremes of sleep duration, particularly below 5 hours and above 8 hours, regardless of motivation. These bars remain "
            "across all motivation levels, which indicates that neither high motivation can compensate for sleep deprivation, nor can longer "
            "sleep offset the effects of low motivation. The students getting 9 or 10 hours of sleep do not necessarily have low attendance "
            "even though it is a light colour, it is mainly because there are not many students getting that many hours of sleep. This pattern "
            "highlights a non-linear relationship between sleep and attendance: while moderate sleep boosts participation, sleep deprivation "
            "correlates with reduced attendance."
        ),
     html.Div([
        dcc.Graph(figure=sleep_heatmap.get_sleep_motivation_heatmap())
        ], style={"display": "flex", "justifyContent": "center"}),
    ], style={"maxWidth": "1000px", "marginTop": "50px"}),

html.Div([
    html.H2("Conclusion: Unveiling the Complexity of Academic Success"),
    html.P(
        "This data-driven exploration highlights how academic performance is the result of a complex web of interconnected factors. "
        "From the downside of parental education and involvement into tutoring, sleep, and peer support, none of these factors work in isolation. "
        "Academic success is achieved when structural, social, and behavioral supports align. Students gain most from an environment that comprises families cognizant of education, "
        "regular access to good education and resources, ability to maintain healthy sleep habits, and motivation from supportive peers and surroundings."
    ),
    html.P(
        "While some factors show relatively direct relationships with performance, such as study hours or school category, the remaining factors, such as sleep or disabilities, "
        "may have more nuanced behaviors and non-linear relationships. At the very least, these variations are of critical importance for some groups (such as people with learning disabilities "
        "or disadvantaged people from lower social-economy backgrounds) who need to be targeted to achieve even results."
    ),
    html.P(
        "In the end, helping students succeed means looking at the full picture, and making sure no one is left behind."
    )
], style={"maxWidth": "800px", "marginTop": "80px", "marginBottom": "80px", "textAlign": "center"})




    ], style={"maxWidth": "1000px", "marginTop": "50px"})
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
