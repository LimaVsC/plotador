import matplotlib.pyplot as plt
import seaborn as sns
import copy
import flet as ft
import io
import base64
import numpy as np


class Plot:
    def __init__(self, data_obj, histogram_obj, line_obj, scatter_obj):
        self.data = data_obj
        self.histogram = histogram_obj
        self.line = line_obj
        self.scatter = scatter_obj

        self.page = None
        self.main_plot = ft.Image()
        self.df = None
        self.x = []
        self.y = []
        self.plot_type = ""
        self.line_style = "-"
        self.line_width = 1
        self.height = 8
        self.aspect = 1

        self.hist_kde = False
        self.log_scalex = False
        self.log_scaley = False
        self.hist_log_scalex = False
        self.hist_log_scaley = False
        self.hist_color_bar = False
        self.hist_element = "bars"
        self.hist_kind = "hist"
        self.bins = 30
        self.cols_wrap = None
        self.size = 50
        self.marker = "."
        self.x_label = None
        self.y_label = None
        self.label = None
        self.title = None
        self.hue = None
        self.cols = None
        self.style = None
        self.line_markers = False
        self.scatter_size = None
        self.hist_stats = "probability"
        self.hist_cumulative = False
        self._initial_state = copy.deepcopy(self.__dict__)

    def reset(self):
        to_keep = ["histogram",
                   "scatter",
                   "line",
                   "page",
                   "main_plot",
                   "data",
                   "df",
                   "x",
                   "y"]
        to_reset = {k: v for k, v in self._initial_state.items()
                    if k not in to_keep}

        self.__dict__.update(to_reset)
        self.data.update()

    def handle_type(self, e):
        plot_type = e.data
        if self.plot_type is not None and plot_type != self.plot_type:
            self.reset()
        if plot_type == "Histogram":
            self.histogram.hist_props.visible = True
            self.line.line_props.visible = False
            self.scatter.scatter_props.visible = False

            self.histogram.hist_props.update()
            self.line.line_props.update()
            self.scatter.scatter_props.update()

            self.get_type(e)

        elif plot_type == "Scatter":
            self.histogram.hist_props.visible = False
            self.line.line_props.visible = False
            self.scatter.scatter_props.visible = True

            self.histogram.hist_props.update()
            self.line.line_props.update()
            self.scatter.scatter_props.update()

            self.get_type(e)

        elif plot_type == "Line":
            self.histogram.hist_props.visible = False
            self.line.line_props.visible = True
            self.scatter.scatter_props.visible = False

            self.histogram.hist_props.update()
            self.line.line_props.update()
            self.scatter.scatter_props.update()

            self.get_type(e)

    def set_bins(self, e):
        self.bins = int(e.control.value)
        self.plot_update()

    def set_cols_wrap(self, e):
        self.cols_wrap = int(e.control.value)
        self.plot_update()

    def set_size(self, e):
        self.size = e.control.value
        self.plot_update()

    def set_marker(self, e):
        if e.data == "point":
            self.marker = "."
        if e.data == "triangle":
            self.marker = "^"
        if e.data == "square":
            self.marker = "s"
        if e.data == "star":
            self.marker = "*"
        if e.data == "x":
            self.marker = "x"
        if e.data == "diamond":
            self.marker = "D"
        self.plot_update()

    def set_hist_kde(self, e):
        if e.control.value:
            self.hist_kde = True
        else:
            self.hist_kde = False
        self.plot_update()

    def set_line_markers(self, e):
        if e.control.value:
            self.line_markers = True
        else:
            self.line_markers = False
        self.plot_update()

    def set_hist_log_scalex(self, e):
        if e.control.value:
            self.hist_log_scalex = True
        else:
            self.hist_log_scalex = False
        self.plot_update()

    def set_hist_log_scaley(self, e):
        if e.control.value:
            self.hist_log_scaley = True
        else:
            self.hist_log_scaley = False
        self.plot_update()

    def set_log_scalex(self, e):
        if e.control.value:
            self.log_scalex = True
        else:
            self.log_scalex = False
        self.plot_update()

    def set_log_scaley(self, e):
        if e.control.value:
            self.log_scaley = True
        else:
            self.log_scaley = False
        self.plot_update()

    def set_hist_cumulative(self, e):
        if e.control.value:
            self.hist_cumulative = True
        else:
            self.hist_cumulative = False
        self.plot_update()

    def set_hist_color_bar(self, e):
        if e.control.value:
            self.hist_color_bar = True
        else:
            self.hist_color_bar = False
        self.plot_update()

    def set_hist_element(self, e):
        if e.data == "Bars":
            self.hist_element = "bars"
        if e.data == "Step":
            self.hist_element = "step"
        if e.data == "Poly":
            self.hist_element = "poly"
        self.plot_update()

    def set_hist_kind(self, e):
        if e.data == "Histogram":
            self.hist_kind = "hist"
        if e.data == "KDE":
            self.hist_kind = "kde"
        if e.data == "eCDF":
            self.hist_kind = "ecdf"
        self.plot_update()

    def set_hist_stats(self, e):
        if e.data == "Count":
            self.hist_stats = "count"
        if e.data == "Frequency":
            self.hist_stats = "frequency"
        if e.data == "Probability":
            self.hist_stats = "probability"
        if e.data == "Percent":
            self.hist_stats = "percent"
        if e.data == "Density":
            self.hist_stats = "density"
        self.plot_update()

    def set_line_style(self, e):
        if e.data == "Line":
            self.line_style = "-"
        elif e.data == "Dash":
            self.line_style = "--"
        elif e.data == "Dash-dot":
            self.line_style = "-."
        elif e.data == "Dot":
            self.line_style = ":"
        self.plot_update()

    def set_line_width(self, e):
        self.line_width = e.control.value
        self.plot_update()

    def set_x_label(self, e):
        self.x_label = e.data
        self.plot_update()

    def set_y_label(self, e):
        self.y_label = e.data
        self.plot_update()

    def set_labels(self, e):
        self.label = e.data
        self.plot_update()

    def set_title(self, e):
        self.title = e.data
        self.plot_update()

    def set_hue(self, e):

        def handle_close(e):
            self.page.close(_dlg)

        _dlg = ft.AlertDialog(modal=True,
                              title=ft.Text("Hue list too long!"),
                              content=ft.Text("Please select another hue option."),
                              actions=[ft.TextButton("Close", on_click=handle_close)],
                              actions_alignment=ft.MainAxisAlignment.CENTER,)

        if e.data == "None":
            self.hue = None
        elif len(self.df[e.data].unique()) > 15:
            self.page.open(_dlg)
        else:
            self.hue = e.data

        self.plot_update()

    def set_cols(self, e):

        def handle_close(e):
            self.page.close(_dlg)

        _dlg = ft.AlertDialog(modal=True,
                              title=ft.Text("columns list too long!"),
                              content=ft.Text("Please select another column option."),
                              actions=[ft.TextButton("Close", on_click=handle_close)],
                              actions_alignment=ft.MainAxisAlignment.CENTER,)

        if e.data == "None":
            self.cols = None
            self.cols_wrap = None
        elif len(self.df[e.data].unique()) > 15:
            self.page.open(_dlg)
        else:
            self.cols = e.data

        self.plot_update()

    def set_scatter_size(self, e):

        def handle_close(e):
            self.page.close(_dlg)

        _dlg = ft.AlertDialog(modal=True,
                              title=ft.Text("Size list too long!"),
                              content=ft.Text("Please select another size option."),
                              actions=[ft.TextButton("Close", on_click=handle_close)],
                              actions_alignment=ft.MainAxisAlignment.CENTER,)

        if e.data == "None":
            self.scatter_size = None
        elif len(self.df[e.data].unique()) > 15:
            self.page.open(_dlg)
        else:
            self.scatter_size = e.data

        self.plot_update()

    def set_style(self, e):

        def handle_close(e):
            self.page.close(_dlg)

        _dlg = ft.AlertDialog(modal=True,
                              title=ft.Text("Style list too long!"),
                              content=ft.Text("Please select another style option."),
                              actions=[ft.TextButton("Close", on_click=handle_close)],
                              actions_alignment=ft.MainAxisAlignment.CENTER,)

        if e.data == "None":
            self.style = None
        elif len(self.df[e.data].unique()) > 15:
            self.page.open(_dlg)
        else:
            self.style = e.data

        self.plot_update()

    def get_x(self, e):
        if e.data != "None":
            self.x = e.data
        else:
            self.x = None
        self.plot_update()

    def get_y(self, e):
        if e.data != "None":
            self.y = e.data
        else:
            self.y = None
        self.plot_update()

    def get_type(self, e):
        self.plot_type = e.data
        self.plot_update()

    def aply_label_changes(self, g):
        if self.log_scalex:
            if self.x_label is not None:
                _xl = f"log({self.x_label})"
            else:
                _xl = f"log({self.x})"
        else:
            if self.x_label is not None:
                _xl = self.x_label
            else:
                _xl = self.x

        if self.log_scaley:
            if self.y_label is not None:
                _yl = f"log({self.y_label})"
            else:
                _yl = f"log({self.y})"
        else:
            if self.y_label is not None:
                _yl = self.y_label
            else:
                _yl = self.y

        if self.title is not None:
            g.set(title=self.title)

        g.set_axis_labels(x_var=_xl)
        g.set_axis_labels(y_var=_yl)

    def plot_hist(self):
        if self.y:
            kwargs = {"cbar": self.hist_color_bar}

            self.histogram.bins_row.disabled = True
            self.histogram.kde.disabled = True
            self.histogram.cumulative.disabled = True
            self.histogram.hist_elements.disabled = True
            self.histogram.hist_stats.disabled = True
            self.histogram.color_bar.disabled = False
            self.histogram.hist_props.update()

            if self.hist_kind == "kde":
                kwargs["fill"] = True
        else:
            if self.hist_kind == "hist":
                self.histogram.bins_row.disabled = False
                self.histogram.kde.disabled = False
                self.histogram.cumulative.disabled = False
                self.histogram.hist_elements.disabled = False
                self.histogram.hist_stats.disabled = False
                self.histogram.color_bar.disabled = True

                kwargs = {"bins": self.bins,
                          "stat": self.hist_stats,
                          "cumulative": self.hist_cumulative,
                          "kde": self.hist_kde,
                          "element": self.hist_element}
            elif self.hist_kind == "ecdf":
                self.histogram.bins_row.disabled = True
                self.histogram.kde.disabled = True
                self.histogram.cumulative.disabled = True
                self.histogram.hist_stats.disabled = True
                self.histogram.hist_elements.disabled = True

                kwargs = {}
            elif self.hist_kind == "kde":
                self.histogram.bins_row.disabled = True
                self.histogram.kde.disabled = True
                self.histogram.cumulative.disabled = True
                self.histogram.hist_stats.disabled = True
                self.histogram.hist_elements.disabled = True

                kwargs = {}

            self.histogram.hist_props.update()

        g = sns.displot(data=self.df,
                        x=self.x,
                        y=self.y,
                        hue=self.hue,
                        log_scale=(self.hist_log_scalex, self.hist_log_scaley),
                        legend=True,
                        kind=self.hist_kind,
                        height=self.height,
                        aspect=self.aspect,
                        col=self.cols,
                        col_wrap=self.cols_wrap,
                        **kwargs)

        if self.x_label is not None:
            g.set_axis_labels(x_var=self.x_label)
        if self.y and self.y_label is not None:
            g.set_axis_labels(y_var=self.y_label)
        if self.title is not None:
            g.set_titles(template=self.title)

        g.tight_layout(pad=3.0)
        buf = io.BytesIO()
        g.figure.savefig(buf, format="png")
        buf.seek(0)
        image_data = base64.b64encode(buf.getvalue()).decode()
        self.main_plot.src_base64 = image_data

        self.main_plot.update()

    def plot_scatter(self):

        if self.log_scalex is True:
            _x = np.log(self.df[self.x])
        elif self.log_scalex is False:
            _x = self.x

        if self.log_scaley is True:
            _y = np.log(self.df[self.y])
        elif self.log_scaley is False:
            _y = self.y

        g = sns.relplot(data=self.df,
                        x=_x,
                        y=_y,
                        hue=self.hue,
                        style=self.style,
                        s=self.size,
                        size=self.scatter_size,
                        sizes=(100, 1000),
                        marker=self.marker,
                        legend=True,
                        col=self.cols,
                        col_wrap=self.cols_wrap,
                        height=self.height,
                        aspect=self.aspect)

        self.aply_label_changes(g=g)

        g.tight_layout(pad=3.0)
        buf = io.BytesIO()
        g.figure.savefig(buf, format="png")
        buf.seek(0)
        image_data = base64.b64encode(buf.getvalue()).decode()
        self.main_plot.src_base64 = image_data

        self.main_plot.update()

    def plot_line(self):
        if self.log_scalex is True:
            _x = np.log(self.df[self.x])
        elif self.log_scalex is False:
            _x = self.x

        if self.log_scaley is True:
            _y = np.log(self.df[self.y])
        elif self.log_scaley is False:
            _y = self.y

        g = sns.relplot(data=self.df,
                        x=_x,
                        y=_y,
                        hue=self.hue,
                        style=self.style,
                        markers=self.line_markers,
                        linestyle=self.line_style,
                        linewidth=self.line_width,
                        col=self.cols,
                        col_wrap=self.cols_wrap,
                        height=self.height,
                        aspect=self.aspect,
                        kind="line")

        self.aply_label_changes(g=g)

        g.tight_layout(pad=3.0)
        buf = io.BytesIO()
        g.figure.savefig(buf, format="png")
        buf.seek(0)
        image_data = base64.b64encode(buf.getvalue()).decode()
        self.main_plot.src_base64 = image_data

        self.main_plot.update()

    def plot_update(self):
        if self.plot_type == "Histogram":
            self.plot_hist()
        elif self.plot_type == "Scatter":
            self.plot_scatter()
        elif self.plot_type == "Line":
            self.plot_line()

    def save_plot(self, path):
        plt.savefig(path)
