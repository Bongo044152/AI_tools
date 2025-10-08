import tools.BaseToolModel as BaseToolModel
class SimpleTool(BaseToolModel.BaseToolModel):
    def __init__(self,a):
        super().__init__()
        self.ch=a
        
    def use(self):
        print("使用的工具:SimpleTool")
        print(self.ch)
    
    def show(self):
        return "SimpleTool:這是一個會返還輸入的工具，我輸入甚麼要返還我甚麼"
        