import flet as ft


class TrainPage(ft.Container):
    def __init__(self,model_shares):
        super().__init__()
        self.model_shares = model_shares
        self.content = ft.Column(
            controls=[ft.Row(
        ),ft.Row()])
        