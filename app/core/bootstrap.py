from app.commands.ping import PingCommand
from app.core.registry import CommandRegistry
from app.commands.open_app import OpenAppCommand


def create_registry():

    registry = CommandRegistry()

    registry.register("ping", PingCommand())
    registry.register("buka", OpenAppCommand())

    return registry