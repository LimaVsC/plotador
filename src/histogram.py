import flet as ft
from config import (border_radius, width, title_font_size)


class Histogram():

    def hist_props(self, bins, kde, logx, logy, c, cbar, stats, element, hue,
                   cols, cols_wrap, kind):

        self.title = ft.Text("Histogram Properties",
                             weight=ft.FontWeight.BOLD,
                             size=title_font_size)
        self.bins_label = ft.Text("Bins")
        self.bins_slider = ft.Slider(min=10,
                                     max=50,
                                     divisions=4,
                                     value=30,
                                     label="{value}",

                                     on_change=bins)

        self.cols_label = ft.Text("Columns Wrap")
        self.cols_slider = ft.Slider(min=1,
                                     max=5,
                                     divisions=4,
                                     label="{value}",
                                     value=1,
                                     on_change=cols_wrap)

        self.kde = ft.Checkbox(label="Add KDE plot",
                               height=35,
                               on_change=kde)

        self.hist_hue_opts = ft.Dropdown(label="Hue",
                                         options_fill_horizontally=True,
                                         width=width,
                                         border_radius=border_radius,
                                         on_change=hue)
        self.hist_cols_opts = ft.Dropdown(label="Columns",
                                          options_fill_horizontally=True,
                                          width=width,
                                          border_radius=border_radius,
                                          on_change=cols)

        self.log_scalex = ft.Checkbox(label="Log-scale for X axis",
                                      height=35,
                                      on_change=logx)
        self.log_scaley = ft.Checkbox(label="Log-scale for Y axis",
                                      height=35,
                                      on_change=logy)

        self.cumulative = ft.Checkbox(label="Cumulative",
                                      height=35,
                                      on_change=c)

        self.color_bar = ft.Checkbox(label="Add a color bar",
                                     height=35,
                                     on_change=cbar)

        self.hist_stats_opts = ["Count",
                                "Frequency",
                                "Probability",
                                "Percent",
                                "Density"]
        self.hist_stats_list = [ft.dropdown.Option(f"{item}") for item in self.hist_stats_opts]
        self.hist_stats = ft.Dropdown(label="Hist stats",
                                      options_fill_horizontally=True,
                                      width=width,
                                      border_radius=border_radius,
                                      options=self.hist_stats_list,
                                      value="Probability",
                                      on_change=stats)

        self.hist_element_opts = ["Bars", "Step", "Poly"]
        self.hist_element_list = [ft.dropdown.Option(f"{item}") for item in self.hist_element_opts]
        self.hist_elements = ft.Dropdown(label="Hist element",
                                         options_fill_horizontally=True,
                                         width=width,
                                         border_radius=border_radius,
                                         options=self.hist_element_list,
                                         value="Bars",
                                         on_change=element)

        self.hist_kind_opts = ["Histogram", "KDE", "eCDF"]
        self.hist_kind_list = [ft.dropdown.Option(f"{item}") for item in self.hist_kind_opts]
        self.hist_kinds = ft.Dropdown(label="Hist kind",
                                      options_fill_horizontally=True,
                                      width=width,
                                      border_radius=border_radius,
                                      options=self.hist_kind_list,
                                      value="Histogram",
                                      on_change=kind)

        self.bins_row = ft.Row(controls=[self.bins_label,
                                         self.bins_slider],
                               width=width,
                               alignment=ft.MainAxisAlignment.SPACE_AROUND)

        self.cols_row = ft.Row(controls=[self.cols_label,
                                         self.cols_slider],
                               width=width,
                               alignment=ft.MainAxisAlignment.SPACE_AROUND)

        self.checkbox_col = ft.Column(controls=[self.kde,
                                                self.cumulative,
                                                self.log_scalex,
                                                self.log_scaley,
                                                self.color_bar,],
                                      alignment=ft.MainAxisAlignment.START)

        self.hist_props = ft.Column(controls=[self.title,
                                              self.bins_row,
                                              self.checkbox_col,
                                              self.hist_kinds,
                                              self.hist_stats,
                                              self.hist_elements,
                                              self.hist_hue_opts,
                                              self.hist_cols_opts,
                                              self.cols_row],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    visible=False)
        self.hist_kind_opts = ["Histogram", "KDE", "eCDF"]
        self.hist_kind_list = [ft.dropdown.Option(f"{item}") for item in self.hist_kind_opts]
        self.hist_kinds = ft.Dropdown(label="Hist kind",
                                      options_fill_horizontally=True,
                                      width=width,
                                      border_radius=border_radius,
                                      options=self.hist_kind_list,
                                      on_change=kind)

        return self.hist_props
