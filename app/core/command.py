from abc import ABC, abstractmethod

from app.core.context import CommandContext


class Command(ABC):
    """Base class untuk semua command."""

    @abstractmethod
    def execute(self, context: CommandContext) -> str:
        """Menjalankan command."""
        raise NotImplementedError