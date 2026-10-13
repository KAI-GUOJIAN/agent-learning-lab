from typing import Literal, TypedDict

from pydantic import BaseModel, ValidationError


class Tool(TypedDict):
    name: str
    description: str


def find_tool(tool_list: list[Tool], name: str) -> Tool | None:
    for tool in tool_list:
        if tool["name"] == name:
            return tool
    return None


tools: list[Tool] = [
    {"name": "calculator", "description": "计算简单表达式"},
    {"name": "search", "description": "搜索资料"},
]

print(find_tool(tools, "calculator"))


class CalculatorArgs(BaseModel):
    operation: Literal["add", "subtract", "multiply", "divide"]
    left: float
    right: float


valid_input = {"operation": "add", "left": 2, "right": 3}
args = CalculatorArgs.model_validate(valid_input)

print(args)
print(args.model_dump())

try:
    CalculatorArgs.model_validate(
        {"operation": "power", "left": 2, "right": 3}
    )
except ValidationError as error:
    print("参数校验失败：")
    print(error.errors()[0]["msg"])