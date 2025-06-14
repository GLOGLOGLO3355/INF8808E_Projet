import pandas as pd
import plotly.graph_objects as go
import preprocess
import plotly.express as px

def categorize_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Very Good"
    elif score >= 70:
        return "Good"
    elif score >= 60:
        return "Pass"
    else:
        return "Low"

def generate_labels(df, cols):
    labels = []
    for col in cols:
        unique_vals = df[col].unique()
        labels.extend([f"{col}: {val}" for val in unique_vals if f"{col}: {val}" not in labels])
    return labels

def hex_to_rgba(hex_color, alpha=0.8):
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return f"rgba({r}, {g}, {b}, {alpha})"

def build_category_color_map(df, cols):
    all_categories = []
    for col in cols:
        all_categories += [f"{col}: {val}" for val in df[col].unique()]
    palette = px.colors.qualitative.Plotly
    extended_palette = (palette * ((len(all_categories) // len(palette)) + 1))[:len(all_categories)]
    rgba_palette = [hex_to_rgba(c) for c in extended_palette]
    return dict(zip(all_categories, rgba_palette))


def build_links(df, cols, labels, category_color_map):
    source, target, values, colors = [], [], [], []
    for i in range(len(cols) - 1):
        pair_counts = df.groupby([cols[i], cols[i + 1]]).size().reset_index(name="count")
        for _, row in pair_counts.iterrows():
            src_label = f"{cols[i]}: {row[cols[i]]}"
            tgt_label = f"{cols[i + 1]}: {row[cols[i + 1]]}"
            source.append(labels.index(src_label))
            target.append(labels.index(tgt_label))
            values.append(row["count"])
            colors.append(category_color_map[src_label])
    return source, target, values, colors

def get_alluvial_diagram():
    df = preprocess.load_data()
    df = df.dropna(subset=["Family_Income", "School_Type", "Teacher_Quality", "Exam_Score"])
    df["Score_Category"] = df["Exam_Score"].apply(categorize_score)

    cols = ["Family_Income", "School_Type", "Teacher_Quality", "Score_Category"]
    labels = generate_labels(df, cols)
    category_color_map = build_category_color_map(df, cols)
    source, target, values, link_colors = build_links(df, cols, labels, category_color_map)
    node_colors = [category_color_map[label] for label in labels]

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color=node_colors
        ),
        link=dict(
            source=source,
            target=target,
            value=values,
            color=link_colors
        )
    )])

    fig.update_layout(
        title_text="Alluvial Diagram: Influence of income and School Quality on Academic Performance",
        font_size=12,
        height=600,
        width=1100,
        annotations=[dict(
            x=1.05, y=1.05, xref="paper", yref="paper",
            showarrow=False,
            text="<b>Score Categories</b><br>90–100: Excellent<br>80–89: Very Good<br>70–79: Good<br>60–69: Pass<br><60: Low",
            align="right", font=dict(size=12),
            bordercolor="black", borderwidth=1,
            bgcolor="white", opacity=0.8
        )]
    )

    return fig
