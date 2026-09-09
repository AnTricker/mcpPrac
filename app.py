from fastmcp import FastMCP
app=FastMCP("My FastMCP App")
# give a addor
@app.tool
def addor(a:int,b:int)->int:
    """Add two numbers""" #tell ai this tool's function
    return a+b