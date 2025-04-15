import flet as ft


border_radius = 15
width = 300
title_font_size = 20
icons_width = 38
icons_height = 38


class Line():

    def line_props(self,
                   lw,
                   lm,
                   ls,
                   style,
                   hue,
                   cols,
                   cols_wrap,
                   logx,
                   logy):

        self.line_props_title = ft.Text("Line Properties",
                                        weight=ft.FontWeight.BOLD,
                                        size=title_font_size)
        self.width_label = ft.Text("Line width")
        self.width_slider = ft.Slider(min=1,
                                      max=5,
                                      divisions=5,
                                      label="{value}",
                                      on_change=lw)

        self.cols_label = ft.Text("Columns Wrap")
        self.cols_slider = ft.Slider(min=1,
                                     max=5,
                                     divisions=4,
                                     label="{value}",
                                     on_change=cols_wrap)
        self.line_markers = ft.Checkbox(label="Add line markers",
                                        height=35,
                                        on_change=lm)
        self.line_options = ['Line',
                             'Dash',
                             'Dash-dot',
                             'Dot']

        self.log_scalex = ft.Checkbox(label="Log-scale for X axis",
                                      height=35,
                                      on_change=logx)
        self.log_scaley = ft.Checkbox(label="Log-scale for Y axis",
                                      height=35,
                                      on_change=logy)

        self.line_hue_opts = ft.Dropdown(label="Hue",
                                         options_fill_horizontally=True,
                                         width=width,
                                         border_radius=border_radius,
                                         on_change=hue)

        self.line_cols_opts = ft.Dropdown(label="Columns",
                                          options_fill_horizontally=True,
                                          width=width,
                                          border_radius=border_radius,
                                          on_change=cols)
        self.line_style_opts = ft.Dropdown(label="Style",
                                           options_fill_horizontally=True,
                                           width=width,
                                           border_radius=border_radius,
                                           on_change=style)

        self.line_style_list = [ft.dropdown.Option(f"{item}") for item in self.line_options]

        self.line_style = ft.Dropdown(label="Line Style",
                                      options_fill_horizontally=True,
                                      width=width,
                                      border_radius=border_radius,
                                      options=self.line_style_list,
                                      visible=True,
                                      on_change=ls)
        self.line_width_row = ft.Row(controls=[self.width_label,
                                               self.width_slider],
                                     width=width,
                                     alignment=ft.MainAxisAlignment.SPACE_AROUND)

        self.cols_row = ft.Row(controls=[self.cols_label,
                                         self.cols_slider],
                               width=width,
                               alignment=ft.MainAxisAlignment.SPACE_AROUND)
        self.line_props = ft.Column(controls=[self.line_props_title,
                                              self.line_width_row,
                                              self.log_scalex,
                                              self.log_scaley,
                                              self.line_markers,
                                              self.line_style,
                                              self.line_hue_opts,
                                              self.line_style_opts,
                                              self.line_cols_opts,
                                              self.cols_row],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    visible=False)
        return self.line_props
