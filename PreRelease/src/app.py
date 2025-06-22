# -*- coding: utf-8 -*-

import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import grouped_bar
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
        html.H1("Final Release – INF8808E – Summer 2025"),

    html.Div([
        html.H2("Understanding Academic Performance: A Data-Driven Exploration"),
        html.P(
            "Understanding how various factors affect academic performance can be challenging. "
            "Some influences such as study hours or past exam scores work directly and measurably, "
            "other factors (could be parental support, motivation, sleep, or socioeconomic background) are also influential."
        ),
        html.P([
            "This interactive dashboard explores these multifaceted relationships with synthetic and yet plausible student data. "
            "The dataset, found here on Kaggle, comprises 6 607 entries and 20 variables that reflect a wide range of academic, "
            "behavioural, and contextual traits, including study habits, family income, school type, peer influence, parental education, "
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
                "The visualization probes the relationship between parental level of education and the degree to which a parent engages in his or her children's academic life. "
                "Surprisingly, and contrary to assumptions that a steep upward trend is expected, the involvement distribution tends to remain consistent across the different levels of education. "
                "In all three groups (High School, University, and Postgraduate) the medium category of involvement is the prevailing one and consistently represents just over half of the parents."
            ),

            html.P(
                "Parents who have 'High' levels of involvement sit at roughly the same levels over the three education categories, with slight variations: 28.7% for high school, 29.9% for university, and 28% for postgraduate. "
                "In other words, it is not the case that high school parents are much less involved or that parents who are postgraduates are highly involved. "
                "The lowest scale, 'Low,' meets some 20% over all the categories with minimal fluctuation. That means parents with higher education do not necessarily ensure it's less likely that they will be Low-involved parents."
                " These findings suggest that parental involvement may depend more on lifestyle, availability, or personal attitudes toward education than on educational attainment alone."
            ),

            html.P(
                "Overall, this visualization challenges the assumption that more educated parents are necessarily more engaged. "
                "Instead, it points to a relatively uniform distribution of parental involvement, regardless of education level. "
                "This may imply that other factors (such as work schedules, cultural values, or access to school communities) could be just as influential as formal education in shaping parental support behaviors."
                " Future research could investigate how cultural norms or work-life balance contribute to these patterns, especially in households with dual-income or immigrant backgrounds."
            )

        ], style={"maxWidth": "800px", "marginBottom": "30px"}),

        dcc.Graph(
            id='example-sunburst',
            figure=grouped_bar.get_grouped_bar_chart()
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
                " The scatter plot also highlights an important ceiling effect: students with very high past scores see limited score improvement, "
                "reinforcing the idea that tutoring and study time benefit those still on a learning curve more than top performers."
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
            html.P(
                "Interestingly, while both factors contribute positively, the distribution is skewed: for example, students receiving 6+ tutoring sessions show a broader range of improvement,"
                "possibly indicating variability in the quality of tutoring or the student’s ability to absorb it."
            ),
            html.H4("Score Improvement by Tutoring Sessions"),
            dcc.Graph(figure=score_improvement.get_by_tutoring()),

            html.H4("Score Improvement by Study Hours"),
            dcc.Graph(figure=score_improvement.get_by_study_hours())
        ], style={"maxWidth": "1000px", "marginTop": "50px"}),

        html.Div([
        html.P(
            "Overall, the data indicates that the final exam might have been more difficult than the previous one, "
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
            " This contrast invites questions about the type and delivery method of tutoring received. Are students with learning disabilities receiving the same instructional quality? Or is a different approach needed to truly meet their needs?"
        ),
        dcc.Graph(figure=numeric_heatmap.get_binary_disability_heatmap())
    ], style={"maxWidth": "1000px", "marginTop": "50px"}),

    html.Div([
    html.H2("Visualizing Motivation Through Social and Environmental Factors"),
    html.P(
        "This dendrogram visualizes the similarity between students based on key performance indicators such as study hours, "
        "past exam scores, and tutoring sessions. It helps identify natural clusters or groups of students with similar academic behaviors."
    ),
    html.P(
        "These groupings can be used to tailor interventions: for example, students in the same motivational cluster might benefit from group mentoring or shared study routines."
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
            "An observation suggests that the clusters of very low motivation students and 5 hours of sleep have the highest average attendance, "
            "with the darkest blue segment exhibited in the heatmap. We might think that very low motivation corresponds with poor attendance usually, "
            "but this may be an anomaly arising from a small size of samples recorded for this category that could have inflated averages."
        ),

        html.P(
            "The four corners of the chart have also seen some attendance at the higher side for the medium motivation students who have 7-hour long sleep; "
            "this is much more intuitive—whether a bit of motivation and one full-night sleep is enough to ensure on-time participation. "
            "Another contrasting phenomenon is that highly motivated students do not always manage to outperform those with medium motivation. "
            "Several parameter combinations with high motivation (especially with very short sleep) fall into below-average or average attendance categories, "
            "suggesting that motivation alone may not be enough for class members to build up consistent participation."
        ),

        html.P(
            "Overall, the chart presents far-from-linear evidence in favor of attendance and sleep. Moderate sleep (about 6 to 8 hours) has been correlated "
            "with the highest attendance levels and fewer variances in attendance levels. Too little or too much sleep, on the other hand, can be detrimental "
            "to attendance. The interaction of motivation with sleep remains a convoluted one: neither high motivation nor long sleeping hours guarantee attendance, "
            "whereas balanced sleep combined with moderate motivation appears to be the most stable predictor."
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
            "or disadvantaged people from lower socioeconomic backgrounds) who need to be targeted to achieve even results."
        ),
    ], style={"maxWidth": "800px", "marginTop": "80px", "marginBottom": "80px", "textAlign": "center", "marginLeft": "auto", "marginRight": "auto"})




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
