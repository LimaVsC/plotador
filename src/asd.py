import flet as ft
from categorical import Categorical


def main(page):
    cat = Categorical()
    cat_props = cat.cat_props(None,
                              None,
                              None,
                              None,
                              None,
                              None,)
    page.add(cat_props)


ft.app(target=main)
