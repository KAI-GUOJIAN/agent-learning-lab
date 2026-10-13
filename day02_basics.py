tools = [
    {"name": "calculator", "description": "计算简单表达式"},
    {"name": "search", "description": "搜索资料"},
    {"name": "weather", "description": "查询天气"},
]

def print_tools(tool_list):
    for tool in tool_list:
        print(f"{tool['name']}: {tool['description']}")

print_tools(tools)

def find_tool(tool_list, target_name):
    for tool in tool_list:
        if tool["name"] == target_name:
            return tool
    return None

print(find_tool(tools, "search"))
print(find_tool(tools, "unknown"))