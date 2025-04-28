from flet import FilePicker as fp
from file_monitor import Monitor


class FilePicker():
    def __init__(self,
                 page,
                 data,
                 plot,
                 loading_overlay,
                 monitor):

        self.page = page
        self.data = data
        self.plot = plot
        self.loading_overlay = loading_overlay
        self.monitor = monitor
        self.file_picker = fp()
        self.file_path = None
        self.sile_name = None

    def on_file_change(self):
        print("on_file_change")
        self.data.read_file_handler(self.file_name, self.file_path)
        self.plot.df = self.data.df
        self.plot.plot_update()

    def pick_file(self, e):
        self.file_picker.pick_files()

    def read_file_loading_screen(self, e):
        self.loading_overlay.start_loading(self.page,
                                           self.on_file_picked,
                                           e)

    def overlay_append(self):
        self.page.overlay.append(self.file_picker)

    def on_file_picked(self, e):
        to_keep = ["histogram",
                   "scatter",
                   "line",
                   "page",
                   "main_plot",
                   "data",
                   "plot_type"]
        self.plot.reset(to_keep)
        if e.files is None:
            self.loading_overlay.hide(self.page)
        else:
            self.file_name = e.files[0].name
            self.file_path = e.files[0].path

            self.data.read_file_handler(self.file_name, self.file_path)
            self.plot.df = self.data.df

            if self.monitor.observer.is_alive():
                self.monitor.stop()

            self.monitor = Monitor(self.file_path,
                                   self.file_name,
                                   self.on_file_change)
            self.monitor.start()
            print(self.file_path, "\n", self.monitor.path)

    def save_file_result(self, e):
        self.plot.save_plot(e.path)
