import flet as ft

border_radius = 15
width = 300
title_font_size = 20
icons_width = 38
icons_height = 38


class Scatter():
    def scatter_props(self,
                      s,
                      sr,
                      marker,
                      hue,
                      style,
                      cols,
                      cols_wrap,
                      logx,
                      logy):

        self.scatter_props_title = ft.Text("Scatter Properties",
                                           weight=ft.FontWeight.BOLD,
                                           size=title_font_size)

        self.size_label = ft.Text("Size")
        self.size_slider = ft.Slider(min=50,
                                     max=200,
                                     divisions=15,
                                     label="{value}",
                                     on_change=s)

        self.size = ft.Row(controls=[self.size_label,
                                     self.size_slider],
                           width=width,
                           alignment=ft.MainAxisAlignment.SPACE_AROUND)

        self.size_r = ft.Dropdown(label="Size relative to",
                                  options_fill_horizontally=True,
                                  width=width,
                                  border_radius=border_radius,
                                  on_change=sr)

        self.log_scalex = ft.Checkbox(label="Log-scale for X axis",
                                      height=35,
                                      on_change=logx)
        self.log_scaley = ft.Checkbox(label="Log-scale for Y axis",
                                      height=35,
                                      on_change=logy)

        self.markers_options = ["point",
                                "triangle",
                                "square",
                                "star",
                                "x",
                                "diamond"]

        self.markers_list = [ft.dropdown.Option(f"{item}") for item in self.markers_options]
        self.markers = ft.Dropdown(label="Makers",
                                   options_fill_horizontally=True,
                                   width=width,
                                   border_radius=border_radius,
                                   options=self.markers_list,
                                   visible=True,
                                   on_change=marker)

        self.hue_opts = ft.Dropdown(label="Hue",
                                    options_fill_horizontally=True,
                                    width=width,
                                    border_radius=border_radius,
                                    on_change=hue)

        self.style_opts = ft.Dropdown(label="Style",
                                      options_fill_horizontally=True,
                                      width=width,
                                      border_radius=border_radius,
                                      on_change=style)

        self.cols_label = ft.Text("Columns Wrap")
        self.cols_slider = ft.Slider(min=1,
                                     max=5,
                                     divisions=4,
                                     label="{value}",
                                     on_change=cols_wrap)
        self.scatter_cols_opts = ft.Dropdown(label="Columns",
                                             options_fill_horizontally=True,
                                             width=width,
                                             border_radius=border_radius,
                                             on_change=cols)
        self.cols_row = ft.Row(controls=[self.cols_label,
                                         self.cols_slider],
                               width=width,
                               alignment=ft.MainAxisAlignment.SPACE_AROUND)
        self.scatter_props = ft.Column(controls=[self.scatter_props_title,
                                                 self.size,
                                                 self.log_scalex,
                                                 self.log_scaley,
                                                 self.markers,
                                                 self.hue_opts,
                                                 self.style_opts,
                                                 self.size_r,
                                                 self.scatter_cols_opts,
                                                 self.cols_row],
                                       horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                       visible=False)
        return self.scatter_props
