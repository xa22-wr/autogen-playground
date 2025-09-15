import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen import AssistantAgent, UserProxyAgent
from openai import AsyncOpenAI
from autogen_ext.models.azure import AzureAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential


load_dotenv()

llm_config = { "config_list": [{ "model": "gpt-4o-mini", "api_key": os.environ.get("OPENAI_API_KEY") }] }

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

user_proxy.initiate_chat(
    assistant,
    message= "Tell me a joke on data scientists"
)
