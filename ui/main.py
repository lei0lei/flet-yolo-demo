import flet as ft
import sys
sys.path.append('D:\\github\\flet-yolo-demo')
from ui.check import CheckPage
from ui.train import TrainPage
from ui.settings import SettingsPage
from ui.eval import EvalPage
from ui.analyze import AnalyzePage
from ui.models import ModelShares
from ui.annotate import AnnotatePage

class DefaultMainPage(ft.Container):
    def __init__(self):
        super().__init__()
        self.model_shares = ModelShares()
        self.analyze_page = AnalyzePage(self.model_shares)
        self.check_page = CheckPage(self.model_shares)
        self.train_page = TrainPage(self.model_shares)
        self.settings_page = SettingsPage(self.model_shares)
        self.eval_page = EvalPage(self.model_shares)
        self.annotate_page = AnnotatePage()
        
        
    def change_page(self,page_name):
        if page_name == 'check':
            self.content=self.check_page
            self.page.update()
        if page_name == 'train':
            self.content=self.train_page
            self.page.update()
        if page_name == 'settings':
            self.content=self.settings_page
            self.page.update()
        if page_name == 'eval':
            self.content=self.eval_page
            self.page.update()
        if page_name == 'analyze':
            self.content=self.analyze_page
            self.page.update()
        if page_name == 'annotate':
            self.content=self.annotate_page
            self.page.update()


def main(page: ft.Page):
    page_list = ['/check',
                 '/train',
                 '/eval',
                 '/settings',
                 '/analyze',
                 '/annotate']
    default_mainpage = DefaultMainPage()
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FACT_CHECK_OUTLINED, 
                selected_icon=ft.icons.FACT_CHECK, 
                label="check"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.TRAIN_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.TRAIN_ROUNDED),
                label="train",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.NOT_STARTED_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.NOT_STARTED_SHARP),
                label_content=ft.Text("eval"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("settings"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ANALYTICS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ANALYTICS),
                label_content=ft.Text("analyze"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.DRAW_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DRAW_ROUNDED),
                label_content=ft.Text("annotate"),
            ),
        ],
        on_change=lambda e: page.go(page_list[e.control.selected_index])
    )
    
    def get_route_list(route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list
    
    def route_change(e):
        route_list = get_route_list(page.route)
        print(f'goto page {route_list}')
            
        if len(route_list) == 0:
            page.go("/check")
        else:
            default_mainpage.change_page(route_list[0])
            
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                default_mainpage,
            ],
            expand=True,
        )
    )

    page.on_route_change = route_change
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    print(f"Initial route: {page.route}")
    page.go(page.route)

ft.app(target=main)