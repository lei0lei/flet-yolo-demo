import flet as ft
from ui.models import ModelShares


class AnnotatePage(ft.Container):
    def __init__(self,):
        super().__init__()
        self.content = wv = ft.WebView(
        "https://flet.dev",
        expand=True,
        on_page_started=lambda _: print("Page started"),
        on_page_ended=lambda _: print("Page ended"),
        on_web_resource_error=lambda e: print("Page error:", e.data),
    )

