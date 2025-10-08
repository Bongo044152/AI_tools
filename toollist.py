import tools.SimpleTool as SimpleTool
import tools.ExampleTool as ExampleTool
toollist = {
    "SimpleTool": SimpleTool,
    "ExampleTool": ExampleTool
}
val=2
def searching(toolname,use):
    if toolname in toollist:
        toolclass=toollist[toolname]
        func=getattr(toolclass,toolname)
        print(f"輸入的字串：{use}")
        text=func(use)
        text.use()
def showtool():
    sentence=""
    for i in toollist:
        toolclass=toollist[i]
        func=getattr(toolclass,i)
        text=func("")
        sentence=sentence+"\n"+text.show()
    return sentence
        