from typing import Dict
from typing import Optional
from app.core.command import Command

class CommandRegistry:
    def __init__(self):
        self._commands: Dict[str, Command] = {}

    def register(self, name: str, command: Command):
        self._commands[name.lower()] = command

    def get(self, name: str) -> Optional[Command]:
        return self._commands.get(name.lower())

    def all(self):
        return self._commands
    