import tools.SimpleTool as SimpleTool
import tools.ExampleTool as ExampleTool
toollib = {
    "SimpleTool": SimpleTool.SimpleTool,
    "ExampleTool": ExampleTool.ExampleTool
}


def searching(toolname:str):
    if toolname in toollib:
        return True
    return False
        
        
def using_tool(toolname:str,usename:str):
    tooltext=toollib[toolname]
    func=tooltext(usename)
    sentence=func.use()
    return sentence


def showtool():
    sentence=""
    for i in toollib:
        tooltext=toollib[i]
        func=tooltext("")
        sentence=sentence+"\n"+func.show()
    return sentence
        