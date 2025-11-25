import tooldecorder
from loggers.logger import init_printer,printer

#測試 decorder 函數和 usetool 方法
def test_decorder():
    #輸入句子，並解構句子
    tool_used=tooldecorder.decorder("<SimpleTool>abc</SimpleTool>")\
    #使用工具
    a=tool_used.usetool()
    init_printer()
    printer(a)
    
    

#測試 decorder 函數和 get_tool_option 方法
def test_get_tool_option():
    #輸入句子，並解構句子
    tool_used=tooldecorder.decorder("<SimpleTool>abc</SimpleTool>")
    #回傳工具使用說明
    a=tool_used.get_tool_option()
    init_printer()
    printer(a)
