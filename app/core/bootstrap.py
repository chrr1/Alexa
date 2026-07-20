from app.commands.ping import PingCommand
from app.commands.open_app import OpenAppCommand
from app.commands.open_website import OpenWebsiteCommand
from app.commands.shutdown import ShutdownCommand
from app.commands.sleep import SleepCommand

from app.commands.play_music import PlayMusicCommand
from app.commands.pause_music import PauseMusicCommand
from app.commands.next_music import NextMusicCommand
from app.commands.previous_music import PreviousMusicCommand

from app.core.registry import CommandRegistry
from app.core.router import CommandRouter
from app.core.assistant import Assistant


def create_registry():

    registry = CommandRegistry()

    registry.register("ping", PingCommand())

    registry.register("buka", OpenAppCommand())
    registry.register("bukain", OpenAppCommand())

    registry.register("website", OpenWebsiteCommand())

    registry.register("shutdown", ShutdownCommand())
    registry.register("matikan", ShutdownCommand())

    registry.register("sleep", SleepCommand())
    registry.register("tidur", SleepCommand())

    registry.register("putar", PlayMusicCommand())
    registry.register("pause", PauseMusicCommand())
    registry.register("next", NextMusicCommand())
    registry.register("previous", PreviousMusicCommand())

    return registry


def create_assistant():

    registry = create_registry()

    router = CommandRouter(registry)

    assistant = Assistant(router)

    return assistant