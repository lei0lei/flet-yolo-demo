import flet as ft
from ui.models import ModelShares


class AnalyzePage(ft.Container):
    def __init__(self,model_shares):
        super().__init__()
        self.model_shares = model_shares

