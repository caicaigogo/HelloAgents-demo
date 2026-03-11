from hello_agents import ReActAgent, HelloAgentsLLM, ToolRegistry
from hello_agents.tools.builtin import ReadTool, WriteTool, TodoWriteTool
from dotenv import load_dotenv

load_dotenv()
llm = HelloAgentsLLM()
registry = ToolRegistry()
registry.register_tool(ReadTool())
registry.register_tool(WriteTool())
registry.register_tool(TodoWriteTool())

agent = ReActAgent("assistant", llm, tool_registry=registry)
agent.run("分析项目结构并生成报告")

