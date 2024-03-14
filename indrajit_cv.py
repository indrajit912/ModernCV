# Indrajit_CV
#
# Author: Indrajit Ghosh
#
# Created on: Mar 04, 2023
#

from curriculumvitae import CurriculumVitae
from main import setup_tex_dir
from pathlib import Path


class IndrajitCV(CurriculumVitae):

    EDUCATIONS = [
        {
            "years": '2023-2034',
            "degree": 'PhD in Mathematics',
            "institution": 'Indian Statistical Institute',
            "country": 'India',
            "grade": '8cgp',
            "description": ['hello there', 'how are you?']
        }
    ]

    def __init__(self):
        super().__init__(
            first_name="Indrajit",
            family_name="Ghosh",
            address=["8th Mile Mysore Road, Pin-560 059", "Bangalore, India"],
            mobile="(+91) 9564 957618",
            email="indrajitghosh912@gmail.com",
            style="casual",
            font_size=12,
            photo_height=70,
            photo_thickness=0.9,
        )

        self.add_section(title="Education")

        for edu in self.EDUCATIONS:
            _years = edu['years']
            _desc = edu['description']
            if _desc:
                if isinstance(_desc, list):
                    _desc = r'\\'.join(_desc)

            self.add_cventry(
                years=_years,
                degree_or_job_title=edu['degree'],
                institution_or_employer=edu['institution'],
                localization=edu['country'],
                grade=edu['grade'],
                description=_desc
            )



def main():
    tex_dir = Path.home() / 'Desktop' / 'indra_cv'
    indrajit = IndrajitCV()

    setup_tex_dir(tex_dir=tex_dir, cvObj=indrajit)
    print(f"CV LaTeX written successfully at `{tex_dir}`")

    print(indrajit.text)


if __name__ == '__main__':
    main()