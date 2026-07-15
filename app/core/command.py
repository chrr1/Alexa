from abc import ABC, abstractmethod

class Command(ABC):
    """Base class untuk semua command Alexa."""

    @abstractmethod
    def execute(self, text: str) -> str:
        """Jalankan command."""
        pass