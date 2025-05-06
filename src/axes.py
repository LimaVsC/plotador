import flet as ft
from config import (border_radius, width, title_font_size)


class Axes():

    def axes_props(self, handle_type, getx, gety,
                   xlabel, x_reset, ylabel, y_reset, title, title_reset):

        self.props_title = ft.Text("General Properties",
                                   weight=ft.FontWeight.BOLD,
                                   size=title_font_size)
        self.plot_type = ft.Dropdown(label="Plot Type",
                                     options_fill_horizontally=True,
                                     width=300,
                                     border_radius=border_radius,
                                     options=[ft.dropdown.Option("Line"),
                                              ft.dropdown.Option("Scatter"),
                                              ft.dropdown.Option("Distribution"),
                                              ft.dropdown.Option("Categorical")],
                                     on_change=handle_type)

        self.axes_title = ft.Text("Plot type and Axes",
                                  weight=ft.FontWeight.BOLD,
                                  size=title_font_size)

        self.x_axis = ft.Dropdown(label="X Axis",
                                  options_fill_horizontally=True,
                                  width=width,
                                  border_radius=border_radius,
                                  on_change=getx)

        self.y_axis = ft.Dropdown(label="Y Axis",
                                  options_fill_horizontally=True,
                                  width=width,
                                  border_radius=border_radius,
                                  on_change=gety)

        self.x_label_reset = ft.IconButton(icon=ft.Icons.AUTORENEW,
                                           on_click=x_reset)
        self.x_label = ft.TextField(label="X Label",
                                    border_radius=border_radius,
                                    suffix_icon=self.x_label_reset,
                                    width=width,
                                    on_submit=xlabel,
                                    )

        self.y_label_reset = ft.IconButton(icon=ft.Icons.AUTORENEW,
                                           on_click=y_reset)
        self.y_label = ft.TextField(label="Y Label",
                                    border_radius=border_radius,
                                    suffix_icon=self.y_label_reset,
                                    width=width,
                                    on_submit=ylabel)

        self.title_reset = ft.IconButton(icon=ft.Icons.AUTORENEW,
                                         on_click=title_reset)
        self.plot_title = ft.TextField(label="Plot Title",
                                       border_radius=border_radius,
                                       suffix_icon=self.title_reset,
                                       width=width,
                                       on_submit=title)
