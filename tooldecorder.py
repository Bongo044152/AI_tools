import toollist

class decorder():
    def __init__(self,sentence):
        self.toolname,self.use = sentence.split(">",1)
        self.toolname = self.toolname.replace('<','',1)
        self.use,notuse = self.use.split("</",1)
        
    def usetool(self):
        toollist.searching(self.toolname,self.use)
    
    
tool_used=decorder("<SimpleTool>abc</SimpleTool>")
tool_used.usetool()