import click
import os
from pathlib import Path
import importlib



class AocCommand(click.MultiCommand):
    """
    Click command with lazy loading subcommands.

    Expects all commands to be in the 'commands' directory with a function with the same
    name.
    """

    def list_commands(self, ctx):
        """Return the names of all the files in the commands dir."""
        return {
            p.stem: self.get_command(None, p.stem)
            for p in (Path(__file__).parent / "commands").iterdir()
            if p.suffix == ".py" and not p.name.startswith("_")
        }

    def get_command(self, ctx, name):
        """Return the names of all the files in the commands dir."""
        from dotenv import load_dotenv  # this is slow to import
        load_dotenv()
        return getattr(importlib.import_module(f"aoc.cli.commands.{name}"), name)


@click.command(cls=AocCommand)
def cli():
    pass
