import flet as ft
from app_state import AppState


def main(page: ft.Page):
    state = AppState()

    texto = ft.Text()
    selecionar_btn = ft.ElevatedButton("Selecionar arquivo")

    # Cria o FilePicker e adiciona ao overlay da página
    def ao_escolher_arquivo(e: ft.FilePickerResultEvent):
        if not e.files:
            return
        path = e.files[0].path
        state.update_file(path, ler_e_exibir)
        ler_e_exibir()

    file_picker = ft.FilePicker(on_result=ao_escolher_arquivo)
    page.overlay.append(file_picker)

    # Agora pode configurar o botão
    selecionar_btn.on_click = lambda _: file_picker.pick_files(allow_multiple=False)

    def ler_e_exibir():
        try:
            with open(state.file_path, "r") as f:
                texto.value = f.read()
        except Exception as e:
            texto.value = f"Erro ao ler o arquivo: {e}"
        page.update()

    page.add(selecionar_btn, texto)

    def on_close(e):
        state.stop_observer()

    page.on_close = on_close


ft.app(target=main)
