# A Scriipt that can create an CV in LaTeX using `moderncv` class
#
# Author: Indrajit Ghosh
#
# Created on: Dec 25, 2022
#

from curriculumvitae import *


def main():
    cv = CurriculumVitae(
        first_name="Indrajit",
        family_name="Ghosh"
    )

    cls = ModernCVClsFile()
    cls.create()


if __name__ == '__main__':
    main()