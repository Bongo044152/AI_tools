import toollist
class showAI():
    def __init__(self):
        self.sentence="接下來回列出所有你可以使用的工具，使用的方法格是為<工具名稱>你使用的東西<工具名稱>，你可以使用的工具有:"
    def optiontool(self):
        self.sentence=self.sentence+toollist.showtool()
        return self.sentence
    
tool_used=showAI()
result=tool_used.optiontool()
print(result)