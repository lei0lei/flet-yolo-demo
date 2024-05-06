import flet as ft


class infoControl(ft.Tabs):
    def __init__(self,display):
        super().__init__()

class displayControl(ft.Row):
    def __init__(self,):
        super().__init__()

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
        pass
        
    def select_device(self,e):
        pass
    def run_algo(self,e):
        pass
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
        self.info_control = infoControl(self.display_control)
        
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
                        ft.Row(
                            controls=[self.display_control, 
                                    self.info_control]
                            
                        )]
                )
            )
        

    
    