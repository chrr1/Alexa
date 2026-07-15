from dataclasses import dataclass

from app.intents.intent_type import IntentType


@dataclass(slots=True)
class Intent:

    type: IntentType

    target: str | None = None