
class ModelShares:
    # 多页面共享数据
    def __init__(self) -> None:
        self.model = {}
        self.model['path'] = None
        self.model['selected_model'] = None
        self.model['cfg'] = None
        self.model['pred_classes'] = [0]
        self.model['conf'] = 0.3
        self.model['iou'] = 0.7
        self.model['imgsz'] = 640
        self.model['device'] = None
        self.data_cfg = None
        self.run_dir = None
        self.yolo_dir = None
        
        