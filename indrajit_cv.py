# Indrajit_CV
#
# Author: Indrajit Ghosh
#
# Created on: Mar 04, 2023
#

from curriculumvitae import CurriculumVitae


class IndrajitCV(CurriculumVitae):

    def __init__(self, first_name: str, family_name: str):
        super().__init__(first_name, family_name)



def main():
    indrajit = IndrajitCV()

    print(indrajit)


if __name__ == '__main__':
    main()