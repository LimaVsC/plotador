from loading import LoadingOverlay

loading_overlay = LoadingOverlay()


class Files():

    def pick_file(e):
        file_picker.pick_files()

    def read_file_loading_screen(e):
        loading_overlay.start_loading(page, on_file_picked, e)

    def on_file_picked(e):
        # plot.reset()
        file_name = e.files[0].name
        file_path = e.files[0].path
        data.read_file_handler(file_name, file_path)
        plot.df = data.df

    # Save plot
    def save_file_result(e):
        save_file_path.value = e.path if e.path else "Cancelled!"
        plot.save_plot(e.path)
        save_file_path.update()
