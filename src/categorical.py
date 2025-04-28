import flet as ft
from config import (border_radius, width, title_font_size)


class Categorical():

    def categorical_props(self, log, kind, hue, cols, cols_wrap):
        self.title = ft.Text("Categorical Properties",
                             weight=ft.FontWeight.BOLD,
                             size=title_font_size)

        self.log_scale = ft.Checkbox(label="Log-scale for X axis",
                                     height=35,
                                     on_change=log)

        self.cat_kind_opts = ["Strip",
                              "Swarm",
                              "Box",
                              "Violin",
                              "Boxen",
                              "Point",
                              "Bar",
                              "Count"]
        self.cat_kind_list = [ft.dropdown.Option(f"{item}")
                              for item in self.cat_kind_opts]
        self.cat_kinds = ft.Dropdown(label="Kind",
                                     options_fill_horizontally=True,
                                     width=width,
                                     border_radius=border_radius,
                                     options=self.cat_kind_list,
                                     value="Strip",
                                     on_change=kind)

        self.cat_hue_opts = ft.Dropdown(label="Hue",
                                        options_fill_horizontally=True,
                                        width=width,
                                        border_radius=border_radius,
                                        on_change=hue)

        self.cols_label = ft.Text("Columns Wrap")
        self.cols_slider = ft.Slider(min=1,
                                     max=5,
                                     divisions=4,
                                     label="{value}",
                                     value=1,
                                     on_change=cols_wrap)
        self.cat_cols_opts = ft.Dropdown(label="Columns",
                                         options_fill_horizontally=True,
                                         width=width,
                                         border_radius=border_radius,
                                         on_change=cols)
        self.cols_row = ft.Row(controls=[self.cols_label,
                                         self.cols_slider],
                               width=width,
                               alignment=ft.MainAxisAlignment.SPACE_AROUND)

        self.checkbox_col = ft.Column(controls=[self.log_scale],
                                      alignment=ft.MainAxisAlignment.START)

        self.cat_props = ft.Column(controls=[self.title,
                                             self.checkbox_col,
                                             self.cat_kinds,
                                             self.cat_hue_opts,
                                             self.cat_cols_opts,
                                             self.cols_row],
                                   horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                   visible=False)
        return self.cat_props
