import flet as ft
from ui.models import ModelShares
import os, platform, subprocess, re





def check_cpu():
    if platform.system() == "Windows":
        return platform.processor()


def check_gpu():
    pass

def check_cuda_version():
    pass



def check_yolo():
    pass


def check_models():
    pass

def warmup_yolo_cpu():
    pass

def warmup_yolo_gpu():
    pass

def warmup_yolo_multi_gpu():
    pass

def onclick_to_install_yolov8():
    pass

def onclick_to_install_yolov5():
    pass


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
        

    
    
    
    
    
