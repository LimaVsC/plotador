import flet as ft
import threading


class LoadingOverlay(ft.Container):
    def __init__(self):
        super().__init__(
            visible=False,
            alignment=ft.alignment.center,
            content=ft.Column([ft.ProgressRing(),
                               ft.Text("Loading...", size=18),],
                              alignment=ft.MainAxisAlignment.CENTER,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor=ft.Colors.with_opacity(0.7, ft.Colors.BLACK),
            expand=True)

    def show(self, page):
        self.visible = True
        page.update()

    def hide(self, page):
        self.visible = False
        page.update()

    def start_loading(self, page, task, *args, **kwargs):
        self.show(page)

        def run():
            task(*args, **kwargs)
            self.hide(page)

        threading.Thread(target=run, daemon=True).start()
