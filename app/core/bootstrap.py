from app.commands.ping import PingCommand
from app.core.registry import CommandRegistry


def create_registry():

    registry = CommandRegistry()

    registry.register("ping", PingCommand())

    return registry