from app.commands.ping import PingCommand
from app.core.registry import CommandRegistry
from app.commands.open_app import OpenAppCommand
from app.commands.open_website import OpenWebsiteCommand


def create_registry():

    registry = CommandRegistry()

    registry.register("ping", PingCommand())
    registry.register("buka", OpenAppCommand())
    registry.register("website", OpenWebsiteCommand())

    return registry