from dataclasses import dataclass


@dataclass(slots=True)
class Knowledge:

    name: str

    type: str

    aliases: list

    path: str | None = None

    url: str | None = None