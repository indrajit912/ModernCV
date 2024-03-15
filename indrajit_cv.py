# Indrajit_CV
#
# Author: Indrajit Ghosh
#
# Created on: Mar 04, 2023
#

from curriculumvitae import CurriculumVitae
from main import setup_tex_dir
from pathlib import Path
import os, sys
from indrajit import Indrajit


class IndrajitCV(CurriculumVitae):

    def __init__(self):
        super().__init__(
            first_name=Indrajit.first_name,
            family_name=Indrajit.family_name,
            address=Indrajit.address,
            mobile=Indrajit.mobile,
            email=Indrajit.email,
            style="banking",
            font_size=12,
            photo_height=70,
            photo_thickness=0.9,
        )

        # Education
        self.add_section(title="Education")

        for edu in Indrajit.education:
            self.add_education(
                years=edu['years'],
                degree_or_job_title=edu['degree'],
                institution_or_employer=edu['institute'],
                localization=edu['location']
            )

        # Research
        self.add_section(title="Research Interests")
        self.add_raw_tex(Indrajit.research_interest)

        # Publication
        self.add_section(title="Publication")
        for pub in Indrajit.publication:
            preprint = (
                '(\\emph{Pre-print})'
                if pub['preprint'] == 1
                else ''
            )
            if pub['collaborators']:  # Check if collaborators list is not empty
                collaborators = ", ".join(pub['collaborators'])
                collaborators = f" (with {collaborators})"
            else:
                collaborators = ""

            tex_line = (
                preprint +
                r" \emph{"
                + pub['title']
                + "}"
                + r"{" + collaborators + r"}, "
                + r'\textbf{'
                + pub['year']
                + r"}, "
                + r"\href{" + pub['url']['link'] + r"}"
                + r"{" + pub['url']['link-text'] + r"}"
            )

            self.add_cvlistitem(tex_line)

        # Fellowship
        self.add_section(title="Fellowships and Achievements")
        for fellowship in Indrajit.fellowship_achievement:
            self.add_cvlistitem(fellowship['description'])

        # Contributed Talks
        self.add_section(title="Contributed Talks")
        for talk in Indrajit.contri_talks:
            desc = (
                r"\cvlistitem{"
                + f"Venue: {talk['venue']}" + "}"
                r"\cvlistitem{"
                + r"Website: \texttt{" 
                + r"\href{"
                + talk['website']['text'] 
                + "}{"
                + talk['website']['url'] + "}}"
                + "}"
            )
            self.add_cventry(
                years=talk['date'],
                degree_or_job_title=talk['institute'],
                institution_or_employer=talk['title'],
                localization=talk['country'],
                description=desc
            )
    



def main():
    tex_dir = Path.home() / 'Desktop' / 'indra_cv'
    indrajit = IndrajitCV()

    setup_tex_dir(tex_dir=tex_dir, cvObj=indrajit)
    print(f"CV LaTeX written successfully at `{tex_dir}`")

    print(indrajit.text)

    # Change the dir
    os.chdir(str(tex_dir))

    # Compile cv.tex
    os.system("pdflatex cv.tex")

    # Open cv.pdf
    pdfpath = str(tex_dir / "cv.pdf")
    if sys.platform.startswith('linux'):
        os.system(f"xdg-open {pdfpath}")
    else:
        os.startfile(pdfpath)

if __name__ == '__main__':
    main()