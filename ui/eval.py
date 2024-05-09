import flet as ft
import asyncio
import os

yolo_instance = None
model = None


class settingsControl(ft.Column):
    def __init__(self,modelshares):
        super().__init__()
        self.modelshares = modelshares
        self.yolo_directory_path = ft.TextField(bgcolor=ft.colors.WHITE70,expand=True)
        self.model_directory_path = ft.TextField(bgcolor=ft.colors.WHITE70,expand=True)
        self.runalgo_directory_path = ft.TextField(bgcolor=ft.colors.WHITE70,expand=True)
        
        self.get_yolo_directory_dialog = ft.FilePicker(on_result=self.get_yolo_directory_result)
        self.get_model_directory_dialog = ft.FilePicker(on_result=self.get_model_directory_result)
        self.get_runalgo_directory_dialog = ft.FilePicker(on_result=self.get_runalgo_directory_result)
        
        self.controls.append(
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                    "yolo",
                    icon=ft.icons.FOLDER_OPEN,
                    on_click=lambda _: self.get_yolo_directory_dialog.get_directory_path(),
                    disabled=False,
                    ),
                    self.yolo_directory_path,]
            )
        )
        self.controls.append(
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                    "model",
                    icon=ft.icons.FOLDER_OPEN,
                    on_click=lambda _: self.get_model_directory_dialog.get_directory_path(),
                    disabled=False,
                    ),
                    self.model_directory_path,]
            )
        )
        self.controls.append(
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                    "run",
                    icon=ft.icons.FOLDER_OPEN,
                    on_click=lambda _: self.get_runalgo_directory_dialog.get_directory_path(),
                    disabled=False,
                    ),
                    self.runalgo_directory_path,]
            )
        )
    def get_yolo_directory_result(self,e: ft.FilePickerResultEvent):
        self.yolo_directory_path.value = e.path if e.path else "Cancelled!"
        self.update_yolo_path(self.yolo_directory_path.value)
        self.yolo_directory_path.update()
        
    def get_model_directory_result(self,e: ft.FilePickerResultEvent):
        self.model_directory_path.value = e.path if e.path else "Cancelled!"
        self.update_yolo_model_path(self.model_directory_path.value)
        self.model_directory_path.update()
        
    def get_runalgo_directory_result(self,e: ft.FilePickerResultEvent):
        self.runalgo_directory_path.value = e.path if e.path else "Cancelled!"
        self.update_runalgo_path(self.runalgo_directory_path.value)
        self.runalgo_directory_path.update()
        
        
    def did_mount(self):
        self.page.overlay.append(self.get_yolo_directory_dialog)
        self.page.overlay.append(self.get_model_directory_dialog)
        self.page.overlay.append(self.get_runalgo_directory_dialog)
        self.page.update()
        
    def update_yolo_path(self, dir):
        global yolo_instance
        self.modelshares.yolo_dir = dir
        
        import sys
        if dir in sys.path:
            pass
        else:
            sys.path.append(dir)
            print(sys.path)
        
        import importlib
        import importlib.util
        yolo_instance = importlib.import_module('ultralytics')
        # from ultralytics import YOLO
        
        
    def update_yolo_model_path(self, model_path):
        
        self.modelshares.model['path'] = model_path
    
    def update_runalgo_path(self, dir):
        self.modelshares.run_dir = dir
    
    def update_model_list(self):
        model_list = []
        return model_list
    
    
class infoControl(ft.Markdown):
    def __init__(self,modelshares):
        super().__init__()
        self.expand = True
        self.modelshares = modelshares
        self.value = """## YOLO Model Test Info
"""
        self.selectable = True
        
        self.extension_set = ft.MarkdownExtensionSet.GITHUB_WEB
        self.code_theme="atom-one-dark",


    def update_info(self,info):
        self.value+= """
"""
        self.value += info
        self.update()

class tabControl(ft.Tabs):
    def __init__(self,display,modelshares):
        super().__init__()
        self.modelshares = modelshares
        self.info_control = infoControl(self.modelshares)
        self.tabs = [
            ft.Tab(
                text="Settings",
                content=ft.Container(
                            padding=5,
                            bgcolor=ft.colors.ON_PRIMARY,
                            content=settingsControl(self.modelshares)
                            )
                ),
            ft.Tab(
                text="Info",
                content=
                ft.Container(
                            padding=5,
                            bgcolor=ft.colors.ON_PRIMARY,
                            content=ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True,
                                                controls=[self.info_control],
                                                )
                            )
                ),
            ]

    def update_info(self,info):
        
        self.info_control.update_info(info)
        self.update()



class displayControl(ft.Row):
    def __init__(self,):
        super().__init__()
        self.icon_height = 50
        self.icon_width = 50
        self.border_radius = 10
        self.viewarea_1 = ft.Image(
                src=f"./assets/camera-310.png",
                fit=ft.ImageFit.CONTAIN,
                height=self.icon_height,
                width = self.icon_width,
            )
        self.controls = [ft.Container(
                            height = 600,
                            width = 800,
                            border_radius=5,
                            bgcolor= ft.colors.PRIMARY_CONTAINER,
                            alignment=ft.alignment.center,
                            content = self.viewarea_1
                            ),]
    def update_im(self,im):
        self.viewarea_1.src = im
        print(im)
        self.viewarea_1.width =780
        self.viewarea_1.height = 1080
        self.update()

