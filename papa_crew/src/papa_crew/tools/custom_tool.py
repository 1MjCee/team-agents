from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from telegram import Bot
import asyncio

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."


class TelegramMessageInput(BaseModel):
    message: str = Field(..., description="The message to be sent to the Telegram group.")

class TelegramBotTool(BaseTool):
    name: str = "Telegram Message Sender"
    description: str = "Sends messages to Telegram group."
    args_schema: type[BaseModel] = TelegramMessageInput

    bot: Bot | None = None
    group_chat_id: int | None = None

    model_config = {
        "arbitrary_types_allowed": True
    }

    def __init__(self, token: str, group_chat_id: int):
        super().__init__()
        self.bot = Bot(token=token)
        self.group_chat_id = group_chat_id

    def _run(self, message: str) -> str:
        # Run the async method in a synchronous context
        return asyncio.run(self._async_run(message))

    async def _async_run(self, message: str) -> str:
        try:
            await self.bot.send_message(chat_id=self.group_chat_id, text=message)
            return "Message sent successfully"
        except Exception as e:
            return f"Failed to send message: {str(e)}"