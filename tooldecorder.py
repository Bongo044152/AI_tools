import toollist

class decorder():
    def __init__(self,sentence):
        self.show="接下來回列出所有你可以使用的工具，使用的方法格是為<工具名稱>你使用的東西<工具名稱>，你可以使用的工具有:"
        
        start_tag_begin = sentence.find('<')
        start_tag_end = sentence.find('>', start_tag_begin) if start_tag_begin != -1 else -1
        
        if start_tag_begin != -1 and start_tag_end != -1:
            self.toolname = sentence[start_tag_begin + 1:start_tag_end]
            end_tag = f"</{self.toolname}>"
            end_tag_begin = sentence.find(end_tag, start_tag_end)
            if end_tag_begin != -1:
                self.use = sentence[start_tag_end + 1:end_tag_begin]
            else:
                self.toolname = ""
                self.use = ""
        else:
            self.toolname = ""
            self.use = ""
            
        
    def usetool(self):
        if(toollist.searching(self.toolname)==True):
            result=toollist.using_tool(self.toolname,self.use)
            return result
        
        
    def get_tool_option(self):
        self.show=self.show+toollist.showtool()
        return self.show

    
