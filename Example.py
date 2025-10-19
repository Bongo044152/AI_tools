import tooldecorder

tool_used=tooldecorder.decorder("<SimpleTool>abc</SimpleTool>")
tool_used.usetool()
a=tool_used.get_tool_option()
print(a)