class modelSelectControl(ft.Row):
    def __init__(self,display,modelshares,tabcontrol):
        super().__init__()
        global model
        self.model = model
        self.tabcontrol = tabcontrol
        self.alignment = ft.MainAxisAlignment.SPACE_AROUND
        self.modelshares = modelshares
        self.display_control = display
        self.selected_model = None
        self.model_list = None
        self.model_list_control = ft.Dropdown(
                                    hint_text="Choose a model",
                                    on_change=self.select_model,
                                    bgcolor=ft.colors.ON_SECONDARY,
                                    height=60,
                                    width=600,
                                    border_radius=15,
                                    options=[
                                    ],
                                    autofocus=True,
                                )        
        
        self.device_list_control = ft.Dropdown(
                                    hint_text="Choose a device",
                                    on_change=self.select_device,
                                    bgcolor=ft.colors.ON_SECONDARY,
                                    height=60,
                                    width=200,
                                    border_radius=15,
                                    options=[ft.dropdown.Option("cpu"),
                                             ft.dropdown.Option("gpu")
                                    ],
                                    autofocus=True,
                                )
        self.load_model_control = ft.ElevatedButton(
                                    text="load model",
                                    height=50,
                                    icon=ft.icons.DOWNLOAD_ROUNDED,
                                    on_click=self.load_model,
                                    disabled=False,
                                    )
        
        self.run_algo_control = ft.ElevatedButton(
                                    text="start algo",
                                    height=50,
                                    icon=ft.icons.RESTART_ALT,
                                    on_click=self.run_algo,
                                    disabled=False,
                                    )
        self.controls = [self.model_list_control,
                         self.device_list_control,
                         self.load_model_control,
                         self.run_algo_control
                         ]
        
    def load_model(self,e):
        global yolo_instance
        self.model = yolo_instance.YOLO(self.modelshares.model['selected_model']) 
        self.tabcontrol.update_info(info="""## Load Model
""")
        
    def select_device(self,e):
        device = self.device_list_control.value
        if device == 'gpu':
            import torch

            torch.cuda.set_device(0)
            self.tabcontrol.update_info(info="""## Select device gpu 
""")
        else:
            self.tabcontrol.update_info(info="""## Select device cpu 
""")
        
        
        
    def run_algo(self,e):
        
        run_dir = self.modelshares.run_dir
        ext = ['.jpg']
        self.tabcontrol.update_info(info="""## 检测目录:
""")
        self.tabcontrol.update_info(info=f'{run_dir}')
        run_ims = [file for file in os.listdir(run_dir) if any(file.endswith(suffix) for suffix in ext)]
        for im in run_ims:
            self.tabcontrol.update_info(info="""## 检测图片: 
""" )
            self.tabcontrol.update_info(info=f'{im}' )
            # self.display_control.update_im(os.path.join(run_dir,im))
            import time
            time.sleep(1.5)
            self.tabcontrol.update_info(info="""等待1.5s
""")
            result = self.model.predict(os.path.join(run_dir,im),iou=0.5,conf=0.3)[0]
            print(result.boxes)
            boxes = result.boxes  # Boxes object for bounding box outputs
            masks = result.masks  # Masks object for segmentation masks outputs
            keypoints = result.keypoints  # Keypoints object for pose outputs
            probs = result.probs  # Probs object for classification outputs
            obb = result.obb  # Oriented boxes object for OBB outputs
            result.save(filename='result'+im)
            # self.display_control.viewarea_1.src ='result.jpg'
            self.display_control.update_im('result'+im)
            
            time.sleep(3)
            
        print(f'run algo')
    
    async def check_model_path(self):
        while True:#self.modelshares.model['path'] is None:
            await asyncio.sleep(2)
            # print(f'wait 2s')
            modeldir = self.modelshares.model['path']
            if modeldir is None:
                continue
            else:
                # 更新模型列表
                extensions = ['.pt', '.pth']
                self.model_list_control.options = []
                pts = [file for file in os.listdir(modeldir) if any(file.endswith(ext) for ext in extensions)]
                for pt in pts:
                    self.model_list_control.options.append(ft.dropdown.Option(pt))
                self.update()
        
    def open_device(self,e):
        print(f'model loaded')
        
    def select_model(self,e):
        self.selected_model = self.model_list_control.value
        self.modelshares.model['selected_model'] = os.path.join(self.modelshares.model['path'],self.selected_model)
        print(f'selected model {self.model_list_control.value}')
   
    def did_mount(self):
        self.page.run_task(self.check_model_path)





class EvalPage(ft.Container):
    def __init__(self,model_shares):
        super().__init__()
        self.model_shares = model_shares
        self.display_control = displayControl()
        self.tab_control = tabControl(self.display_control,self.model_shares)
        self.model_select_control = modelSelectControl(self.display_control,self.model_shares,self.tab_control)
        
        
        self.content = ft.Container(
            
            content=ft.Column(
                controls=[
                    ft.Container(
                        width = 1100,
                        alignment=ft.alignment.center,
                        content = self.model_select_control,
                        bgcolor=ft.colors.INDIGO,
                        border_radius=5,
                        padding=5,
                        ),
                    ft.Container(
                        width = 1100,
                        height = 550,
                        alignment=ft.alignment.center,
                        content = ft.Row(
                            controls=[
                                self.display_control, 
                                
                                ft.Container(
                                    height = 600,
                                    width = 280,
                                    border_radius=5,
                                    bgcolor= ft.colors.PRIMARY_CONTAINER,
                                    alignment=ft.alignment.center,
                                    content = self.tab_control
                                    )
                                ]
                        ),
                        bgcolor=ft.colors.SECONDARY,
                        border_radius=5,
                        padding=5,
                        ),
                ]
            )
        )
        

    
    