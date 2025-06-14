import pandas as pd
import plotly.graph_objects as go
import preprocess

def get_tree_plot():
    df = preprocess.load_data()
    df = df.dropna(subset=["Peer_Influence", "Distance_from_Home", "Motivation_Level"])

    grouped = df.groupby(["Peer_Influence", "Distance_from_Home", "Motivation_Level"]).size().reset_index(name="Count")

    peer_values = sorted(df["Peer_Influence"].unique())
    distance_values = sorted(df["Distance_from_Home"].unique())
    motivation_values = sorted(df["Motivation_Level"].unique())

    x_gap = 300
    y_inner = 60

    total_leaves = len(peer_values) * len(distance_values) * len(motivation_values)
    total_height = total_leaves * y_inner
    y_start = 0

    positions = {}
    nodes = []
    edges = []

    root_id = "ROOT"
    x_root = 0
    y_root = total_height / 2
    positions[root_id] = (x_root, y_root)
    nodes.append(dict(id=root_id, label="", x=x_root, y=y_root, size=10))

    for peer in peer_values:
        peer_leaves = len(distance_values) * len(motivation_values)
        y_peer_center = y_start + (peer_leaves * y_inner) / 2
        x_peer = x_root + x_gap
        peer_id = f"Peer_{peer}"
        positions[peer_id] = (x_peer, y_peer_center)
        nodes.append(dict(id=peer_id, label=peer, x=x_peer, y=y_peer_center, size=10))
        edges.append((root_id, peer_id))

        for dist in distance_values:
            dist_leaves = len(motivation_values)
            y_dist_center = y_start + (dist_leaves * y_inner) / 2
            x_dist = x_peer + x_gap
            dist_id = f"Peer_{peer}_Dist_{dist}"
            positions[dist_id] = (x_dist, y_dist_center)
            nodes.append(dict(id=dist_id, label=dist, x=x_dist, y=y_dist_center, size=10))
            edges.append((peer_id, dist_id))

            for mot in motivation_values:
                y_leaf = y_start
                x_leaf = x_dist + x_gap
                leaf_id = f"{peer}_{dist}_{mot}"
                count = grouped.query(
                    "Peer_Influence == @peer and Distance_from_Home == @dist and Motivation_Level == @mot"
                )["Count"].sum()
                positions[leaf_id] = (x_leaf, y_leaf)
                nodes.append(dict(id=leaf_id, label=mot, x=x_leaf, y=y_leaf, size=count))
                edges.append((dist_id, leaf_id))
                y_start += y_inner

    edge_traces = []
    for src, dst in edges:
        x0, y0 = positions[src]
        x1, y1 = positions[dst]
        edge_traces.append(go.Scatter(
            x=[x0, x1], y=[y0, y1],
            mode='lines',
            line=dict(color='lightgrey'),
            hoverinfo='none',
            showlegend=False
        ))

    node_trace = go.Scatter(
        x=[n["x"] for n in nodes],
        y=[n["y"] for n in nodes],
        mode='markers+text',
        text=[n["label"] for n in nodes],
        textposition="middle right",
        marker=dict(
            size=[max(n["size"], 8) for n in nodes],
            color=['green' if n["x"] == x_gap * 3 else 'lightgrey' for n in nodes],
            sizemode='area',
            sizeref=2.*max([n["size"] for n in nodes])/40**2 if nodes else 1,
            sizemin=6
        ),
        hoverinfo='text',
        showlegend=False
    )

    fig = go.Figure(data=edge_traces + [node_trace])
    fig.update_layout(
        title="Peer Influence → Distance from Home → Motivation Level",
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        height=total_height + 100,
        width=1200,
        showlegend=False
    )
    return fig
