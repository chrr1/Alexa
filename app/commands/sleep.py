import subprocess

from app.core.context import CommandContext


class SleepCommand:

    def execute(self, context: CommandContext):

        subprocess.Popen(
            "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
            shell=True
        )

        return "Mode sleep..."