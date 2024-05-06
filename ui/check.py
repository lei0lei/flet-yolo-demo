import flet as ft
from ui.models import ModelShares



def hardware_check_control():
    return ft.Column()

def yolo_check_control():
    return ft.Column()



def install_yolo_control():
    return ft.Column()

class CheckPage(ft.Container):
    def __init__(self,model_shares):
        super().__init__()
        self.model_shares = model_shares
        self.content = ft.Column(
            controls=[ft.Row(
                controls=[hardware_check_control(),
                          install_yolo_control(),
                          yolo_check_control()]
        ),ft.Row()])
        

    
    
    
    
    
