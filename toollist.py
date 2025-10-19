import tools.SimpleTool as SimpleTool
import tools.ExampleTool as ExampleTool
toollib = {
    "SimpleTool": SimpleTool,
    "ExampleTool": ExampleTool
}


def searching(toolname:str):
    if toolname in toollib:
        return True
    return False
        
        
def using_tool(toolname:str,usename:str):
    tooltext=toollib[toolname]
    toolclass=getattr(tooltext,toolname)
    func=toolclass(usename)
    sentence=func.use()
    return sentence


def showtool():
    sentence=""
    for i in toollib:
        tooltext=toollib[i]
        toolclass=getattr(tooltext,i)
        func=toolclass("")
        sentence=sentence+"\n"+func.show()
    return sentence
        