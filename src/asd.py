import flet as ft
import pandas as pd

# ✅ Caminho centralizado
CAMINHO_CSV = "/mnt/disco2/forfun/flet/plotador/data/NG_sample_2.txt"


def ler_csv(caminho):
    df = pd.read_csv(caminho)
    colunas = df.columns.tolist()
    linhas = df.values.tolist()
    return colunas, linhas


def main(page: ft.Page):
    page.title = "Tabela CSV com Pandas e Scroll"

    colunas, linhas = ler_csv(CAMINHO_CSV)

    # Cabeçalho
    cabecalho = ft.Row(
        controls=[
            ft.Container(ft.Text(col, weight="bold"), padding=10, expand=1)
            for col in colunas
        ],
        spacing=5
    )

    # Linhas da tabela
    linhas_tabela = []
    for linha in linhas:
        linhas_tabela.append(
            ft.Row(
                controls=[
                    ft.Container(ft.Text(str(valor)), padding=10, expand=1)
                    for valor in linha
                ],
                spacing=5
            )
        )

    # Tabela completa (com cabeçalho e linhas)
    tabela_completa = ft.Column([cabecalho] + linhas_tabela, spacing=0)

    # ListView com rolagem
    tabela_scroll = ft.ListView(
        controls=[tabela_completa],
        expand=True,
        spacing=0,
        padding=10
    )

    page.add(tabela_scroll)


ft.app(target=main)
