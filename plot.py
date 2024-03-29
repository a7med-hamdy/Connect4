from igraph import Graph, Vertex
import plotly.graph_objects as go
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets





class Plotter(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QtWidgets.QPushButton('Plot', self)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)

        self.button.clicked.connect(self.show_graph)
        self.resize(1000,800)

        self.vertices = None
        self.edges = None
        self.text = None
        self.labels = None
        self.max = None
        self.min = None
        self.terminal = None

    def set_param(self, l , E, unique,s, maxi, mini, terminal):
        self.labels = l
        self.vertices = unique
        self.edges = E
        self.text = s
        self.max = maxi
        self.min = mini
        self.terminal = terminal

    def show_graph(self):
        if self.edges is None or self.vertices is None:
            return

        G = Graph(n = len(self.vertices), edges = self.edges, directed = False)

        lay = G.layout_reingold_tilford(root = [self.vertices[0]])

        position = {k: lay[k] for k in self.vertices}
        
        Y = [lay[k][1] for k in self.vertices]
        M = max(Y)

        Xmax = [position[k][0] for k in self.max]
        Ymax = [2*M-position[k][1] for k in self.max]

        Xmin = [position[k][0] for k in self.min]
        Ymin = [2*M-position[k][1] for k in self.min]

        Xt = [position[k][0] for k in self.terminal]
        Yt = [2*M-position[k][1] for k in self.terminal]

        Xe = []
        Ye = []
        for edge in self.edges:
            Xe+=[position[edge[0]][0],position[edge[1]][0], None]
            Ye+=[2*M-position[edge[0]][1],2*M-position[edge[1]][1], None]


        axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
                    zeroline=False,
                    showgrid=False,
                    showticklabels=False,
                    )

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=Xe,
                        y=Ye,
                        mode='lines',
                        line=dict(color='rgb(210,210,210)', width=1),
                        hoverinfo='none'
                        ))

        fig.add_trace(go.Scatter(x=Xmax,
                        y=Ymax,
                        mode='markers',
                        name='node',
                        marker=dict(symbol='triangle-up-dot',
                                        size=25,
                                        color='rgb(255,0,0)',    #'#DB4551',
                                        line=dict(color='rgb(50,50,50)', width=1)
                                        ),
                        opacity=0.8
                        ))

        fig.add_trace(go.Scatter(x=Xt,
                        y=Yt,
                        mode='markers',
                        name='node',
                        marker=dict(symbol='square-dot',
                                        size=17,
                                        color='rgb(0,255,0)',    #'#DB4551',
                                        line=dict(color='rgb(50,50,50)', width=1)
                                        ),
                        opacity=0.8
                        ))
                        
        fig.add_trace(go.Scatter(x=Xmin,
                        y=Ymin,
                        mode='markers',
                        name='node',
                        marker=dict(symbol='triangle-down-dot',
                                        size=25,
                                        color='#6175c1',    #'#DB4551',
                                        line=dict(color='rgb(50,50,50)', width=1)
                                        ),
                        opacity=0.8
                        ))


        def make_annotations(pos, font_size=10, font_color='rgb(0,0,0)'):
            annotations = []
            for k in range(len(self.labels)):
                annotations.append(
                    dict(
                        text=str(self.labels[k]), # or replace labels with a different list for the text within the circle
                        x=pos[self.vertices[k]][0], y=2*M-position[self.vertices[k]][1],
                        xref='x1', yref='y1',
                        font=dict(color=font_color, size=font_size),
                        showarrow=False)
                )
            return annotations

        fig.update_layout(title= self.text,
                    annotations=make_annotations(position),
                    font_size=12,
                    showlegend=False,
                    xaxis=axis,
                    yaxis=axis,
                    margin=dict(l=40, r=40, b=85, t=100),
                    hovermode='closest',
                    plot_bgcolor='rgb(248,248,248)'
                    )

        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))


