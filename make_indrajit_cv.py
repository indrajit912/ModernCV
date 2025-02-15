# Indrajit_CV - This script generate the CV from the data
# given in indrajit.py module
#
# Author: Indrajit Ghosh
# Created on: Mar 04, 2023
# Modified On: Mar 15, 2024
#

from curriculumvitae import CurriculumVitae
from main import setup_tex_dir
from pathlib import Path
import os, sys, re
from indrajit import Indrajit

def _get_weblink_tex(url:str, url_text:str=None):
    """
    This functions accepts an `url` (e.g- "https://google.com/") and 
    an optional `url_text` (e.g- "Click here").
    And returns a str 
        r"\texttt{\href{ <url> }{ <url_text> }}}" 
    """
    url_text = url_text if url_text else url
    return f"\\texttt{{\\href{{{url}}}{{{url_text}}}}}"


def latex_escape(text:str):
    """
    This function accepts plain text and return the TeX escaped text.
    Parameter:
    ----------
        `text`: `str`, a plain text message; This msg should not be any 
                        standard LaTeX command such as `\begin{document}`.
    
    Returns:
    --------
        `str`; the message escaped to paste it into a `.tex` file
    """
    tex_conversion = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
    }

    regex = re.compile(
        '|'.join(
            re.escape(str(key)) for key in sorted(
                tex_conversion.keys(), key=lambda item : -len(item)
            )
        )
    )

    return regex.sub(
        lambda match: tex_conversion[match.group()], text
    )


class IndrajitCV(CurriculumVitae):

    def __init__(self):
        super().__init__(
            first_name=Indrajit.first_name,
            family_name=Indrajit.family_name,
            address=Indrajit.address,
            mobile=Indrajit.mobile,
            email=latex_escape(Indrajit.email),
            style="banking",
            color="blue",
            font_size=10,
            photo_height=70,
            photo_thickness=0.9,
            scale=0.7
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
        self.add_section(title="Publications")
        for pub in Indrajit.publication:
            authors = [
                r"\textbf{I. Ghosh}" if name == "Me" else name
                for name in pub['authors']
            ]
            authors = ', '.join(authors)
            pub_links = ', '.join(
                f"[\\href{{{item['link']}}}{{\\small {item['link-text']}}}]"
                for item in pub['links']
            )

            tex_line = (
                authors 
                + "; "
                + r"\emph{"
                + pub['title']
                + "}, "
                + pub['status']
                + "."
                + "\n"
                + r"\newline"
                + pub_links
            )

            self.add_cvlistitem(tex_line)

        # Fellowship
        self.add_section(title="Fellowships and Achievements")
        for fellowship in Indrajit.fellowship_achievement:
            self.add_cvlistitem(fellowship['description'])

        # Contributed Talks
        self.add_section(title="Contributed Talks")
        for talk in Indrajit.contri_talks:
            talk_desc = (
                "\n"
                + r"\cvlistitem{"
                + f"Venue: {talk['venue']}" 
                + "}"
                + "\n"
                + r"\cvlistitem{Website: "
                + _get_weblink_tex(url=talk['website']['url'], url_text=talk['website']['url_text'])
                + "}"
            )
            if  'abstract' in talk.keys() and talk['abstract']:
                talk_desc += (
                    "\n"
                    + r"\cvlistitem{Abstract: "
                    + _get_weblink_tex(url=talk['abstract']['url'], url_text=talk['abstract']['url_text'])
                    + "}"
                    +"\n"
                )
            self.add_cventry(
                years=talk['date'],
                degree_or_job_title=talk['institute'],
                institution_or_employer=talk['title'],
                localization=talk['country'],
                description=talk_desc
            )
        
        # Teaching Experiences
        self.add_section(title="Teaching Experiences")
        for teach in Indrajit.teaching_experience:
            teach_desc = (
                "\n"
                + r"\cvlistitem{"
                + "Course: " 
                + _get_weblink_tex(
                    url=teach['webpage'],
                    url_text=teach['course']
                )
                + "}"
                + "\n"
                + r"\cvlistitem{Instructor: "
                + teach['instructor']
                + "}"
            )

            self.add_cventry(
                years=teach['year'],
                degree_or_job_title=teach['role'],
                institution_or_employer=teach['institute'],
                localization=teach['country'],
                description=teach_desc
            )


        # Conferences
        self.add_section(title="Conferences and Workshops Attended")
        for conf in Indrajit.conferences:
            if 'website' in conf and conf['website']:
                conf_web = (
                    "\n"
                    + r"\cvlistitem{Website: "
                    + _get_weblink_tex(url=conf['website']['url'], url_text=conf['website']['url_text'])
                    + "}"
                )
            else:
                conf_web = ''
                

            conf_desc = (
                "\n"
                + r"\cvlistitem{"
                + f"Venue: {conf['venue']}" 
                + "}"
                + conf_web
            )
            
            self.add_cventry(
                years=conf['date'],
                degree_or_job_title=conf['institute'],
                institution_or_employer=conf['title'],
                localization=conf['country'],
                description=conf_desc
            )

        # References
        self.add_section(title="References")
        for ref in Indrajit.references:
            _tex = (
                "\n"
                + r"\textbf{"
                + ref['name']
                + "}"
                + ", "
                + "\\emph{" + ref['designation'] + "}"
                + " | "
                + ref['address']
                + " | "
                + "\\texttt{" + ref['email'] + "}"
            )
            self.add_cvlistitem(_tex)
        


def main():
    tex_dir = Path.cwd() / 'indra_cv'
    indrajit = IndrajitCV()

    setup_tex_dir(tex_dir=tex_dir, cvObj=indrajit)
    print(f"\n\nCV LaTeX written successfully at `{tex_dir}`\n")

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