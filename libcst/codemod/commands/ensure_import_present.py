import argparse
from typing import Generator, Type

from libcst.codemod import Codemod, MagicArgsCodemodCommand
from libcst.codemod.visitors import AddImportsVisitor


class EnsureImportPresentCommand(MagicArgsCodemodCommand):

    DESCRIPTION: str = (
        "Given a module and possibly an entity in that module, add an import "
        + "as long as one does not already exist."
    )

    @staticmethod
    def add_args(parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--module",
            dest="module",
            metavar="MODULE",
            help="Module that should be imported.",
            type=str,
            required=True,
        )
        parser.add_argument(
            "--entity",
            dest="entity",
            metavar="ENTITY",
            help=(
                "Entity that should be imported from module. If left empty, entire "
                + " module will be imported."
            ),
            type=str,
            default=None,
        )

    def get_transforms(self) -> Generator[Type[Codemod], None, None]:
        AddImportsVisitor.add_needed_import(
            self.context, self.context.scratch["module"], self.context.scratch["entity"]
        )
        yield AddImportsVisitor
