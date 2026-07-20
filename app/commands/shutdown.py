import subprocess

from app.core.context import CommandContext


class ShutdownCommand:

    def execute(self, context: CommandContext):

        subprocess.Popen(
            "shutdown /s /t 0",
            shell=True
        )

        return "Mematikan komputer..."