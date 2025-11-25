from tools import BaseToolModel
class SimpleTool(BaseToolModel.BaseToolModel):
    def __init__(self,a):
        self.ch=a
       
        
    def use(self):
        return self.ch
    
    
    def show(self):
        return "SimpleTool:這是一個會返還輸入的工具，我輸入甚麼要返還我甚麼"
        