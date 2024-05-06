import flet as ft


class infoControl(ft.Tabs):
    def __init__(self,display,modelshares):
        super().__init__()
        self.modelshares = modelshares
        self.tabs = [
            ft.Tab(
                text="Settings",
                content=ft.Column(
                    controls = [
                            ft.Container(
                            height = 20,
                            content=ft.Row(
                                controls=[ft.Text('settings')]
                            )
                        ),
                    ]
                )
            ),
            ft.Tab(
                text="Info",
                content=ft.Column(
                    controls = [
                            ft.Container(
                            height = 20,
                            content=ft.Row(
                                controls=[ft.Text('camera info')]
                            )
                        ),
                    ]
                )
            )]


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
        

class modelSelectControl(ft.Row):
    def __init__(self,display):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.SPACE_AROUND
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
                                    icon=ft.icons.FILE_DOWNLOAD_DONE_ROUNDED,
                                    on_click=self.load_model,
                                    disabled=False,
                                    )
        
        self.run_algo_control = ft.ElevatedButton(
                                    text="start algo",
                                    height=50,
                                    icon=ft.icons.FILE_DOWNLOAD_DONE_ROUNDED,
                                    on_click=self.run_algo,
                                    disabled=False,
                                    )
        self.controls = [self.model_list_control,
                         self.device_list_control,
                         self.load_model_control,
                         self.run_algo_control
                         ]
        
    def load_model(self,e):
        print(f'load model')
        
    def select_device(self,e):
        
        print(f'select device')
        
        
    def run_algo(self,e):
        print(f'run algo')
    
    
    
    def open_device(self,e):
        print(f'model loaded')
        
    def select_model(self,e):
        self.selected_model = self.model_list_control.value
        print(f'selected model {self.model_list_control.value}')
   

class EvalPage(ft.Container):
    def __init__(self,model_shares):
        super().__init__()
        self.model_shares = model_shares
        self.display_control = displayControl()
        self.model_select_control = modelSelectControl(self.display_control)
        self.info_control = infoControl(self.display_control,self.model_shares)
        
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
                                    content = self.info_control
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
        

    
    