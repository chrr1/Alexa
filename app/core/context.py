from dataclasses import dataclass, field


@dataclass(slots=True)
class CommandContext:

    raw_text: str

    arguments: list[str] = field(default_factory=list)