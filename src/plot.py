import matplotlib.pyplot as plt
import seaborn as sns
import copy
import flet as ft
import io
import base64
import numpy as np


class Plot:
    def __init__(self, histogram_obj, line_obj, scatter_obj):
        self.histogram = histogram_obj
        self.line = line_obj
        self.scatter = scatter_obj

        # self.hist_props = None
        # self.scatter_props = None
        # self.line_props = None

        self.page = None
        self.main_plot = ft.Image()
        self.ax = None
        self.df = None
        self.x = []
        self.y = []
        self.plot_type = ""
        self.line_style = "-"
        self.line_width = 1
        self.height = 8
        self.aspect = 1

        # properties of plots
        self.hist_kde = False
        self.hist_log_scalex = False
        self.hist_log_scaley = False
        self.scatter_log_scalex = False
        self.scatter_log_scaley = False
        self.line_log_scalex = False
        self.line_log_scaley = False
        self.hist_color_bar = False
        self.hist_element = "bars"
        self.hist_kind = "hist"
        self.bins = 30
        self.cols_wrap = None
        self.size = 50
        self.marker = "."
        self.color = "b"
        self.dark_theme = False
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
        self.__dict__.update(self._initial_state)

    def handle_type(self, e):
        plot_type = e.data
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

    # Set functions
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

    def set_scatter_log_scalex(self, e):
        if e.control.value:
            self.scatter_log_scalex = True
        else:
            self.scatter_log_scalex = False
        self.plot_update()

    def set_scatter_log_scaley(self, e):
        if e.control.value:
            self.scatter_log_scaley = True
        else:
            self.scatter_log_scaley = False
        self.plot_update()

    def set_line_log_scalex(self, e):
        if e.control.value:
            self.line_log_scalex = True
        else:
            self.line_log_scalex = False
        self.plot_update()

    def set_line_log_scaley(self, e):
        if e.control.value:
            self.line_log_scaley = True
        else:
            self.line_log_scaley = False
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

    def set_color(self, e):
        if e.data == "Blue":
            self.color = "b"
        elif e.data == "Green":
            self.color = "g"
        elif e.data == "Red":
            self.color = "r"
        elif e.data == "Cyan":
            self.color = "c"
        elif e.data == "Magenta":
            self.color = "m"
        elif e.data == "Yellow":
            self.color = "y"
        elif e.data == "Black":
            self.color = "k"
        elif e.data == "White":
            self.color = "w"
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

    # Get functions
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

    # Plot funtions
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

        buf = io.BytesIO()
        g.figure.savefig(buf, format="png")
        buf.seek(0)
        image_data = base64.b64encode(buf.getvalue()).decode()
        self.main_plot.src_base64 = image_data

        self.main_plot.update()

    def plot_scatter(self):

        if self.scatter_log_scalex is True:
            _x = np.log(self.df[self.x])
        elif self.scatter_log_scalex is False:
            _x = self.x

        if self.scatter_log_scaley is True:
            _y = np.log(self.df[self.y])
        elif self.scatter_log_scaley is False:
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
                        color=self.color,
                        legend=True,
                        col=self.cols,
                        col_wrap=self.cols_wrap,
                        height=self.height,
                        aspect=self.aspect)

        if self.x_label is not None:
            g.set_axis_labels(x_var=self.x_label)
        if self.title is not None:
            g.set_titles(template=self.title)
        if self.y_label is not None:
            g.set_axis_labels(y_var=self.y_label)

        buf = io.BytesIO()
        g.figure.savefig(buf, format="png")
        buf.seek(0)
        image_data = base64.b64encode(buf.getvalue()).decode()
        self.main_plot.src_base64 = image_data

        self.main_plot.update()

    def plot_line(self):
        if self.line_log_scalex is True:
            _x = np.log(self.df[self.x])
        elif self.line_log_scalex is False:
            _x = self.x

        if self.line_log_scaley is True:
            _y = np.log(self.df[self.y])
        elif self.line_log_scaley is False:
            _y = self.y

        g = sns.relplot(data=self.df,
                        x=_x,
                        y=_y,
                        color=self.color,
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

        if self.x_label is not None:
            g.set_axis_labels(x_var=self.x_label)
        if self.title is not None:
            g.set_titles(template=self.title)
        if self.y_label is not None:
            g.set_axis_labels(y_var=self.y_label)

        buf = io.BytesIO()
        g.figure.savefig(buf, format="png")
        buf.seek(0)
        image_data = base64.b64encode(buf.getvalue()).decode()
        self.main_plot.src_base64 = image_data

        self.main_plot.update()

    # Update functions
    def plot_update(self):
        if self.plot_type == "Histogram":
            self.plot_hist()
        elif self.plot_type == "Scatter":
            self.plot_scatter()
        elif self.plot_type == "Line":
            self.plot_line()

    def save_plot(self, path):
        plt.savefig(path)
