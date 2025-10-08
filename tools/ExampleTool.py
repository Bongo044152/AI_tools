import tools.BaseToolModel as BaseToolModel
class ExampleTool(BaseToolModel.BaseToolModel):
    def __init__(self,a):
        super().__init__()
        self.ch=a
        
    def use(self):
        print("使用的工具:ExampleTool")
        print("y=ax+b")
    
    def show(self):
        return "ExampleTool:這是一個只會輸出y=ax+b的工具"
        