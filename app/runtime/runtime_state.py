from enum import Enum


class RuntimeState(Enum):

    STANDBY = "standby"

    LISTENING = "listening"

    PROCESSING = "processing"

    RESPONDING = "responding"