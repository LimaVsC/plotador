import flet as ft
from config import (border_radius, width, title_font_size)


class Axes():

    def axes_props(self, handle_type, getx, gety,
                   xlabel, ylabel, labels, title):

        # Props title
        self.props_title = ft.Text("General Properties",
                                   weight=ft.FontWeight.BOLD,
                                   size=title_font_size)
        # Plot Type
        self.plot_type = ft.Dropdown(label="Plot Type",
                                     options_fill_horizontally=True,
                                     width=300,
                                     border_radius=border_radius,
                                     options=[ft.dropdown.Option("Line"),
                                              ft.dropdown.Option("Scatter"),
                                              ft.dropdown.Option("Histogram")],
                                     on_change=handle_type)

        # ***************************************************************************
        # Axes

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

        self.x_label = ft.TextField(label="X Label",
                                    border_radius=border_radius,
                                    width=width,
                                    on_submit=xlabel)

        # Y label
        self.y_label = ft.TextField(label="Y Label",
                                    border_radius=border_radius,
                                    width=width,
                                    on_submit=ylabel)

        # Title
        self.plot_title = ft.TextField(label="Plot Title",
                                       border_radius=border_radius,
                                       width=width,
                                       on_submit=title)
