import flet as ft
import seaborn as sns
import io
import base64
import pandas as pd

from plot import Plot
from data import Data
from axes import Axes
from loading import LoadingOverlay
from file_monitor import Monitor
from file_picker import FilePicker
from config import (icons_width, icons_height)

from scatter import Scatter
from line import Line
from histogram import Histogram

sns.set_theme(style="darkgrid")


def main(page):
    page.title = "Plotador"
    primary_color = ft.Colors.INDIGO
    on_primary_color = ft.Colors.WHITE
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(
                            primary=primary_color,
                            on_primary=on_primary_color,
                            primary_container=primary_color,
                            on_primary_container=on_primary_color,
                                                      ),
                          visual_density=ft.VisualDensity.COMFORTABLE,
                          )

    github_icon = ft.Image(src="icons/github.svg",
                           width=icons_width,
                           height=icons_height,
                           tooltip="Github")
    buy_me_a_coffee_icon = ft.Image(src="icons/buymeacoffee.svg",
                                    width=icons_width,
                                    height=icons_height,
                                    tooltip="Buy me a coffee")
    page.appbar = ft.AppBar(
        elevation=4,
        title=ft.Text("Plotador",
                      weight=ft.FontWeight.BOLD,),
        center_title=False,
        actions=[ft.IconButton(content=github_icon,
                               url="https://github.com/seu-repositorio"),
                 ft.IconButton(content=buy_me_a_coffee_icon,
                               url="https://www.paypal.com/donate/?business=EENWCL2V74NTC&no_recurring=0&currency_code=BRL")],)

    buf = io.BytesIO()
    g = sns.FacetGrid(data=pd.DataFrame(), height=8, aspect=1)
    g.figure.savefig(buf, format="png")
    fig = ft.Image(src_base64=base64.b64encode(buf.getvalue()).decode())

    scatter = Scatter()
    line = Line()
    histogram = Histogram()
    data = Data()
    axes = Axes()
    plot = Plot(data_obj=data,
                histogram_obj=histogram,
                line_obj=line,
                scatter_obj=scatter)

    loading_overlay = LoadingOverlay()
    monitor = Monitor(".", "", None)
    monitor.start()
    file_picker = FilePicker(page,
                             data,
                             plot,
                             loading_overlay,
                             monitor)
    scatter_props = scatter.scatter_props(plot.set_size,
                                          plot.set_scatter_size,
                                          plot.set_marker,
                                          plot.set_hue,
                                          plot.set_style,
                                          plot.set_cols,
                                          plot.set_cols_wrap,
                                          plot.set_log_scalex,
                                          plot.set_log_scaley)

    line_props = line.line_props(plot.set_line_width,
                                 plot.set_line_markers,
                                 plot.set_line_style,
                                 plot.set_style,
                                 plot.set_hue,
                                 plot.set_cols,
                                 plot.set_cols_wrap,
                                 plot.set_log_scalex,
                                 plot.set_log_scaley)

    hist_props = histogram.hist_props(plot.set_bins,
                                      plot.set_hist_kde,
                                      plot.set_hist_log_scalex,
                                      plot.set_hist_log_scaley,
                                      plot.set_hist_cumulative,
                                      plot.set_hist_color_bar,
                                      plot.set_hist_stats,
                                      plot.set_hist_element,
                                      plot.set_hue,
                                      plot.set_cols,
                                      plot.set_cols_wrap,
                                      plot.set_hist_kind)

    axes.axes_props(plot.handle_type,
                    plot.get_x,
                    plot.get_y,
                    plot.set_x_label,
                    plot.set_y_label,
                    plot.set_labels,
                    plot.set_title)

    plot.main_plot = fig
    plot.page = page
    data.page = page
    plot.ax = g.ax

    file_picker.file_picker.on_result = file_picker.read_file_loading_screen
    file_picker.overlay_append()
    save_file_dialog = ft.FilePicker(on_result=file_picker.save_file_result)

    page.overlay.extend([save_file_dialog])

    data.x_axis = axes.x_axis
    data.y_axis = axes.y_axis

    data.hist_hue_opts = histogram.hist_hue_opts
    data.scatter_hue_opts = scatter.hue_opts
    data.line_hue_opts = line.line_hue_opts

    data.hist_cols_opts = histogram.hist_cols_opts
    data.scatter_cols_opts = scatter.scatter_cols_opts
    data.line_cols_opts = line.line_cols_opts

    data.scatter_style_opts = scatter.style_opts
    data.line_style_opts = line.line_style_opts

    data.scatter_size_opts = scatter.size_r

    add_file = ft.FloatingActionButton(icon=ft.Icons.ADD,
                                       on_click=file_picker.pick_file)
    save_plot = ft.FloatingActionButton(icon=ft.Icons.SAVE,
                                        on_click=lambda _: save_file_dialog.save_file())

    buttons = ft.Row([add_file, save_plot],
                     expand=1,
                     alignment=ft.MainAxisAlignment.SPACE_AROUND)

    col = ft.Column([ft.Container(fig, expand=4), buttons],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    general_props = ft.Column(controls=[axes.props_title,
                                        axes.plot_title,
                                        axes.x_label,
                                        axes.y_label,],
                              alignment=ft.MainAxisAlignment.CENTER,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    props = ft.Column([axes.axes_title,
                      axes.plot_type,
                      axes.x_axis,
                      axes.y_axis,
                      general_props,
                      line_props,
                      scatter_props,
                      hist_props,],
                      alignment=ft.MainAxisAlignment.CENTER,
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                      scroll=True)
    plot_props = ft.Column([
                      line_props,
                      scatter_props,
                      hist_props,],
                      alignment=ft.MainAxisAlignment.CENTER,
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                      scroll=True)

    t = ft.Tabs(selected_index=0,
                animation_duration=300,
                tab_alignment=ft.TabAlignment.CENTER,
                tabs=[ft.Tab(text="Axes", content=props),
                      ft.Tab(text="Properties", content=plot_props)],)

    def handle_window_event(e):
        if e.data == "close":
            monitor.stop()
            page.window.destroy()

    page.window.prevent_close = True
    page.window.on_event = handle_window_event

    page.add(ft.Stack([ft.Row([ft.Container(content=col, expand=1),
                               ft.VerticalDivider(),
                               ft.Container(content=t,
                                            alignment=ft.alignment.top_center,
                                            width=300)],
                              spacing=10,
                              expand=True),
                       loading_overlay],
                      expand=True))


ft.app(target=main, assets_dir="assets")
