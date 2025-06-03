import pandas as pd
import flet as ft
import csv


class Data:
    def __init__(self):
        self.page = None
        self.df = pd.DataFrame()
        self.x_axis = None
        self.y_axis = None
        self.hist_hue_opts = None
        self.scatter_hue_opts = None
        self.line_hue_opts = None
        self.hist_cols_opts = None
        self.scatter_cols_opts = None
        self.line_cols_opts = None
        self.scatter_style_opts = None
        self.line_style_opts = None
        self.scatter_size_opts = None

    def read_csv(self, path):
        with open(path, newline="") as f:
            header = csv.Sniffer().has_header(f.read(2048))
            f.seek(0)
            dialect = csv.Sniffer().sniff(f.read(2048))
            f.seek(0)
            sep = dialect.delimiter if dialect.delimiter != "." else ","
            if header:
                return pd.read_csv(f, sep=sep)
            else:
                return pd.read_csv(f, sep=sep, header=None)

    def read_excel(self, path):
        return pd.read_excel(path)

    def read_file_handler(self, name, path):
        if name.endswith(".xlsx") or name.endswith(".xls"):
            self.df = self.read_excel(path)
        else:
            self.df = self.read_csv(path)
            if type(self.df.columns[0]) is not str:
                self.df.columns = self.df.columns.map(str)
        self.set_opts()

    def set_opts(self):
        _x_opts = list(self.df.columns)
        _x_opts.insert(0, "None")

        _y_opts = list(self.df.columns)
        _y_opts.insert(0, "None")

        _hue_opts = list(self.df.columns)
        _hue_opts.insert(0, "None")
        _cols_opts = list(self.df.columns)
        _cols_opts.insert(0, "None")

        self.x_axis.options = [ft.dropdown.Option(f"{item}")
                               for item in _x_opts]
        self.y_axis.options = [ft.dropdown.Option(f"{item}")
                               for item in _y_opts]

        self.hist_hue_opts.options = [ft.dropdown.Option(f"{item}")
                                      for item in _hue_opts]
        self.scatter_hue_opts.options = [ft.dropdown.Option(f"{item}")
                                         for item in _hue_opts]
        self.line_hue_opts.options = [ft.dropdown.Option(f"{item}")
                                      for item in _hue_opts]
        self.cat_hue_opts.options = [ft.dropdown.Option(f"{item}")
                                     for item in _hue_opts]

        self.hist_cols_opts.options = [ft.dropdown.Option(f"{item}")
                                       for item in _cols_opts]
        self.scatter_cols_opts.options = [ft.dropdown.Option(f"{item}")
                                          for item in _cols_opts]
        self.line_cols_opts.options = [ft.dropdown.Option(f"{item}")
                                       for item in _cols_opts]
        self.cat_cols_opts.options = [ft.dropdown.Option(f"{item}")
                                      for item in _cols_opts]

        self.scatter_style_opts.options = [ft.dropdown.Option(f"{item}")
                                           for item in _hue_opts]
        self.line_style_opts.options = [ft.dropdown.Option(f"{item}")
                                        for item in _hue_opts]

        self.scatter_size_opts.options = [ft.dropdown.Option(f"{item}")
                                          for item in _hue_opts]
        self.scatter_size_opts.options = [ft.dropdown.Option(f"{item}")
                                          for item in _hue_opts]
        self.update()

    def update(self):
        self.x_axis.update()
        self.y_axis.update()

        self.hist_hue_opts.update()
        self.scatter_hue_opts.update()
        self.line_hue_opts.update()
        self.cat_hue_opts.update()

        self.scatter_style_opts.update()
        self.line_style_opts.update()

        self.scatter_size_opts.update()
