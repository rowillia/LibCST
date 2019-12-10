from typing import Type

from libcst.codemod import Codemod, CodemodTest
from libcst.codemod.commands.unnecessary_format_string import UnnecessaryFormatString


class TestUnnecessaryFormatString(CodemodTest):
    TRANSFORM: Type[Codemod] = UnnecessaryFormatString

    def test_replace(self) -> None:
        before = r"""
            good: str = "good"
            good: str = f"with_arg{arg}"
            good = "good{arg1}".format(1234)
            good = "good".format()
            good = "good" % {}
            good = "good" % ()
            good = rf"good\d+{bar}"
            good = f"wow i dont have args but dont mess my braces {{ up }}"

            bad: str = f"bad" + "bad"
            bad: str = f'bad'
            bad: str = rf'bad\d+'
        """
        after = r"""
            good: str = "good"
            good: str = f"with_arg{arg}"
            good = "good{arg1}".format(1234)
            good = "good".format()
            good = "good" % {}
            good = "good" % ()
            good = rf"good\d+{bar}"
            good = f"wow i dont have args but dont mess my braces {{ up }}"

            bad: str = "bad" + "bad"
            bad: str = 'bad'
            bad: str = r'bad\d+'
        """
        self.assertCodemod(before, after)
