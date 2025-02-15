# A class for Curriculum Vitae
#
# Author: Indrajit Ghosh
#
# Created on: Dec 25, 2022
#

from datetime import datetime
from pathlib import Path

__all__ = [
    "CurriculumVitae",
    "ModernCVColorStyFile",
    "ModernCVColorBlueStyFile",
    "ModernCVColorBlackStyFile",
    "ModernCVColorPurpleStyFile",
    "ModernCVColorRedStyFile",
    "ModernCVColorGreenStyFile",
    "ModernCVColorOrangeStyFile",
    "ModernCVColorGreyStyFile",
    "ModernCVStyleStyFile",
    "ModernCVCompatibilityStyFile",
    "ModernCVStyleBankingStyFile",
    "ModernCVStyleCasualStyFile",
    "ModernCVStyleClassicStyFile",
    "ModernCVStyleEmptyStyFile",
    "ModernCVStyleOldStyFile",
    "TweakListStyFile",
    "ModernCVClsFile"
]


class CurriculumVitae:
    """
    Class representing a CurriculumVitae in LaTeX

    Author: Indrajit Ghosh
    Created On: Dec 25, 2022
    """

    default_font_size = 11 # available: 10, 11, or 12;
    default_paper_size = 'a4paper' # available: a4paper, letterpaper, a5paper, legalpaper, executivepaper or landscape
    default_font_family = 'sans' # available: sans or roman
    default_style = 'classic' # available: 'casual' (default), 'classic', 'oldstyle' and 'banking'
    default_color = 'blue' # available: 'blue' (default), 'orange', 'green', 'red', 'purple', 'grey' and 'black'
    default_address = ["Address line, Pin-XXXXXX", "Your State, Country"]
    default_mobile = "(+91) xxxx xxxxxx"
    default_email = "someone@somewhere.com"
    default_photo = "indra.JPG"
    default_photo_height = 70
    default_photo_thickness = 0.9 

    DEFAULT_SPACING = 0.25

    def __init__(
        self,
        first_name:str,
        family_name:str,
        title:str='Curriculum Vitae',
        photo:str=None,
        address:list=None,
        mobile:str=None,
        email:str=None,
        *,
        font_size:int=None,
        paper_size:str=None,
        font_family:str=None,
        style:str=None,
        color:str=None,
        photo_height:float=None,
        photo_thickness:float=None,
        colorlinks:bool=True,
        scale:float=0.87
    ):
        self._firstname = first_name
        self._familyname = family_name
        self._title = title

        self._photo = self.default_photo if photo is None else photo
        self._address = self.default_address if address is None else address
        self._mobile = self.default_mobile if mobile is None else mobile
        self._email = self.default_email if email is None else email

        self._fontsize = self.default_font_size if font_size is None else font_size
        self._papersize = self.default_paper_size if paper_size is None else paper_size
        self._fontfamily = self.default_font_family if font_family is None else font_family
        self._style = self.default_style if style is None else style
        self._color = self.default_color if color is None else color
        self._photo_height = self.default_photo_height if photo_height is None else photo_height
        self._photo_thickness = self.default_photo_thickness if photo_thickness is None else photo_thickness
        self._colorlinks = colorlinks
        self._scale = scale

        self._preamble = self.get_preamble()
        self._body = self.get_body()


    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, new):
        self._firstname = new

    @property
    def familyname(self):
        return self._familyname
    
    @familyname.setter
    def familyname(self, new):
        self._familyname = new

    @property
    def mobile(self):
        return self._mobile
    
    @mobile.setter
    def mobile(self, num):
        self._mobile = num

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new):
        self._address = new

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new):
        self._email = new

    @property
    def photo(self):
        return self._photo

    @photo.setter
    def photo(self, p):
        self._photo = p

    @property
    def fontsize(self):
        return self._fontsize

    @fontsize.setter
    def fontsize(self, s):
        self._fontsize = s

    @property
    def fontfamily(self):
        return self._fontfamily
    
    @fontfamily.setter
    def fontfamily(self, n):
        self._fontfamily = n
    
    @property
    def papersize(self):
        return self._papersize

    @papersize.setter
    def papersize(self, new):
        self._papersize = new

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, new):
        self._style = new

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new):
        self._color = new

    @property
    def colorlinks(self):
        return self._colorlinks
    
    @colorlinks.setter
    def colorlinks(self, new:bool):
        self._colorlinks = new

    @property
    def scale(self):
        return self._scale
    
    @scale.setter
    def scale(self, new_scale_val:float):
        self._scale = new_scale_val


    @property
    def text(self):
        return self._preamble + "\n"*3 +  r"\begin{document}" "\n" + self._body + "\n" + r"\end{document}"


    def get_preamble(self):
        """
        From starting upto `\begin{document}` (not inclusive)
        """

        preamble = ''

        now = datetime.now().strftime('%b %d, %Y')
        
        texauthor_msg = f"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Modern CV
% Author: Indrajit Ghosh
% Created On: {now}

% This cv is typeset using `moderncv` LaTeX class.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""
        preamble += texauthor_msg

        _colorlinks = (
            ',colorlinks'
            if self._colorlinks
            else ''
        )

        docmentclass = (
            "\n"
            r"\documentclass[" + 
            f"{self._fontsize}pt,{self._papersize},{self._fontfamily}{_colorlinks}" + 
            r"]{moderncv}" + 
            "\n"
        )

        preamble += docmentclass

        _config = (
            "\n"
            r"\moderncvstyle{" + self._style + r"}" + 
            "\n" + 
            r"\moderncvcolor{" + self._color + r"}" + 
            "\n"
        )
        preamble += _config

        packages = (
            "\n" +
            r"\usepackage[scale="+ self._scale.__str__() + r"]{geometry}" + 
            "\n\n"
        )
        preamble += packages

        arguments = (
            r"\firstname{" + self._firstname + r"}" + 
            "\n" + 
            r"\familyname{" + self._familyname + r"}" + 
            "\n\n" + 
            r"\title{" + self._title + r"}" + 
            "\n" + 
            r"\address{" + self._address[0] + r"}" + r"{" + self._address[1] + "}" +
            "\n" + 
            r"\mobile{" + self._mobile + r"}" + 
            "\n" + 
            r"\email{" + self._email + r"}" + 
            "\n" + 
            r"\photo[" + 
            str(self._photo_height) + 
            r"pt][" +
            str(self._photo_thickness) +
            "pt]{" + self._photo + r"}" + # (Pic Height, Thickness of the frame)
            "\n\n"
        )
        preamble += arguments

        preamble += r"\newcommand{\Csharp}{{\settoheight{\dimen0}{C}C\kern-.05em \resizebox{!}{\dimen0}{\raisebox{\depth}{\textbf{\#}}}}}"
        preamble += "\n\n"

        return preamble


    def get_body(self):
        """
        Contents inbetween `\begin{document}` and `\end{document}`
        """
        return (
            "\n" + 
            r"\makecvtitle" + 
            "\n"
        )
    
    def add_raw_tex(self, tex:str):
        """
        Adds a raw LaTeX to the body
        """
        self._body += "\n" + tex


    @staticmethod
    def _cvitem(spacing:float, header:str, text:str):
        return "\n" + r"\cvitem[" + str(spacing) + r"em]{" + header + r"}{" + text + r"}" + "\n"

    def add_cvitem(self, header:str, text:str, spacing:float=None):
        """
        Makes a resume line with a header and a corresponding text
            usage: \cvitem[spacing]{header}{text}
        """

        spacing = self.DEFAULT_SPACING if spacing is None else spacing
        cmd = self._cvitem(spacing=spacing, header=header, text=text)

        self._body += cmd

    @staticmethod
    def _section(title:str):
        return "\n" + r"\section{" + title + r"}" + "\n"

    def add_section(self, title:str):
        self._body += self._section(title=title)

    @staticmethod
    def _cventry(
        years:str,
        degree_or_job_title:str,
        institution_or_employer:str,
        localization:str,
        grade:str,
        description:str,
        spacing:float
    ):

        return (
            "\n" + 
            r"\cventry[" +
            str(spacing) + 'em'
            r"]{" + 
            years + 
            r"}{" + 
            degree_or_job_title + 
            r"}{" +
            institution_or_employer + 
            r"}{" +
            localization + 
            r"}{" +
            grade + 
            r"}{" +
            description + 
            r"}" +
            "\n"
        )

    def add_cventry(
        self,
        years:str,
        degree_or_job_title:str,
        institution_or_employer:str,
        localization:str=None,
        grade:str=None,
        description:str=None,
        spacing:float=None
    ):
        """
        Makes a typical resume job / education entry
        """
        grade = '' if grade is None else grade
        description = '' if description is None else description
        spacing = self.DEFAULT_SPACING if spacing is None else spacing
        localization = '' if localization is None else localization

        self._body += self._cventry(
            years=years,
            degree_or_job_title=degree_or_job_title,
            institution_or_employer=institution_or_employer,
            localization=localization,
            grade=grade,
            description=description,
            spacing=spacing
        )

    def add_education(self, **kwargs):
        return self.add_cventry(**kwargs)

    @staticmethod
    def _cvitemwithcomment(
        header:str,
        text:str,
        comment:str,
        spacing:str
    ):
        return (
            "\n" +
            r"\cvitemwithcomment[" + 
            spacing + "em" + 
            r"]{" + 
            header + 
            r"}{" + 
            text + 
            r"}{" +
            comment + 
            r"}" + 
            "\n"
        )

    def add_cvitemwithcomment(
        self,
        header:str,
        text:str,
        comment:str,
        spacing:str=None
    ):
        spacing = self.DEFAULT_SPACING if spacing is None else spacing
        self._body += self._cvitemwithcomment(
            header=header,
            text=text,
            comment=comment,
            spacing=str(spacing)
        )

    @staticmethod
    def _cvlistitem(item:str):
        return "\n" + r"\cvlistitem{" + item + r"}" + "\n"

    def add_cvlistitem(self, item:str):
        """
        Makes a resume line with a list item
            usage: \cvlistitem[label]{item}
        """
        self._body += self._cvlistitem(item=item)

    @staticmethod
    def httplink(link:str, text:str=None):
        return r"\httplink[" + text + r"]{" + link + r"}"

    def add_httplink(self, link:str, text:str):
        """
        Makes a http hyperlink
            usage: \httplink[optional text]{link}
        """
        self._body += self.httplink(link=link, text=text)


    @staticmethod
    def emaillink(link:str, text:str):
        return r"\emaillink[" + text + r"]{" + link + r"}"

    def add_emaillink(self, link:str, text:str):
        self._body += self.emaillink(link, text)


    @staticmethod
    def quote(quotation:str):
        return r"\quote{" + quotation + r"}"

    def add_quote(self, quotation:str):
        self._body += self.quote(quotation=quotation)

    
    def create(self, path:Path=None):
        path = Path.cwd() if path is None else Path(path)
        with open(path / "cv.tex", 'w') as f:
            f.write(self.text)



#################### .sty files for `moderncv` ###############
    
class ModernCVColorStyFile:

    def __init__(
        self, 
        name:str, 
        color0_rgb:tuple, 
        color1_rgb:tuple, 
        color2_rgb:tuple
    ):
        self._name = name
        self._styfilename = self._name + '.sty'
        self._color0 = color0_rgb
        self._color1 = color1_rgb
        self._color2 = color2_rgb

        self._text = (
            "\n" +
            r"\NeedsTeXFormat{LaTeX2e}" + 
            "\n" +
            r"\ProvidesPackage{" + 
            self._name + 
            r"}"
            "\n\n\n" +
            r"\definecolor{color0}{rgb}{" + 
            f"{self._color0[0]}, {self._color0[1]}, {self._color0[2]}" +
            r"}" + 
            "\n"
            r"\definecolor{color1}{rgb}{" + 
            f"{self._color1[0]}, {self._color1[1]}, {self._color1[2]}" +
            r"}" + "\n"
            r"\definecolor{color2}{rgb}{" + 
            f"{self._color2[0]}, {self._color2[1]}, {self._color2[2]}" +
            r"}" + 
            "\n\n\n"  + 
            r"\endinput" + 
            "\n"
        )

    def create(self, path:Path=None):
        path = Path.cwd() if path is None else Path(path)
        with open(path / self._styfilename, 'w') as f:
            f.write(self._text)


class ModernCVColorBlueStyFile(ModernCVColorStyFile):
    def __init__(self):
        name = 'moderncvcolorblue'
        color0_rgb = (0,0,0)
        color1_rgb = (0.22,0.45,0.70)
        color2_rgb = (0.45,0.45,0.45)
        super().__init__(name, color0_rgb, color1_rgb, color2_rgb)


class ModernCVColorBlackStyFile(ModernCVColorStyFile):
    def __init__(self):
        name = 'moderncvcolorblack'
        color0_rgb = (0,0,0)
        color1_rgb = color0_rgb
        color2_rgb = color0_rgb
        super().__init__(name, color0_rgb, color1_rgb, color2_rgb)


class ModernCVColorGreenStyFile(ModernCVColorStyFile):
    def __init__(self):
        name = 'moderncvcolorgreen'
        color0_rgb = (0,0,0)
        color1_rgb = (0.35,0.70,0.30)
        color2_rgb = (0.45,0.45,0.45)
        super().__init__(name, color0_rgb, color1_rgb, color2_rgb)


class ModernCVColorGreyStyFile(ModernCVColorStyFile):
    def __init__(self):
        name = 'moderncvcolorgrey'
        color0_rgb = (0,0,0)
        color1_rgb = (0.55,0.55,0.55)
        color2_rgb = (0.55,0.55,0.55)
        super().__init__(name, color0_rgb, color1_rgb, color2_rgb)


class ModernCVColorOrangeStyFile(ModernCVColorStyFile):
    def __init__(self):
        name = 'moderncvcolororange'
        color0_rgb = (0,0,0)
        color1_rgb = (0.95,0.55,0.15)
        color2_rgb = (0.45,0.45,0.45)
        super().__init__(name, color0_rgb, color1_rgb, color2_rgb)

class ModernCVColorPurpleStyFile(ModernCVColorStyFile):
    def __init__(self):
        name = 'moderncvcolorpurple'
        color0_rgb = (0,0,0)
        color1_rgb = (0.50,0.33,0.80)
        color2_rgb = (0.45,0.45,0.45)
        super().__init__(name, color0_rgb, color1_rgb, color2_rgb)


class ModernCVColorRedStyFile(ModernCVColorStyFile):
    def __init__(self):
        name = 'moderncvcolorred'
        color0_rgb = (0,0,0)
        color1_rgb = (0.95,0.20,0.20)
        color2_rgb = (0.45,0.45,0.45)
        super().__init__(name, color0_rgb, color1_rgb, color2_rgb)


class ModernCVStyleStyFile:
    def __init__(
        self,
        name:str,
        required_packages:str,
        package_options:str,
        definitions:str
    ):
        self._name = name
        self._styfilename = name + ".sty"
        self._text = (
            r"""

%-------------------------------------------------------------------------------
%                identification
%-------------------------------------------------------------------------------

            """ + 
            "\n" +
            r"\NeedsTeXFormat{LaTeX2e}" + 
            "\n" +
            r"\ProvidesPackage{" + 
            self._name + 
            r"}" + 
            "\n\n\n" + 
            r"""
%-------------------------------------------------------------------------------
%                required packages
%-------------------------------------------------------------------------------

            """ + 
            required_packages + 
            r"""
%-------------------------------------------------------------------------------
%                package options
%-------------------------------------------------------------------------------

            """ + 
            package_options + 
            "\n\n" + 
            r"""
%-------------------------------------------------------------------------------
%                overall style definition
%-------------------------------------------------------------------------------

            """ + 
            definitions + 
            "\n\n"
        )

    
    def create(self, path:Path=None):
        path = Path.cwd() if path is None else Path(path)
        with open(path / self._styfilename, 'w') as f:
            f.write(self._text)


class ModernCVCompatibilityStyFile(ModernCVStyleStyFile):
    def __init__(self):
        name = 'moderncvcompatibility'

        required_packages = ""
        package_options = r"""
\DeclareOption*{}

% process given options
\ProcessOptions\relax
        """

        definitions = r"""
% compatibility with version 0.1
\newcommand*{\cvresume}[2]{\cvlistdoubleitem{#1}{#2}}

% compatibility with versions <= 0.2
% section, cvline, ... with width argument...
%\newcommand*{\section}[2][0.825]{%
%  \closesection{}%
%  \@sectionopentrue%
%  \addcontentsline{toc}{part}{#2}
%  \begin{longtable}[t]{@{}r@{\hspace{.025\textwidth}}@{}p{#1\textwidth}@{}}%
%%  \colorrule{.15\textwidth}&\mbox{\color{sectiontitlecolor}\sectionfont#2}\\[1ex]}%
%  {\color{sectionrectanglecolor}\rule{0.15\textwidth}{1ex}}&\mbox{\color{sectiontitlecolor}\sectionfont#2}\\[1ex]}%
%\newcommand*{\cvline}[3][.825]{%
%  \begin{minipage}[t]{\hintscolumnwidth}\raggedleft\small\sffamily#2\end{minipage}&\begin{minipage}[t]{\maincolumnwidth}#3\end{minipage}\\}
%\newcommand*{\cvitem}[3][.825]{%
%  \cvline[#1]{#2}{#3\vspace*{.75em}}}   % the \vspace*{} inside the cvline environment is a hack... (should conceptually be outside the environment)

% compatibility with versions <= 0.5
%\newcommand*{\cvitem}[2]{\cvline{#1}{#2}}
%\newcommand*{\moderncvstyle}[1]{\moderncvtheme{#1}}

% compatibility with versions <= 0.7
\newcommand*{\closesection}{}
\newcommand*{\emptysection}{}
\newcommand*{\sethintscolumnlength}[1]{%
  \setlength{\hintscolumnwidth}{#1}%
  \recomputelengths}
\newcommand*{\sethintscolumntowidth}[1]{%
  \settowidth{\hintscolumnwidth}{#1}%
  \recomputelengths}

% compatibility with versions <= 0.15
\newcommand*{\cvline}[2]{\cvitem{#1}{#2}}
\newcommand*{\cvlanguage}[3]{\cvitemwithcomment{#1}{#2}{#3}}
\newcommand*{\cvcomputer}[4]{\cvdoubleitem{#1}{\small#2}{#3}{\small#4}}
\newcommand*{\moderncvtheme}[2][blue]{%
  \moderncvcolor{#1}%
  \moderncvstyle{#2}}

% compatibility with versions <= 0.19
\newcommand*{\maketitle}{\makecvtitle}%
\title{}% to avoid LaTeX complaining that \maketitle is a called without first a call to \title
\newcommand*{\maketitlenamewidth}{\makecvtitlenamewidth}


\endinput


%% end of file `moderncvcompatibility.sty'.
        """
        super().__init__(name, required_packages, package_options, definitions)


class ModernCVStyleBankingStyFile(ModernCVStyleStyFile):
    def __init__(self):
        name = "moderncvstylebanking"
        required_packages = ""
        package_options = ""
        definitions = r"""
 \IfFileExists{tgpagella.sty}%
    {%
      \RequirePackage{tgpagella}%
      \renewcommand*{\familydefault}{\rmdefault}}%
    {}
%\fi

% symbols
\renewcommand*{\mobilesymbol}{\marvosymbol{72}~}
\renewcommand*{\phonesymbol}{\marvosymbol{84}~}
\renewcommand*{\faxsymbol}{\marvosymbol{117}~}
\renewcommand*{\emailsymbol}{\marvosymbol{66}~}
\renewcommand*{\homepagesymbol}{{\Large\marvosymbol{205}}~}

% commands
\newcommand*{\maketitlesymbol}{%
    {~~~{\rmfamily\textbullet}~~~}}% the \rmfamily is required to force Latin Modern fonts when using sans serif, as OMS/lmss/m/n is not defined and gets substituted by OMS/cmsy/m/n
%   internal command to add an element to the footer
%   it collects the elements in a temporary box, and checks when to flush the box
\newsavebox{\maketitlebox}%
\newsavebox{\maketitletempbox}%
\newlength{\maketitlewidth}%
\newlength{\maketitleboxwidth}%
\newif\if@firstmaketitleelement\@firstmaketitleelementtrue%
%   adds an element to the maketitle, separated by maketitlesymbol
%   usage: \addtomaketitle[maketitlesymbol]{element}
\newcommand*{\addtomaketitle}[2][\maketitlesymbol]{%
  \if@firstmaketitleelement%
    \savebox{\maketitletempbox}{\usebox{\maketitlebox}#2}%
  \else%
    \savebox{\maketitletempbox}{\usebox{\maketitlebox}#1#2}\fi%
  \settowidth{\maketitleboxwidth}{\usebox{\maketitletempbox}}%
  \ifnum\maketitleboxwidth<\maketitlewidth%
    \savebox{\maketitlebox}{\usebox{\maketitletempbox}}%
    \@firstmaketitleelementfalse%
  \else%
    \flushmaketitle{}\\%
    \savebox{\maketitlebox}{#2}%
    \savebox{\maketitletempbox}{#2}%
    \settowidth{\maketitleboxwidth}{\usebox{\maketitlebox}}%
    \@firstmaketitleelementfalse\fi}
%   internal command to flush the maketitle
\newcommand*{\flushmaketitle}{%
  \strut\usebox{\maketitlebox}%
  \savebox{\maketitlebox}{}%
  \savebox{\maketitletempbox}{}%
  \setlength{\maketitleboxwidth}{0pt}}
\renewcommand*{\maketitle}{%
  \setlength{\maketitlewidth}{0.8\textwidth}%
  \hfil%
  \parbox{\maketitlewidth}{%
    \centering%
    % name and title
    \namestyle{\@firstname~\@familyname}%
    \ifthenelse{\isundefined{\@title}}{}{\titlestyle{~|~\@title}}\\%
    % detailed information
    \addressfont\color{color2}%
    \ifthenelse{\isundefined{\@addressstreet}}{}{\addtomaketitle{\addresssymbol\@addressstreet}%
      \ifthenelse{\equal{\@addresscity}{}}{}{\addtomaketitle[~--~]{\@addresscity}}\flushmaketitle\@firstmaketitleelementtrue\\}% if \addresstreet is defined, \addresscity will always be defined but could be empty
    \ifthenelse{\isundefined{\@mobile}}{}{\addtomaketitle{\mobilesymbol\@mobile}}%
    \ifthenelse{\isundefined{\@phone}}{}{\addtomaketitle{\phonesymbol\@phone}}%
    \ifthenelse{\isundefined{\@fax}}{}{\addtomaketitle{\faxsymbol\@fax}}%
    \ifthenelse{\isundefined{\@email}}{}{\addtomaketitle{\emailsymbol\emaillink{\@email}}}%
        \ifthenelse{\isundefined{\@homepage}}{}{%
	\ifthenelse{\equal{\@homepagetitle}{}}% \homepagetitle could be empty
	{\addtomaketitle{\homepagesymbol\httplink{\@homepage}}}%
	{\addtomaketitle{\homepagesymbol\httplink[\@homepagetitle]{\@homepage}}}}%
    \ifthenelse{\isundefined{\@extrainfo}}{}{\addtomaketitle{\@extrainfo}}%
    \flushmaketitle}\\[2.5em]}% need to force a \par after this to avoid weird spacing bug at the first section if no blank line is left after \maketitle


%-------------------------------------------------------------------------------
%                resume style definition
%-------------------------------------------------------------------------------
% fonts
\renewcommand*{\namefont}{\Huge\bfseries\upshape}
\renewcommand*{\titlefont}{\Huge\mdseries\upshape}
\renewcommand*{\addressfont}{\normalsize\mdseries\upshape}
\renewcommand*{\quotefont}{\large\slshape}
\renewcommand*{\sectionfont}{\Large\bfseries\upshape}
\renewcommand*{\subsectionfont}{\large\upshape\fontseries{sb}\selectfont}
\renewcommand*{\hintfont}{\bfseries}

% styles
\renewcommand*{\namestyle}[1]{{\namefont\textcolor{color1}{#1}}}
\renewcommand*{\titlestyle}[1]{{\titlefont\textcolor{color2!85}{#1}}}
\renewcommand*{\addressstyle}[1]{{\addressfont\textcolor{color1}{#1}}}
\renewcommand*{\quotestyle}[1]{{\quotefont\textcolor{color1}{#1}}}
\renewcommand*{\sectionstyle}[1]{{\sectionfont\textcolor{color1}{#1}}}
\renewcommand*{\subsectionstyle}[1]{{\subsectionfont\textcolor{color1}{#1}}}
\renewcommand*{\hintstyle}[1]{{\hintfont\textcolor{color0}{#1}}}

% lengths
\newlength{\quotewidth}
\newlength{\hintscolumnwidth}
\setlength{\hintscolumnwidth}{0.3\textwidth}%
\newlength{\separatorcolumnwidth}
\setlength{\separatorcolumnwidth}{0.025\textwidth}%
\newlength{\maincolumnwidth}
\newlength{\doubleitemcolumnwidth}
\newlength{\listitemsymbolwidth}
\settowidth{\listitemsymbolwidth}{\listitemsymbol}
\newlength{\listitemmaincolumnwidth}
\newlength{\listdoubleitemmaincolumnwidth}

% commands
\renewcommand*{\recomputecvlengths}{%
  \setlength{\quotewidth}{0.65\textwidth}%
  % main lenghts
  \setlength{\maincolumnwidth}{\textwidth}%
  % listitem lengths
  \setlength{\listitemmaincolumnwidth}{\maincolumnwidth-\listitemsymbolwidth}%
  % doubleitem lengths
  \setlength{\doubleitemcolumnwidth}{\maincolumnwidth-\separatorcolumnwidth}%
  \setlength{\doubleitemcolumnwidth}{0.5\doubleitemcolumnwidth}%
  % listdoubleitem lengths
  \setlength{\listdoubleitemmaincolumnwidth}{\maincolumnwidth-\listitemsymbolwidth-\separatorcolumnwidth-\listitemsymbolwidth}%
  \setlength{\listdoubleitemmaincolumnwidth}{0.5\listdoubleitemmaincolumnwidth}%
  % fancyhdr lengths
  \renewcommand{\headwidth}{\textwidth}%
  % regular lengths
  \setlength{\parskip}{0\p@}}

\renewcommand*{\makecvtitle}{%
  % recompute lengths (in case we are switching from letter to resume, or vice versa)
  \recomputecvlengths%
  \maketitle%
  % optional quote
  \ifthenelse{\isundefined{\@quote}}%
    {}%
    {{\centering\begin{minipage}{\quotewidth}\centering\quotestyle{\@quote}\end{minipage}\\[2.5em]}}%
  \par}% to avoid weird spacing bug at the first section if no blank line is left after \maketitle}

\renewcommand*{\section}[1]{%
  \par\addvspace{2.5ex}%
  \phantomsection{}% reset the anchor for hyperrefs
  \addcontentsline{toc}{section}{#1}%
  \strut\sectionstyle{#1}%
  {\color{color1}\hrule}%
  \par\nobreak\addvspace{1ex}\@afterheading}

\newcommand{\subsectionfill}{\xleaders\hbox to 0.35em{\scriptsize.}\hfill}% different subsectionfills will not be perfectly aligned, but remaining space at the end of the fill will be distributed evenly between leaders, so it will be barely visible
\renewcommand*{\subsection}[1]{%
  \par\addvspace{1ex}%
  \phantomsection{}%
  \addcontentsline{toc}{subsection}{#1}%
  \strut\subsectionstyle{#1}{\color{color1}{\subsectionfill}}%
  \par\nobreak\addvspace{0.5ex}\@afterheading}

\renewcommand*{\cvitem}[3][.25em]{%
  \ifthenelse{\equal{#2}{}}{}{\hintstyle{#2}: }{#3}%
  \par\addvspace{#1}}

\renewcommand*{\cvdoubleitem}[5][.25em]{%
  \begin{minipage}[t]{\doubleitemcolumnwidth}\hintstyle{#2}: #3\end{minipage}%
  \hfill% fill of \separatorcolumnwidth
  \begin{minipage}[t]{\doubleitemcolumnwidth}\ifthenelse{\equal{#4}{}}{}{\hintstyle{#4}: }#5\end{minipage}%
  \par\addvspace{#1}}

\renewcommand*{\cvlistitem}[2][.25em]{%
  \listitemsymbol\begin{minipage}[t]{\listitemmaincolumnwidth}#2\end{minipage}%
  \par\addvspace{#1}}

\renewcommand*{\cvlistdoubleitem}[3][.25em]{%
  \cvitem[#1]{}{\listitemsymbol\begin{minipage}[t]{\listdoubleitemmaincolumnwidth}#2\end{minipage}%
  \hfill% fill of \separatorcolumnwidth
  \ifthenelse{\equal{#3}{}}%
    {}%
    {\listitemsymbol\begin{minipage}[t]{\listdoubleitemmaincolumnwidth}#3\end{minipage}}}}

\renewcommand*{\cventry}[7][.25em]{
  \begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}%
	  {\bfseries #4} & {\bfseries #5} \\%
	  {\itshape #3\ifthenelse{\equal{#6}{}}{}{, #6}} & {\itshape #2}\\%
  \end{tabular*}%
  \ifx&#7&%
    \else{\\\vbox{\small#7}}\fi%
  \par\addvspace{#1}}

\newbox{\cvitemwithcommentmainbox}
\newlength{\cvitemwithcommentmainlength}
\newlength{\cvitemwithcommentcommentlength}
\renewcommand*{\cvitemwithcomment}[4][.25em]{%
  \savebox{\cvitemwithcommentmainbox}{\ifthenelse{\equal{#2}{}}{}{\hintstyle{#2}: }#3}%
  \setlength{\cvitemwithcommentmainlength}{\widthof{\usebox{\cvitemwithcommentmainbox}}}%
  \setlength{\cvitemwithcommentcommentlength}{\maincolumnwidth-\separatorcolumnwidth-\cvitemwithcommentmainlength}%
  \begin{minipage}[t]{\cvitemwithcommentmainlength}\ifthenelse{\equal{#2}{}}{}{\hintstyle{#2}: }#3\end{minipage}%
  \hfill% fill of \separatorcolumnwidth
  \begin{minipage}[t]{\cvitemwithcommentcommentlength}\raggedleft\small\itshape#4\end{minipage}%
  \par\addvspace{#1}}

\renewenvironment{thebibliography}[1]%
  {%
    \bibliographyhead{\refname}%
%    \small%
    \begin{list}{\bibliographyitemlabel}%
      {%
        \setlength{\topsep}{0pt}%
        \setlength{\labelwidth}{0pt}%
        \setlength{\labelsep}{0pt}%
        \leftmargin\labelwidth%
        \advance\leftmargin\labelsep%
        \@openbib@code%
        \usecounter{enumiv}%
        \let\p@enumiv\@empty%
        \renewcommand\theenumiv{\@arabic\c@enumiv}}%
        \sloppy\clubpenalty4000\widowpenalty4000%
%        \sfcode`\.\@m%
%        \sfcode `\=1000\relax%
  }%
  {%
    \def\@noitemerr{\@latex@warning{Empty `thebibliography' environment}}%
    \end{list}%
  }


%-------------------------------------------------------------------------------
%                letter style definition
%-------------------------------------------------------------------------------
% commands
\renewcommand*{\recomputeletterlengths}{
  \recomputecvlengths%
  \setlength{\parskip}{6\p@}}

\renewcommand*{\makelettertitle}{%
  % recompute lengths (in case we are switching from letter to resume, or vice versa)
  \recomputeletterlengths%
  % sender block
  \maketitle%
  \par%
   % recipient block
  \begin{minipage}[t]{.5\textwidth}
    \raggedright%
    \addressfont%
    {\bfseries\upshape\@recipientname}\\%
    \@recipientaddress%
  \end{minipage}
  % date
  \hfill % US style
%  \\[1em] % UK style
  \@date\\[2em]% US informal style: "April 6, 2006"; UK formal style: "05/04/2006"
  % opening
  \raggedright%
  \@opening\\[1.5em]%
  % ensure no extra spacing after \makelettertitle due to a possible blank line
%  \ignorespacesafterend% not working
  \hspace{0pt}\par\vspace{-\baselineskip}\vspace{-\parskip}}

\renewcommand*{\makeletterclosing}{
  \@closing\\[3em]%
  {\bfseries \@firstname~\@familyname}%
  \ifthenelse{\isundefined{\@enclosure}}{}{%
    \\%
    \vfill%
    {\color{color2}\itshape\enclname: \@enclosure}}}


\endinput


%% end of file `moderncvstylebanking.sty'.
        """

        super().__init__(name, required_packages, package_options, definitions)


class ModernCVStyleCasualStyFile(ModernCVStyleStyFile):
    def __init__(self):

        name = "moderncvstylecasual"
        required_packages = ""
        package_options = r"""\RequirePackage{moderncvstyleclassic}"""
        definitions = r"""
% commands
%   footer symbol used to separate footer elements
\newcommand*{\footersymbol}{%
    {~~~{\rmfamily\textbullet}~~~}}% the \rmfamily is required to force Latin Modern fonts when using sans serif, as OMS/lmss/m/n is not defined and gets substituted by OMS/cmsy/m/n
%   internal command to add an element to the footer
%   it collects the elements in a temporary box, and checks when to flush the box
\newsavebox{\footerbox}%
\newsavebox{\footertempbox}%
\newlength{\footerwidth}%
\newlength{\footerboxwidth}%
\newif\if@firstfooterelement\@firstfooterelementtrue%
%   adds an element to the footer, separated by footersymbol
%   usage: \addtofooter[footersymbol]{element}
\newcommand*{\addtofooter}[2][\footersymbol]{%
  \if@firstfooterelement%
    \savebox{\footertempbox}{\usebox{\footerbox}#2}%
  \else%
    \savebox{\footertempbox}{\usebox{\footerbox}#1#2}\fi%
  \settowidth{\footerboxwidth}{\usebox{\footertempbox}}%
  \ifnum\footerboxwidth<\footerwidth%
    \savebox{\footerbox}{\usebox{\footertempbox}}%
    \@firstfooterelementfalse%
  \else%
    \flushfooter\\%
    \savebox{\footerbox}{#2}%
    \savebox{\footertempbox}{#2}%
    \settowidth{\footerboxwidth}{\usebox{\footerbox}}%
    \@firstfooterelementfalse\fi}
%   internal command to flush the footer
\newcommand*{\flushfooter}{%
  \strut\usebox{\footerbox}%
  \savebox{\footerbox}{}%
  \savebox{\footertempbox}{}%
  \setlength{\footerboxwidth}{0pt}}


%-------------------------------------------------------------------------------
%                resume style definition
%-------------------------------------------------------------------------------
% fonts
\renewcommand*{\namefont}{\fontsize{38}{40}\mdseries\upshape}
\renewcommand*{\addressfont}{\normalsize\mdseries\slshape}

% commands
\renewcommand*{\makecvtitle}{%
  % recompute lengths (in case we are switching from letter to resume, or vice versa)
  \recomputecvlengths%
  % ensure footer with personal information
  \makecvfooter%
  % optional picture
  \newbox{\makecvtitlepicturebox}%
  \savebox{\makecvtitlepicturebox}{%
    \ifthenelse{\isundefined{\@photo}}%
      {}%
      {%
       \setlength\fboxrule{\@photoframewidth}%
       \ifdim\@photoframewidth=0pt%
         \setlength{\fboxsep}{0pt}\fi%
       {\color{color1}\framebox{\includegraphics[width=\@photowidth]{\@photo}}}}}%
  \usebox{\makecvtitlepicturebox}%
  % name
  \@initializelength{\makecvtitlepicturewidth}%
  \settowidth{\makecvtitlepicturewidth}{\usebox{\makecvtitlepicturebox}}%
  \parbox[b]{\textwidth-\makecvtitlepicturewidth}{%
    \raggedleft\namefont{\color{color2!50}\@firstname} {\color{color2}\@familyname}}\\[-.35em]% alternate design: \MakeLowercase and no space
  {\color{color2!50}\rule{\textwidth}{.25ex}}%
  % optional title
  \ifthenelse{\equal{\@title}{}}{}{\\[1.25em]\null\hfill\titlestyle{\@title}}\\[2.5em]% \null is required as there is no box on the line after \\, so glue (and leaders) disappears; this is in contrast to after \par, where the next line starts with an indent box (even after \noindent).
  % optional quote
  \ifthenelse{\isundefined{\@quote}}%
    {}%
    {{\null\hfill\begin{minipage}{\quotewidth}\centering\quotestyle{\@quote}\end{minipage}\hfill\null\\[2.5em]}}%
  \par}% to avoid weird spacing bug at the first section if no blank line is left after \maketitle

\renewcommand*{\makecvfooter}{%
  \setlength{\footerwidth}{0.8\textwidth}%
  \fancypagestyle{plain}{%
    \fancyfoot[c]{%
      \parbox[b]{\footerwidth}{%
        \centering%
        \color{color2}\addressfont%
        \ifthenelse{\isundefined{\@addressstreet}}{}{\addtofooter[]{\addresssymbol\@addressstreet}%
          \ifthenelse{\equal{\@addresscity}{}}{}{\addtofooter[~--~]{\@addresscity}}\flushfooter\@firstfooterelementtrue\\}% if \addresstreet is defined, \addresscity will always be defined but could be empty
        \ifthenelse{\isundefined{\@mobile}}{}{\addtofooter{\mobilesymbol\@mobile}}%
        \ifthenelse{\isundefined{\@phone}}{}{\addtofooter{\phonesymbol\@phone}}%
        \ifthenelse{\isundefined{\@fax}}{}{\addtofooter{\faxsymbol\@fax}}%
        \ifthenelse{\isundefined{\@email}}{}{\addtofooter{\emailsymbol\emaillink{\@email}}}%
        	\ifthenelse{\isundefined{\@homepage}}{}{%
	\ifthenelse{\equal{\@homepagetitle}{}}% \homepagetitle could be empty
	{\addtofooter{\homepagesymbol\httplink{\@homepage}}}%
	{\addtofooter{\homepagesymbol\httplink[\@homepagetitle]{\@homepage}}}}% 
        \ifthenelse{\isundefined{\@extrainfo}}{}{\addtofooter{\@extrainfo}}%
        \ifthenelse{\lengthtest{\footerboxwidth=0pt}}{}{\flushfooter}% the lengthtest is required to avoid flushing an empty footer, which could cause a blank line due to the \\ after the address, if no other personal info is used
        }}}%
  \pagestyle{plain}}


%-------------------------------------------------------------------------------
%                letter style definition
%-------------------------------------------------------------------------------
\renewcommand*{\makelettertitle}{%
  % recompute lengths (in case we are switching from letter to resume, or vice versa)
  \recomputeletterlengths%
  % ensure footer with personal information
  \makeletterfooter%
  % recipient block
  \begin{minipage}[t]{.5\textwidth}
    \raggedright%
    \addressfont%
    {\bfseries\upshape\@recipientname}\\%
    \@recipientaddress%
  \end{minipage}
  % date
  \hfill% US style
%  \\[1em]% UK style
  \@date\\[2em]% US informal style: "April 6, 2006"; UK formal style: "05/04/2006"
  % opening
  \raggedright%
  \@opening\\[1.5em]%
  % ensure no extra spacing after \makelettertitle due to a possible blank line
%  \ignorespacesafterend% not working
  \hspace{0pt}\par\vspace{-\baselineskip}\vspace{-\parskip}}

\renewcommand*{\makeletterfooter}{%
  \setlength{\footerwidth}{0.8\textwidth}%
  \fancypagestyle{plain}{%
    \fancyfoot[c]{%
      \parbox[b]{\footerwidth}{%
        \centering%
        \addressfont\color{color2}%
        \vspace{-\baselineskip}% to cancel out the extra vertical space taken by the name (below) and ensure perfect alignment of letter and cv footers
        \strut{\bfseries\upshape\@firstname~\@familyname}\\% the \strut is required to ensure the line is exactly \baselineskip tall
        \ifthenelse{\isundefined{\@addressstreet}}{}{\addtofooter[]{\addresssymbol\@addressstreet}%
          \ifthenelse{\equal{\@addresscity}{}}{}{\addtofooter[~--~]{\@addresscity}}\flushfooter\@firstfooterelementtrue\\}% if \addresstreet is defined, \addresscity will always be defined but could be empty
        \ifthenelse{\isundefined{\@mobile}}{}{\addtofooter{\mobilesymbol\@mobile}}%
        \ifthenelse{\isundefined{\@phone}}{}{\addtofooter{\phonesymbol\@phone}}%
        \ifthenelse{\isundefined{\@fax}}{}{\addtofooter{\faxsymbol\@fax}}%
        \ifthenelse{\isundefined{\@email}}{}{\addtofooter{\emailsymbol\emaillink{\@email}}}%
        	\ifthenelse{\isundefined{\@homepage}}{}{%
	\ifthenelse{\equal{\@homepagetitle}{}}% \homepagetitle could be empty
	{\addtofooter{\homepagesymbol\httplink{\@homepage}}}%
	{\addtofooter{\homepagesymbol\httplink[\@homepagetitle]{\@homepage}}}}%
        \ifthenelse{\isundefined{\@extrainfo}}{}{\addtofooter{\@extrainfo}}%
        \ifthenelse{\lengthtest{\footerboxwidth=0pt}}{}{\flushfooter}% the lengthtest is required to avoid flushing an empty footer, which could cause a blank line due to the \\ after the address, if no other personal info is used
        }}}%
  \pagestyle{plain}}

\renewcommand*{\makeletterclosing}{
  \@closing\\[3em]%
  {\bfseries\@firstname~\@familyname}%
  \ifthenelse{\isundefined{\@enclosure}}{}{%
    \\%
    \vfil%
    {\color{color2}\itshape\enclname: \@enclosure}}%
    \vfil}


\endinput


%% end of file `moderncvstylecasual.sty'.
        """
        super().__init__(name, required_packages, package_options, definitions)


class ModernCVStyleClassicStyFile(ModernCVStyleStyFile):
    def __init__(self):
        name = "moderncvstyleclassic"
        required_packages = ""
        package_options = ""
        definitions = r"""
  \IfFileExists{lmodern.sty}%
    {\RequirePackage{lmodern}}%
    {}
%\fi

% symbols
\renewcommand*{\mobilesymbol}{\marvosymbol{72}~}
\renewcommand*{\phonesymbol}{\marvosymbol{84}~}
\renewcommand*{\faxsymbol}{\marvosymbol{117}~}
\renewcommand*{\emailsymbol}{\marvosymbol{66}~}
\renewcommand*{\homepagesymbol}{{\Large\marvosymbol{205}}~}


%-------------------------------------------------------------------------------
%                resume style definition
%-------------------------------------------------------------------------------
% fonts
\renewcommand*{\namefont}{\fontsize{34}{36}\mdseries\upshape}
\renewcommand*{\titlefont}{\LARGE\mdseries\slshape}
\renewcommand*{\addressfont}{\small\mdseries\slshape}
\renewcommand*{\quotefont}{\large\slshape}
\renewcommand*{\sectionfont}{\Large\mdseries\upshape}
\renewcommand*{\subsectionfont}{\large\mdseries\upshape}
\renewcommand*{\hintfont}{}

% styles
\renewcommand*{\namestyle}[1]{{\namefont\textcolor{color0}{#1}}}
\renewcommand*{\titlestyle}[1]{{\titlefont\textcolor{color2}{#1}}}
\renewcommand*{\addressstyle}[1]{{\addressfont\textcolor{color1}{#1}}}
\renewcommand*{\quotestyle}[1]{{\quotefont\textcolor{color1}{#1}}}
\renewcommand*{\sectionstyle}[1]{{\sectionfont\textcolor{color1}{#1}}}
\renewcommand*{\subsectionstyle}[1]{{\subsectionfont\textcolor{color1}{#1}}}
\renewcommand*{\hintstyle}[1]{{\hintfont\textcolor{color0}{#1}}}

% lengths
\newlength{\quotewidth}
\newlength{\hintscolumnwidth}
\setlength{\hintscolumnwidth}{0.175\textwidth}
\newlength{\separatorcolumnwidth}
\setlength{\separatorcolumnwidth}{0.025\textwidth}
\newlength{\maincolumnwidth}
\newlength{\doubleitemmaincolumnwidth}
\newlength{\listitemsymbolwidth}
\settowidth{\listitemsymbolwidth}{\listitemsymbol}
\newlength{\listitemmaincolumnwidth}
\newlength{\listdoubleitemmaincolumnwidth}

% commands
\renewcommand*{\recomputecvlengths}{%
  \setlength{\quotewidth}{0.65\textwidth}%
  % main lenghts
  \setlength{\maincolumnwidth}{\textwidth-\separatorcolumnwidth-\hintscolumnwidth}%
  % listitem lengths
  \setlength{\listitemmaincolumnwidth}{\maincolumnwidth-\listitemsymbolwidth}%
  % doubleitem lengths
  \setlength{\doubleitemmaincolumnwidth}{\maincolumnwidth-\hintscolumnwidth-\separatorcolumnwidth-\separatorcolumnwidth}%
  \setlength{\doubleitemmaincolumnwidth}{0.5\doubleitemmaincolumnwidth}%
  % listdoubleitem lengths
  \setlength{\listdoubleitemmaincolumnwidth}{\maincolumnwidth-\listitemsymbolwidth-\separatorcolumnwidth-\listitemsymbolwidth}%
  \setlength{\listdoubleitemmaincolumnwidth}{0.5\listdoubleitemmaincolumnwidth}%
  % fancyhdr lengths
  \renewcommand{\headwidth}{\textwidth}%
  % regular lengths
  \setlength{\parskip}{0\p@}}

% optional maketitle width to force a certain width (if set to 0pt, the width is calculated automatically)
\newlength{\makecvtitlenamewidth}
\setlength{\makecvtitlenamewidth}{0pt}% dummy value
\renewcommand*{\makecvtitle}{%
  % recompute lengths (in case we are switching from letter to resume, or vice versa)
  \recomputecvlengths%
  % optional detailed information box
  \newbox{\makecvtitledetailsbox}%
  \savebox{\makecvtitledetailsbox}{%
    \addressfont\color{color2}%
    \begin{tabular}[b]{@{}r@{}}%
      \ifthenelse{\isundefined{\@addressstreet}}{}{\makenewline\addresssymbol\@addressstreet%
        \ifthenelse{\equal{\@addresscity}{}}{}{\makenewline\@addresscity}}% if \addresstreet is defined, \addresscity will always be defined but could be empty
      \ifthenelse{\isundefined{\@mobile}}{}{\makenewline\mobilesymbol\@mobile}%
      \ifthenelse{\isundefined{\@phone}}{}{\makenewline\phonesymbol\@phone}%
      \ifthenelse{\isundefined{\@fax}}{}{\makenewline\faxsymbol\@fax}%
      \ifthenelse{\isundefined{\@email}}{}{\makenewline\emailsymbol\emaillink{\@email}}%
      \ifthenelse{\isundefined{\@homepage}}{}{%
	\ifthenelse{\equal{\@homepagetitle}{}}% \homepagetitle could be empty
	{\makenewline\homepagesymbol\httplink{\@homepage}}%
	{\makenewline\homepagesymbol\httplink[\@homepagetitle]{\@homepage}}}% 
      \ifthenelse{\isundefined{\@extrainfo}}{}{\makenewline\@extrainfo}%
    \end{tabular}
  }%
  % optional photo (pre-rendering)
  \newbox{\makecvtitlepicturebox}%
  \savebox{\makecvtitlepicturebox}{%
    \ifthenelse{\isundefined{\@photo}}%
    {}%
    {%
      \hspace*{\separatorcolumnwidth}%
      \color{color1}%
      \setlength{\fboxrule}{\@photoframewidth}%
      \ifdim\@photoframewidth=0pt%
        \setlength{\fboxsep}{0pt}\fi%
      \framebox{\includegraphics[width=\@photowidth]{\@photo}}}}%
  % name and title
  \newlength{\makecvtitledetailswidth}\settowidth{\makecvtitledetailswidth}{\usebox{\makecvtitledetailsbox}}%
  \newlength{\makecvtitlepicturewidth}\settowidth{\makecvtitlepicturewidth}{\usebox{\makecvtitlepicturebox}}%
  \ifthenelse{\lengthtest{\makecvtitlenamewidth=0pt}}% check for dummy value (equivalent to \ifdim\makecvtitlenamewidth=0pt)
    {\setlength{\makecvtitlenamewidth}{\textwidth-\makecvtitledetailswidth-\makecvtitlepicturewidth}}%
    {}%
  \begin{minipage}[b]{\makecvtitlenamewidth}%
    \namestyle{\@firstname\ \@familyname}%
    \ifthenelse{\equal{\@title}{}}{}{\\[1.25em]\titlestyle{\@title}}%
  \end{minipage}%
  \hfill%
  % detailed information
  \llap{\usebox{\makecvtitledetailsbox}}% \llap is used to suppress the width of the box, allowing overlap if the value of makecvtitlenamewidth is forced
  % optional photo (rendering)
  \usebox{\makecvtitlepicturebox}\\[2.5em]%
  % optional quote
  \ifthenelse{\isundefined{\@quote}}%
    {}%
    {{\centering\begin{minipage}{\quotewidth}\centering\quotestyle{\@quote}\end{minipage}\\[2.5em]}}%
  \par}% to avoid weird spacing bug at the first section if no blank line is left after \makecvtitle

\newlength{\baseletterheight}
\settoheight{\baseletterheight}{\sectionstyle{o}}
\setlength{\baseletterheight}{\baseletterheight-0.95ex}
\renewcommand*{\section}[1]{%
  \par\addvspace{2.5ex}%
  \phantomsection{}% reset the anchor for hyperrefs
  \addcontentsline{toc}{section}{#1}%
  \parbox[t]{\hintscolumnwidth}{\strut\raggedleft\raisebox{\baseletterheight}{\color{color1}\rule{\hintscolumnwidth}{0.95ex}}}%
  \hspace{\separatorcolumnwidth}%
  \parbox[t]{\maincolumnwidth}{\strut\sectionstyle{#1}}%
  \par\nobreak\addvspace{1ex}\@afterheading}% to avoid a pagebreak after the heading

\renewcommand*{\subsection}[1]{%
  \par\addvspace{1ex}%
  \phantomsection{}% reset the anchor for hyperrefs
  \addcontentsline{toc}{subsection}{#1}%
  \begin{tabular}{@{}p{\hintscolumnwidth}@{\hspace{\separatorcolumnwidth}}p{\maincolumnwidth}@{}}%
 	  \raggedleft\hintstyle{} &{\strut\subsectionstyle{#1}}%
  \end{tabular}%
  \par\nobreak\addvspace{0.5ex}\@afterheading}% to avoid a pagebreak after the heading

\renewcommand*{\cvitem}[3][.25em]{%
  \begin{tabular}{@{}p{\hintscolumnwidth}@{\hspace{\separatorcolumnwidth}}p{\maincolumnwidth}@{}}%
 	  \raggedleft\hintstyle{#2} &{#3}%
  \end{tabular}%
  \par\addvspace{#1}}

\renewcommand*{\cvdoubleitem}[5][.25em]{%
 \cvitem[#1]{#2}{%
   \begin{minipage}[t]{\doubleitemmaincolumnwidth}#3\end{minipage}%
   \hfill% fill of \separatorcolumnwidth
   \begin{minipage}[t]{\hintscolumnwidth}\raggedleft\hintstyle{#4}\end{minipage}%
   \hspace*{\separatorcolumnwidth}%
   \begin{minipage}[t]{\doubleitemmaincolumnwidth}#5\end{minipage}}}

\renewcommand*{\cvlistitem}[2][.25em]{%
  \cvitem[#1]{}{\listitemsymbol\begin{minipage}[t]{\listitemmaincolumnwidth}#2\end{minipage}}}

\renewcommand*{\cvlistdoubleitem}[3][.25em]{%
  \cvitem[#1]{}{\listitemsymbol\begin{minipage}[t]{\listdoubleitemmaincolumnwidth}#2\end{minipage}%
  \hfill% fill of \separatorcolumnwidth
  \ifthenelse{\equal{#3}{}}%
    {}%
    {\listitemsymbol\begin{minipage}[t]{\listdoubleitemmaincolumnwidth}#3\end{minipage}}}}

\renewcommand*{\cventry}[7][.25em]{%
  \cvitem[#1]{#2}{%
    {\bfseries#3}%
    \ifthenelse{\equal{#4}{}}{}{, {\slshape#4}}%
    \ifthenelse{\equal{#5}{}}{}{, #5}%
    \ifthenelse{\equal{#6}{}}{}{, #6}%
    .\strut%
    \ifx&#7&%
      \else{\newline{}\begin{minipage}[t]{\linewidth}\small#7\end{minipage}}\fi}}

\newbox{\cvitemwithcommentmainbox}
\newlength{\cvitemwithcommentmainlength}
\newlength{\cvitemwithcommentcommentlength}
\renewcommand*{\cvitemwithcomment}[4][.25em]{%
  \savebox{\cvitemwithcommentmainbox}{{\bfseries#3}}%
  \setlength{\cvitemwithcommentmainlength}{\widthof{\usebox{\cvitemwithcommentmainbox}}}%
  \setlength{\cvitemwithcommentcommentlength}{\maincolumnwidth-\separatorcolumnwidth-\cvitemwithcommentmainlength}%
  \cvitem[#1]{#2}{%
    \begin{minipage}[t]{\cvitemwithcommentmainlength}\bfseries#3\end{minipage}%
    \hfill% fill of \separatorcolumnwidth
    \begin{minipage}[t]{\cvitemwithcommentcommentlength}\raggedleft\small\itshape#4\end{minipage}}}

\renewenvironment{thebibliography}[1]%
  {%
    \bibliographyhead{\refname}%
%    \small%
    \begin{list}{\bibliographyitemlabel}%
      {%
        \setlength{\topsep}{0pt}%
        \setlength{\labelwidth}{\hintscolumnwidth}%
        \setlength{\labelsep}{\separatorcolumnwidth}%
        \leftmargin\labelwidth%
        \advance\leftmargin\labelsep%
        \@openbib@code%
        \usecounter{enumiv}%
        \let\p@enumiv\@empty%
        \renewcommand\theenumiv{\@arabic\c@enumiv}}%
        \sloppy\clubpenalty4000\widowpenalty4000%
%        \sfcode`\.\@m%
%        \sfcode `\=1000\relax%
  }%
  {%
    \def\@noitemerr{\@latex@warning{Empty `thebibliography' environment}}%
    \end{list}%
  }


%-------------------------------------------------------------------------------
%                letter style definition
%-------------------------------------------------------------------------------
% commands
\renewcommand*{\recomputeletterlengths}{%
  \recomputecvlengths%
  \setlength{\parskip}{6\p@}}

\renewcommand*{\makelettertitle}{%
  % recompute lengths (in case we are switching from letter to resume, or vice versa)
  \recomputeletterlengths%
  % sender contact info
  \hfill%
  \begin{minipage}{.5\textwidth}%
    \raggedleft%
    \addressfont\textcolor{color2}{%
      {\bfseries\upshape\@firstname~\@familyname}\@firstdetailselementfalse%
      \ifthenelse{\isundefined{\@addressstreet}}{}{\makenewline\addresssymbol\@addressstreet%
        \ifthenelse{\equal{\@addresscity}{}}{}{\makenewline\@addresscity}}%
      \ifthenelse{\isundefined{\@mobile}}{}{\makenewline\mobilesymbol\@mobile}%
      \ifthenelse{\isundefined{\@phone}}{}{\makenewline\phonesymbol\@phone}%
      \ifthenelse{\isundefined{\@fax}}{}{\makenewline\faxsymbol\@fax}%
      \ifthenelse{\isundefined{\@email}}{}{\makenewline\emailsymbol\emaillink{\@email}}%
     \ifthenelse{\isundefined{\@homepage}}{}{%
	\ifthenelse{\equal{\@homepagetitle}{}}% \homepagetitle could be empty
	{\makenewline\homepagesymbol\httplink{\@homepage}}%
	{\makenewline\homepagesymbol\httplink[\@homepagetitle]{\@homepage}}}%
      \ifthenelse{\isundefined{\@extrainfo}}{}{\makenewline\@extrainfo}}%
    \end{minipage}\\[1em]
  % recipient block
  \begin{minipage}[t]{.5\textwidth}
    \raggedright%
    \addressfont%
    {\bfseries\upshape\@recipientname}\\%
    \@recipientaddress%
  \end{minipage}
  % date
  \hfill% US style
%  \\[1em]% UK style
  \@date\\[2em]% US informal style: "January 1, 1900"; UK formal style: "01/01/1900"
  % opening
  \raggedright%
  \@opening\\[1.5em]%
  % ensure no extra spacing after \makelettertitle due to a possible blank line
%  \ignorespacesafterend% not working
  \hspace{0pt}\par\vspace{-\baselineskip}\vspace{-\parskip}}

\renewcommand*{\makeletterclosing}{
  \@closing\\[3em]%
  {\bfseries \@firstname~\@familyname}%
  \ifthenelse{\isundefined{\@enclosure}}{}{%
    \\%
    \vfill%
    {\color{color2}\itshape\enclname: \@enclosure}}}


\endinput


%% end of file `moderncvstyleclassic.sty'.
        """
        super().__init__(name, required_packages, package_options, definitions)


class ModernCVStyleEmptyStyFile(ModernCVStyleStyFile):
    def __init__(self):
        name = "moderncvstyleempty"
        required_packages = ""
        package_options = ""
        definitions = r"\endinput" + "\n" + r"%% end of file `moderncvstyleempty.sty'."
        super().__init__(name, required_packages, package_options, definitions)


class ModernCVStyleOldStyFile(ModernCVStyleStyFile):
    def __init__(self):
        name = "moderncvstyleoldstyle"
        required_packages = r"\RequirePackage{changepage}"
        package_options = ""
        definitions = r"""
  \IfFileExists{kurier.sty}%
    {\RequirePackage[light,math]{kurier}}%
    {}
%\fi

% symbols
\renewcommand*{\listitemsymbol}{\labelitemi~}
\renewcommand*{\addresssymbol}{}
\renewcommand*{\mobilesymbol}{\textbf{M}~}
\renewcommand*{\phonesymbol}{\textbf{T}~}
\renewcommand*{\faxsymbol}{\textbf{F}~}
\renewcommand*{\emailsymbol}{\textbf{E}~}
\renewcommand*{\homepagesymbol}{}


%-------------------------------------------------------------------------------
%                resume style definition
%-------------------------------------------------------------------------------
% fonts
\renewcommand*{\namefont}{\fontsize{34}{36}\mdseries\upshape}
\renewcommand*{\titlefont}{\LARGE\mdseries\slshape}
\renewcommand*{\addressfont}{\fontsize{8.7}{11}\mdseries}
\renewcommand*{\quotefont}{\large\itshape}
\renewcommand*{\sectionfont}{\Large\bfseries\upshape}
\renewcommand*{\subsectionfont}{\large\bfseries\itshape}
\renewcommand*{\hintfont}{\bfseries}

% styles
\renewcommand*{\namestyle}[1]{{\namefont\textcolor{color0}{#1}}}
\renewcommand*{\titlestyle}[1]{{\titlefont\textcolor{color2}{#1}}}
\renewcommand*{\addressstyle}[1]{{\addressfont\textcolor{color2}{#1}}}
\renewcommand*{\quotestyle}[1]{{\quotefont\textcolor{color1}{#1}}}
\renewcommand*{\sectionstyle}[1]{{\sectionfont\textcolor{color1}{#1}}}
\renewcommand*{\subsectionstyle}[1]{{\subsectionfont\textcolor{color1}{#1}}}
\renewcommand*{\hintstyle}[1]{{\hintfont\textcolor{color0}{#1}}}

% lengths
\newlength{\quotewidth}
\newlength{\hintscolumnwidth}
\setlength{\hintscolumnwidth}{0.3\textwidth}%
\newlength{\separatorcolumnwidth}
\setlength{\separatorcolumnwidth}{0.025\textwidth}%
\newlength{\maincolumnwidth}
\newlength{\doubleitemcolumnwidth}
\newlength{\listitemsymbolwidth}
\settowidth{\listitemsymbolwidth}{\listitemsymbol}
\newlength{\listitemmaincolumnwidth}
\newlength{\listdoubleitemmaincolumnwidth}

% commands
\setlength{\marginparwidth}{0\p@}%
\setlength{\marginparsep}{0\p@}
\renewcommand*{\recomputecvlengths}{%
  % regular lengths
  \changepage{}{+\marginparwidth+\marginparsep}{}{}{}{}{}{}{}% if a letter was typeset before the resume, \marginparwidth and \marginparsep will be non-zero; otherwise, this has no effect
  \setlength{\marginparwidth}{0\p@}%
  \setlength{\marginparsep}{0\p@}
  \setlength{\parskip}{0\p@}%
  % maketitle lengths
  \setlength{\quotewidth}{0.65\textwidth}%
  % main lenghts
  \setlength{\maincolumnwidth}{\textwidth-\hintscolumnwidth-\separatorcolumnwidth}%
  % listitem lengths
  \setlength{\listitemmaincolumnwidth}{\maincolumnwidth-\listitemsymbolwidth}%
  % doubleitem lengths
  \setlength{\doubleitemcolumnwidth}{\maincolumnwidth-\separatorcolumnwidth}%
  \setlength{\doubleitemcolumnwidth}{0.5\doubleitemcolumnwidth}%
  % listdoubleitem lengths
  \setlength{\listdoubleitemmaincolumnwidth}{\maincolumnwidth-\listitemsymbolwidth-\separatorcolumnwidth-\listitemsymbolwidth}%
  \setlength{\listdoubleitemmaincolumnwidth}{0.5\listdoubleitemmaincolumnwidth}%
  % fancyhdr lengths
  \renewcommand{\headwidth}{\textwidth}}

\newcommand{\makecvinfo}[1]{%
  \newbox{\makecvinfobox}%
  \savebox{\makecvinfobox}{\parbox[t]{\hintscolumnwidth}{#1}}%
  \newlength{\makecvinfoheight}%
  \setlength{\makecvinfoheight}{\totalheightof{\usebox{\makecvinfobox}}}% the total height of the parbox is the sum of its height (\the\ht\makeinfobox) and its depth (\the\dp\makeinfobox); the \totalheightof command is provided by the "calc" package
  \usebox{\makecvinfobox}\vspace{-\makecvinfoheight}%
  \newlength{\leftcolumnwidth}%
  \setlength{\leftcolumnwidth}{\hintscolumnwidth+\separatorcolumnwidth}%
  \par\vspace{-\baselineskip}\vspace{-\parskip}\leftskip=\leftcolumnwidth}

\renewcommand*{\makecvtitle}{
  % recompute lengths (in case we are switching from letter to resume, or vice versa)
  \recomputecvlengths%
  % optional picture box
  \newbox{\makecvtitlepicturebox}%
  \savebox{\makecvtitlepicturebox}{%
    \ifthenelse{\isundefined{\@photo}}%
    {}%
    {%
      \color{color1}%
      \setlength\fboxrule{\@photoframewidth}%
      \ifdim\@photoframewidth=0pt%
        \setlength{\fboxsep}{0pt}\fi%
      \framebox{\includegraphics[width=\@photowidth]{\@photo}}}}%
  % name and title
  \newlength{\makecvtitlepicturewidth}\settowidth{\makecvtitlepicturewidth}{\usebox{\makecvtitlepicturebox}}%
  \newlength{\makecvtitlenamewidth}\setlength{\makecvtitlenamewidth}{\textwidth-\makecvtitlepicturewidth}%
  \begin{minipage}[b]{\makecvtitlenamewidth}%
    \namestyle{\@firstname\ \@familyname}%
    \ifthenelse{\equal{\@title}{}}{}{\\[1.25em]\titlestyle{\@title}}%
  \end{minipage}%
  % optional photo
  \usebox{\makecvtitlepicturebox}\\[2.5em]%
   % optional quote
  \ifthenelse{\isundefined{\@quote}}%
    {}%
    {{\centering\begin{minipage}{\quotewidth}\centering\quotestyle{\@quote}\end{minipage}\\[2.5em]}}%
  % optional details
  \makecvinfo{%
    \addressfont\color{color2}%
    \ifthenelse{\isundefined{\@addressstreet}}{}{\makenewline\addresssymbol\@addressstreet%
      \ifthenelse{\equal{\@addresscity}{}}{}{\makenewline\@addresscity}}% if \addresstreet is defined, \addresscity will always be defined but could be empty
    \ifthenelse{\isundefined{\@mobile}}{}{\makenewline\mobilesymbol\@mobile}%
    \ifthenelse{\isundefined{\@phone}}{}{\makenewline\phonesymbol\@phone}%
    \ifthenelse{\isundefined{\@fax}}{}{\makenewline\faxsymbol\@fax}%
    \ifthenelse{\isundefined{\@email}}{}{\makenewline\emailsymbol\emaillink{\@email}}%
    \ifthenelse{\isundefined{\@homepage}}{}{%
	\ifthenelse{\equal{\@homepagetitle}{}}% \homepagetitle could be empty
	{\makenewline\homepagesymbol\httplink{\@homepage}}%
	{\makenewline\homepagesymbol\httplink[\@homepagetitle]{\@homepage}}}% 
    \ifthenelse{\isundefined{\@extrainfo}}{}{\makenewline\@extrainfo}}}

\renewcommand*{\section}[1]{%
  \par\addvspace{2.5ex}%
  \phantomsection{}% reset the anchor for hyperrefs
  \addcontentsline{toc}{section}{#1}%
  \strut\sectionstyle{#1}%
  \par\nobreak\addvspace{1ex}\@afterheading}% to avoid a pagebreak after the heading

\renewcommand*{\subsection}[1]{%
  \par\addvspace{1ex}%
  \phantomsection{}% reset the anchor for hyperrefs
  \addcontentsline{toc}{subsection}{#1}%
  \strut\subsectionstyle{#1}%
  \par\nobreak\addvspace{0.5ex}\@afterheading}% to avoid a pagebreak after the heading

\renewcommand*{\cvitem}[3][.25em]{%
  \ifthenelse{\equal{#2}{}}{}{\hintstyle{#2}: }{#3}%
  \par\addvspace{#1}}

\renewcommand*{\cvdoubleitem}[5][.25em]{%
  \begin{minipage}[t]{\doubleitemcolumnwidth}\hintstyle{#2}: #3\end{minipage}%
  \hfill% fill of \separatorcolumnwidth
  \begin{minipage}[t]{\doubleitemcolumnwidth}\ifthenelse{\equal{#4}{}}{}{\hintstyle{#4}: }#5\end{minipage}%
  \par\addvspace{#1}}

\renewcommand*{\cvlistitem}[2][.25em]{%
  \cvitem[#1]{}{\listitemsymbol\begin{minipage}[t]{\listitemmaincolumnwidth}#2\end{minipage}}}

\renewcommand*{\cvlistdoubleitem}[3][.25em]{%
  \cvitem[#1]{}{\listitemsymbol\begin{minipage}[t]{\listdoubleitemmaincolumnwidth}#2\end{minipage}%
  \hfill% fill of \separatorcolumnwidth
  \ifthenelse{\equal{#3}{}}%
    {}%
    {\listitemsymbol\begin{minipage}[t]{\listdoubleitemmaincolumnwidth}#3\end{minipage}}}}

\newbox{\cventryyearbox}
\newlength{\cventrytitleboxwidth}
\renewcommand*{\cventry}[7][.25em]{%
  \savebox{\cventryyearbox}{%
    \hspace*{2\separatorcolumnwidth}%
    \hintstyle{#2}}%
  \setlength{\cventrytitleboxwidth}{\widthof{\usebox{\cventryyearbox}}}%
  \setlength{\cventrytitleboxwidth}{\maincolumnwidth-\cventrytitleboxwidth}%
  \begin{minipage}{\maincolumnwidth}%
    \parbox[t]{\cventrytitleboxwidth}{%
      \strut%
      {\bfseries#3}%
      \ifthenelse{\equal{#4}{}}{}{, {\slshape#4}}%
      \ifthenelse{\equal{#5}{}}{}{, #5}%
      \ifthenelse{\equal{#6}{}}{}{, #6}%
      .\strut}%
    \usebox{\cventryyearbox}%
  \end{minipage}%
  \ifx&#7&%
    \else{%
      \newline{}%
      \begin{minipage}[t]{\maincolumnwidth}%
        \small%
        #7%
      \end{minipage}}\fi%
  \par\addvspace{#1}}

\newbox{\cvitemwithcommentmainbox}
\newlength{\cvitemwithcommentmainlength}
\newlength{\cvitemwithcommentcommentlength}
\renewcommand*{\cvitemwithcomment}[4][.25em]{%
  \savebox{\cvitemwithcommentmainbox}{\ifthenelse{\equal{#2}{}}{}{\hintstyle{#2}: }#3}%
  \setlength{\cvitemwithcommentmainlength}{\widthof{\usebox{\cvitemwithcommentmainbox}}}%
  \setlength{\cvitemwithcommentcommentlength}{\maincolumnwidth-\separatorcolumnwidth-\cvitemwithcommentmainlength}%
  \begin{minipage}[t]{\cvitemwithcommentmainlength}\ifthenelse{\equal{#2}{}}{}{\hintstyle{#2}: }#3\end{minipage}%
  \hfill% fill of \separatorcolumnwidth
  \begin{minipage}[t]{\cvitemwithcommentcommentlength}\raggedleft\small\itshape#4\end{minipage}%
  \par\addvspace{#1}}

\renewenvironment{thebibliography}[1]%
  {%
    \bibliographyhead{\refname}%
%    \small%
    \begin{list}{\bibliographyitemlabel}%
      {%
        \setlength{\topsep}{0pt}%
        \setlength{\labelwidth}{\hintscolumnwidth}%
        \setlength{\labelsep}{\separatorcolumnwidth}%
        \leftmargin\labelwidth%
        \advance\leftmargin\labelsep%
        \@openbib@code%
        \usecounter{enumiv}%
        \let\p@enumiv\@empty%
        \renewcommand\theenumiv{\@arabic\c@enumiv}}%
        \sloppy\clubpenalty4000\widowpenalty4000%
%        \sfcode`\.\@m%
%        \sfcode `\=1000\relax%
  }%
  {%
    \def\@noitemerr{\@latex@warning{Empty `thebibliography' environment}}%
    \end{list}%
  }


%-------------------------------------------------------------------------------
%                letter style definition
%-------------------------------------------------------------------------------
% commands
%\newlength{\textwidthdelta}%
\renewcommand*{\recomputeletterlengths}{%
  \recomputecvlengths%
  \setlength{\parskip}{6\p@}%
  \leftskip=0pt%
%  \setlength{\textwidthdelta}{+\marginparwidth+\marginparsep}%
  \setlength{\marginparwidth}{\hintscolumnwidth}%
  \setlength{\marginparsep}{2\separatorcolumnwidth}%
%  \addtolength{\textwidthdelta}{-\marginparwidth-\marginparsep}%
%  \changepage{}{\textwidthdelta}{-\textwidthdelta}{}{}{}{}{}{}%\changepage{<textheight>}{<textwidth>}{<evensidemargin>}{<oddsidemargin>}{<columnsep>}{<topmargin>}{<headheight>}{<headsep>}{<footskip>}
  \changepage{}{-\marginparwidth-\marginparsep}{}{}{}{}{}{}{}%\changepage{<textheight>}{<textwidth>}{<evensidemargin>}{<oddsidemargin>}{<columnsep>}{<topmargin>}{<headheight>}{<headsep>}{<footskip>}
  }

\renewcommand*{\makelettertitle}{%
  % recompute lengths (in case we are switching from letter to resume, or vice versa)
  \recomputeletterlengths%
  % recipient block
  {\addressfont%
    {\bfseries\upshape\@recipientname}\\%
    \@recipientaddress}\\[1em]%
  % date
  \@date\\[2em]%
  % opening
  \@opening\\[1.5em]%
  % sender contact info
  \hspace{0pt}%
  \marginpar{%
    \addressfont\textcolor{color2}{%
      {\bfseries\@firstname~\@familyname}\@firstdetailselementfalse%
      \ifthenelse{\isundefined{\@addressstreet}}{}{\makenewline\addresssymbol\@addressstreet%
        \ifthenelse{\equal{\@addresscity}{}}{}{\makenewline\@addresscity}}%
      \ifthenelse{\isundefined{\@mobile}}{}{\makenewline\mobilesymbol\@mobile}%
      \ifthenelse{\isundefined{\@phone}}{}{\makenewline\phonesymbol\@phone}%
      \ifthenelse{\isundefined{\@fax}}{}{\makenewline\faxsymbol\@fax}%
      \ifthenelse{\isundefined{\@email}}{}{\makenewline\emailsymbol\emaillink{\@email}}%
      \ifthenelse{\isundefined{\@homepage}}{}{%
	\ifthenelse{\equal{\@homepagetitle}{}}% \homepagetitle could be empty
	{\makenewline\homepagesymbol\httplink{\@homepage}}%
	{\makenewline\homepagesymbol\httplink[\@homepagetitle]{\@homepage}}}% 
      \ifthenelse{\isundefined{\@extrainfo}}{}{\makenewline\@extrainfo}}}%
  % ensure no extra spacing after \makelettertitle due to a possible blank line
%  \ignorespacesafterend% not working
  \par\vspace{-\baselineskip}\vspace{-\parskip}}

\renewcommand*{\makeletterclosing}{
  \@closing\\[3em]%
  {\bfseries\@firstname~\@familyname}%
  \ifthenelse{\isundefined{\@enclosure}}{}{%
    \\%
    \vfill%
    {\color{color2}\itshape\enclname: \@enclosure}}}


\endinput


%% end of file `moderncvstyleoldstyle.sty'.
        """
        super().__init__(name, required_packages, package_options, definitions)


class TweakListStyFile:
    def __init__(self):
        self._styfilename = "tweaklist.sty"
        self._text = r"""
%% start of file `tweaklist.sty'.


% hooks for the itemize environment
\def\itemhook{}
\def\itemhooki{}
\def\itemhookii{}
\def\itemhookiii{}
\def\itemhookiv{}
% hooks for the enumerate environment
\def\enumhook{}
\def\enumhooki{}
\def\enumhookii{}
\def\enumhookiii{}
\def\enumhookiv{}
% hook for the description environment
\def\deschook{}
% original environment definitions, with hooks added
\def\enumerate{%
  \ifnum \@enumdepth >\thr@@\@toodeep\else
    \advance\@enumdepth\@ne
    \edef\@enumctr{enum\romannumeral\the\@enumdepth}%
      \expandafter
      \list
        \csname label\@enumctr\endcsname
        {%
          \enumhook \csname enumhook\romannumeral\the\@enumdepth\endcsname%
          \usecounter\@enumctr\def\makelabel##1{\hss\llap{##1}}%
        }%
  \fi}
\def\itemize{%
  \ifnum \@itemdepth >\thr@@\@toodeep\else
    \advance\@itemdepth\@ne
    \edef\@itemitem{labelitem\romannumeral\the\@itemdepth}%
    \expandafter
    \list
      \csname\@itemitem\endcsname
      {%
        \itemhook \csname itemhook\romannumeral\the\@itemdepth\endcsname%
        \def\makelabel##1{\hss\llap{##1}}%
      }%
  \fi}
\newenvironment{description}
  {\list{}{\deschook\labelwidth\z@ \itemindent-\leftmargin
           \let\makelabel\descriptionlabel}}
  {\endlist}
        """


    def create(self, path:Path=None):
        path = Path.cwd() if path is None else Path(path)
        with open(path / self._styfilename, 'w') as f:
            f.write(self._text)


class ModernCVClsFile:
    def __init__(self):
        self._filename = "moderncv.cls"
        self._text = r"""

%% start of file `moderncv.cls'.
%% Copyright 2006-2012 Xavier Danaux (xdanaux@gmail.com).
%
% This work may be distributed and/or modified under the
% conditions of the LaTeX Project Public License version 1.3c,
% available at http://www.latex-project.org/lppl/.


%-------------------------------------------------------------------------------
%                identification
%-------------------------------------------------------------------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{moderncv}[2012/10/31 v1.2.0 modern curriculum vitae and letter document class]


%-------------------------------------------------------------------------------
%                class options
%
% (need to be done before the external package loading, for example because
% we need \paperwidth, \paperheight and \@ptsize to be defined before loading
% geometry and fancyhdr)
%-------------------------------------------------------------------------------
% paper size option
\DeclareOption{a4paper}{
  \setlength\paperheight{297mm}
  \setlength\paperwidth{210mm}}
\DeclareOption{a5paper}{
  \setlength\paperheight{210mm}
  \setlength\paperwidth{148mm}}
\DeclareOption{b5paper}{
  \setlength\paperheight{250mm}
  \setlength\paperwidth{176mm}}
\DeclareOption{letterpaper}{
  \setlength\paperheight{11in}
  \setlength\paperwidth{8.5in}}
\DeclareOption{legalpaper}{
  \setlength\paperheight{14in}
  \setlength\paperwidth{8.5in}}
\DeclareOption{executivepaper}{
  \setlength\paperheight{10.5in}
  \setlength\paperwidth{7.25in}}
\DeclareOption{landscape}{
  \setlength\@tempdima{\paperheight}
  \setlength\paperheight{\paperwidth}
  \setlength\paperwidth{\@tempdima}}

% font size options
\newcommand\@ptsize{}
\DeclareOption{10pt}{\renewcommand\@ptsize{0}}
\DeclareOption{11pt}{\renewcommand\@ptsize{1}}
\DeclareOption{12pt}{\renewcommand\@ptsize{2}}

% font type options
\DeclareOption{sans}{\AtBeginDocument{\renewcommand{\familydefault}{\sfdefault}}}
\DeclareOption{roman}{\AtBeginDocument{\renewcommand{\familydefault}{\rmdefault}}}

% draft/final option
\DeclareOption{draft}{\setlength\overfullrule{5pt}}
\DeclareOption{final}{\setlength\overfullrule{0pt}}

% execute default options
\ExecuteOptions{a4paper,11pt,final}

% process given options
\ProcessOptions\relax
\input{size1\@ptsize.clo}


%-------------------------------------------------------------------------------
%                required packages
%-------------------------------------------------------------------------------
% \AtEndPreamble hook (loading etoolbox instead of defining the macro, as to avoid incompatibilities with etoolbox (and packages relying on it) defining the macro too)
\RequirePackage{etoolbox}
%\let\@endpreamblehook\@empty
%\def\AtEndPreamble{\g@addto@macro\@endpreamblehook}
%\let\document@original\document
%\def\document{\endgroup\@endpreamblehook\begingroup\document@original}

% if... then... else... constructs
\RequirePackage{ifthen}
% TODO: move to xifthen and \isempty{<arg>} instead of \equal{<arg>}{}

% color
\RequirePackage{xcolor}

% font loading
%\usepackage{ifxetex,ifluatex}
%\newif\ifxetexorluatex
%\ifxetex
%  \xetexorluatextrue
%\else
%  \ifluatex
%    \xetexorluatextrue
%  \else
%    \xetexorluatexfalse
%  \fi
%\fi
% automatic loading of latin modern fonts
%\ifxetexorluatex
%  \RequirePackage{fontspec}
%  \defaultfontfeatures{Ligatures=TeX}
%  \RequirePackage{unicode-math}
%  \setmainfont{Latin Modern}
%  \setsansfont{Latin Modern Sans}
%  \setmathfont{Latin Modern Math}
%\else
  \RequirePackage[T1]{fontenc}
  \IfFileExists{lmodern.sty}%
    {\RequirePackage{lmodern}}%
    {}
%\fi

% MarVoSym font for symbols
%\RequirePackage{marvosym}
\newcommand*{\marvosymbol}[1]{}
%\ifxetexorluatex
%  \renewcommand*{\marvosymbol}[1]{{\fontspec{MarVoSym}\char#1}}
%\else
  \renewcommand*{\marvosymbol}[1]{{\fontfamily{mvs}\fontencoding{U}\fontseries{m}\fontshape{n}\selectfont\char#1}}
%\fi

% hyper links (hyperref is loaded at the end of the preamble to pass options required by loaded packages such as CJK)
\RequirePackage{url}
\urlstyle{tt}
\AtEndPreamble{
  \pagenumbering{arabic}% has to be issued before loading hyperref, as to set \thepage and hence to avoid hyperref issuing a warning and setting pdfpagelabels=false
  \RequirePackage[unicode]{hyperref}% unicode is required for unicode pdf metadata
  \hypersetup{
    breaklinks,
    baseurl       = http://,
    pdfborder     = 0 0 0,
    pdfpagemode   = UseNone,% do not show thumbnails or bookmarks on opening
    pdfstartpage  = 1,
    pdfcreator    = {\LaTeX{} with 'moderncv' package},
%    pdfproducer   = {\LaTeX{}},% will/should be set automatically to the correct TeX engine used
    bookmarksopen = true,
    bookmarksdepth= 2,% to show sections and subsections
    pdfauthor     = {\@firstname{}~\@familyname{}},
    pdftitle      = {\@firstname{}~\@familyname{} -- \@title{}},
    pdfsubject    = {Resum\'{e} of \@firstname{}~\@familyname{}},
    pdfkeywords   = {\@firstname{}~\@familyname{}, curriculum vit\ae{}, resum\'{e}}}}

% graphics
\RequirePackage{graphicx}

% headers and footers
\RequirePackage{fancyhdr}
\fancypagestyle{plain}{
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
  \fancyhf{}}
% page numbers in footer if more than 1 page
\newif\if@displaypagenumbers\@displaypagenumberstrue
\newcommand*{\nopagenumbers}{\@displaypagenumbersfalse}
\AtEndPreamble{%
  \AtBeginDocument{%
    \if@displaypagenumbers%
      \@ifundefined{r@lastpage}{}{%
        \ifthenelse{\pageref{lastpage}>1}{%
          \newlength{\pagenumberwidth}%
          \settowidth{\pagenumberwidth}{\color{color2}\addressfont\itshape\strut\thepage/\pageref{lastpage}}%
          \fancypagestyle{plain}{%
            \fancyfoot[r]{\parbox[b]{\pagenumberwidth}{\color{color2}\addressfont\itshape\strut\thepage/\pageref{lastpage}}}}% the parbox is required to ensure alignment with a possible center footer (e.g., as in the casual style)
          \pagestyle{plain}}{}}%
      \AtEndDocument{\label{lastpage}}\else\fi}}
\pagestyle{plain}

% lengths calculations
\RequirePackage{calc}

% advanced command arguments (LaTeX 3)
\RequirePackage{xargs}
% TODO (?): replace all \newcommand by \NewDocumentCommand

% micro-typography (e.g., character protrusion, font expansion, hyphenatable letterspacing)
\RequirePackage{microtype}

% compatibility package with older versions of moderncv
\RequirePackageWithOptions{moderncvcompatibility}


%-------------------------------------------------------------------------------
%                class definition
%-------------------------------------------------------------------------------
% minimal base settings
\setlength\lineskip{1\p@}
\setlength\normallineskip{1\p@}
\renewcommand\baselinestretch{}
\setlength{\parindent}{0\p@}
\setlength{\parskip}{0\p@}
\setlength\columnsep{10\p@}
\setlength\columnseprule{0\p@}
\setlength\fboxsep{3\p@}
\setlength\fboxrule{.4\p@}
\setlength\arrayrulewidth{.4\p@}
\setlength\doublerulesep{2\p@}

% not set on purpose
%\setlength\arraycolsep{5\p@}
%\setlength\tabcolsep{6\p@}
%\setlength\tabbingsep{\labelsep}

\raggedbottom
\onecolumn


%-------------------------------------------------------------------------------
%                overall design commands definitions
%-------------------------------------------------------------------------------
% elements
\newcommand*{\firstname}[1]{\def\@firstname{#1}}
\newcommand*{\familyname}[1]{\def\@familyname{#1}}
\renewcommand*{\title}[1]{\def\@title{#1}}
\newcommand*{\address}[2]{\def\@addressstreet{#1}\def\@addresscity{#2}}
\newcommand*{\mobile}[1]{\def\@mobile{#1}}
\newcommand*{\phone}[1]{\def\@phone{#1}}
\newcommand*{\fax}[1]{\def\@fax{#1}}
\newcommand*{\email}[1]{\def\@email{#1}}
\newcommand*{\homepage}[2]{\def\@homepage{#1}\def\@homepagetitle{#2}}

% colors
\definecolor{color0}{rgb}{0,0,0}% main default color, normally left to black
\definecolor{color1}{rgb}{0,0,0}% primary theme color
\definecolor{color2}{rgb}{0,0,0}% secondary theme color
\definecolor{color3}{rgb}{0,0,0}% tertiary theme color

% symbols
%   itemize labels (the struts were added to correct inter-item spacing (works for single line items, until a solution is found for multi-line ones...)
\newcommand*{\labelitemi}{\strut\textcolor{color1}{\marvosymbol{123}}}% equivalent to \Neutral from marvosym package; alternative: \fontencoding{U}\fontfamily{ding}\selectfont\tiny\symbol{'102}
\newcommand*{\labelitemii}{\strut\textcolor{color1}{\large\bfseries-}}
\newcommand*{\labelitemiii}{\strut\textcolor{color1}{\rmfamily\textperiodcentered}}% alternative: \textasteriskcentered; the \rmfamily is required to force Latin Modern fonts when using sans serif, as OMS/lmss/m/n is not defined and gets substituted by OMS/cmsy/m/n
\newcommand*{\labelitemiv}{\labelitemiii}
%   enumerate labels
\renewcommand{\theenumi}{\@arabic\c@enumi}
\renewcommand{\theenumii}{\@alph\c@enumii}
\renewcommand{\theenumiii}{\@roman\c@enumiii}
\renewcommand{\theenumiv}{\@Alph\c@enumiv}
%   other symbols
\newcommand*{\listitemsymbol}{\labelitemi~}
\newcommand*{\addresssymbol}{}
\newcommand*{\mobilesymbol}{}
\newcommand*{\phonesymbol}{}
\newcommand*{\faxsymbol}{}
\newcommand*{\emailsymbol}{}
\newcommand*{\homepagesymbol}{}

% fonts
\AtBeginDocument{\normalfont\color{color0}}

% strings for internationalisation
\newcommand*{\refname}{Publications}
\newcommand*{\enclname}{Enclosure}

% makes the footer (normally used both for the resume and the letter)
% usage: \makefooter
\newcommand*{\makefooter}{}%

% loads a style scheme
\newcommand*{\moderncvstyle}[1]{
  \RequirePackage{moderncvstyle#1}}
  
% loads a color scheme
\newcommand*{\moderncvcolor}[1]{
  \RequirePackage{moderncvcolor#1}}

% recomputes all automatic lengths
\newcommand*{\recomputelengths}{\recomputecvlengths}
\AtBeginDocument{\recomputelengths{}}

% creates a length if not yet defined
\newcommand*{\@initializelength}[1]{%
  \ifdefined#1\else\newlength{#1}\fi}


%-------------------------------------------------------------------------------
%                resume design commands definitions
%-------------------------------------------------------------------------------
% elements
\newcommand*{\extrainfo}[1]{\def\@extrainfo{#1}}
\newcommandx*{\photo}[3][1=64pt,2=0.4pt,usedefault]{\def\@photowidth{#1}\def\@photoframewidth{#2}\def\@photo{#3}}% the 1st (optional) argument is the width of the photo, the 2nd (optional) argument is the thickness of the frame around it.
\newcommand*{\quote}[1]{\def\@quote{#1}}

% fonts
\newcommand*{\namefont}{}
\newcommand*{\titlefont}{}
\newcommand*{\addressfont}{}
\newcommand*{\quotefont}{}
\newcommand*{\sectionfont}{}
\newcommand*{\subsectionfont}{}
\newcommand*{\hintfont}{}

% styles
\newcommand*{\namestyle}[1]{{\namefont#1}}
\newcommand*{\titlestyle}[1]{{\titlefont#1}}
\newcommand*{\addressstyle}[1]{{\addressfont#1}}
\newcommand*{\quotestyle}[1]{{\quotefont#1}}
\newcommand*{\sectionstyle}[1]{{\sectionfont#1}}
\newcommand*{\subsectionstyle}[1]{{\subsectionfont#1}}
\newcommand*{\hintstyle}[1]{{\hintfont#1}}

% recompute all resume lengths
\newcommand*{\recomputecvlengths}{}

% internal maketitle command to issue a new line only when required
\newif\if@firstdetailselement\@firstdetailselementtrue
\newcommand*{\makenewline}{
  \if@firstdetailselement%
    \strut% to ensure baseline alignment, e.g. with when put in the margin vs sections that also contains a \strut
  \else%
    \\\fi%
  \@firstdetailselementfalse}

% makes the resume title
% usage: \makecvtitle
\newcommand*{\makecvtitle}{}

% makes the resume footer
% usage: \makecvfooter
\newcommand*{\makecvfooter}{\makefooter}

% makes a resume section
% usage: \section{<title>}
\newcommand*{\section}[1]{}
% starred variant, which is identical but defined to allow its use (e.g. for natbib compatibility, who uses \section*{} for the bibliography header)
\RequirePackage{suffix}
\AtBeginDocument{\WithSuffix\newcommand\section*{\section}}

% makes a resume subsection
% usage: \subsection{title}
\newcommand*{\subsection}[1]{}
\AtBeginDocument{\WithSuffix\newcommand\subsection*{\subsection}}

% makes a resume line with a header and a corresponding text
% usage: \cvitem[spacing]{header}{text}
\newcommand*{\cvitem}[3][.25em]{}

% makes a resume line 2 headers and their corresponding text
% usage: \cvdoubleitem[spacing]{header1}{text1}{header2}{text2}
\newcommand*{\cvdoubleitem}[5][.25em]{}

% makes a resume line with a list item
% usage: \cvlistitem[label]{item}
\newcommand*{\cvlistitem}[2][\listitemsymbol]{}

% makes a resume line with 2 list items
% usage: \cvlistdoubleitem[label]{item1}{item2}
\newcommand*{\cvlistdoubleitem}[3][\listitemsymbol]{}

% makes a typical resume job / education entry
% usage: \cventry[spacing]{years}{degree/job title}{institution/employer}{localization}{optionnal: grade/...}{optional: comment/job description}
\newcommand*{\cventry}[7][.25em]{}

% makes a resume entry with a proficiency comment
% usage: \cvitemwithcomment[spacing]{header}{text}{comment}
\newcommand*{\cvitemwithcomment}[4][.25em]{}

% makes a generic hyperlink
% usage: \link[optional text]{link}
\newcommand*{\link}[2][]{%
  \ifthenelse{\equal{#1}{}}%
    {\href{#2}{#2}}%
    {\href{#2}{#1}}}

% makes a http hyperlink
% usage: \httplink[optional text]{link}
\newcommand*{\httplink}[2][]{%
  \ifthenelse{\equal{#1}{}}%
    {\href{http://#2}{#2}}%
    {\href{http://#2}{#1}}}

% makes an email hyperlink
% usage: \emaillink[optional text]{link}
\newcommand*{\emaillink}[2][]{%
  \ifthenelse{\equal{#1}{}}%
    {\href{mailto:#2}{#2}}%
    {\href{mailto:#2}{#1}}}

% thebibliography environment, for use with BibTeX and possibly multibib
\newlength{\bibindent}
\setlength{\bibindent}{1.5em}
% bibliography item label
\newcommand*{\bibliographyitemlabel}{}% use \@biblabel{\arabic{enumiv}} for BibTeX labels
%\newif\if@multibibfirstbib\@multibibfirstbibfalse
% bibliography head (section, etc}, depending on whether multibib is used
\newcommand*{\bibliographyhead}[1]{\section{#1}}
\AtEndPreamble{\@ifpackageloaded{multibib}{\renewcommand*{\bibliographyhead}[1]{\subsection{#1}}}{}}
% thebibliography environment definition
\newenvironment{thebibliography}[1]{}{}
\newcommand*{\newblock}{\hskip .11em\@plus.33em\@minus.07em}
\let\@openbib@code\@empty

% itemize, enumerate and description environment
\setlength{\leftmargini}   {1em}
\leftmargin\leftmargini
\setlength{\leftmarginii}  {\leftmargini}
\setlength{\leftmarginiii} {\leftmargini}
\setlength{\leftmarginiv}  {\leftmargini}
\setlength{\leftmarginv}   {\leftmargini}
\setlength{\leftmarginvi}  {\leftmargini}
\setlength{\labelsep}      {.5em}% this is the distance between the label and the body, but it pushes the label to the left rather than pushing the body to the right (to do the latter, modify \leftmargin(i)
\setlength{\labelwidth}    {\leftmargini}% unfortunately, \labelwidth is not defined by item level (i.e. no \labeliwidth, \labeliiwidth, etc)
\addtolength{\labelwidth}  {-\labelsep}
\@beginparpenalty -\@lowpenalty
\@endparpenalty   -\@lowpenalty
\@itempenalty     -\@lowpenalty
\newcommand\labelenumi{\theenumi.}
\newcommand\labelenumii{(\theenumii)}
\newcommand\labelenumiii{\theenumiii.}
\newcommand\labelenumiv{\theenumiv.}
\renewcommand\p@enumii{\theenumi}
\renewcommand\p@enumiii{\p@enumii(\theenumii)}
\renewcommand\p@enumiv{\p@enumiii\theenumiii}
% description label
\newcommand*\descriptionlabel[1]{\hspace\labelsep\normalfont\bfseries#1}
% hooks to adjust spacing (idea by Jakob Schiøtz; see http://dcwww.camd.dtu.dk/~schiotz/comp/LatexTips/tweaklist.sty)
\RequirePackage{tweaklist}% distributed with moderncv, not found on ctan and slightly modified
\renewcommand*{\itemhook}{
  \setlength{\topsep}{0pt}%
  \setlength{\parsep}{0pt}%
  \setlength{\parskip}{0pt}%
  \setlength{\itemsep}{0pt}}
\renewcommand*{\enumhook}{\itemhook{}}
\renewcommand*{\deschook}{\itemhook{}}

% classical \today definition
\def\today{\ifcase\month\or
  January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or December\fi
  \space\number\day, \number\year}

%\newcommand{\widthofautobox}[1]{%
%  \widthof{\begin{tabular}{@{}l@{}}#1\end{tabular}}}

%\newcommand{\autobox}[2][b]{%
%  \parbox[#1]{\widthofautobox{#2}}{#2}}


%-------------------------------------------------------------------------------
%                letter design commands definitions
%-------------------------------------------------------------------------------
% elements
\newcommand*{\recipient}[2]{\def\@recipientname{#1}\def\@recipientaddress{#2}}
\renewcommand*{\date}[1]{\def\@date{#1}}\date{\today}
\newcommand*{\opening}[1]{\def\@opening{#1}}
\newcommand*{\closing}[1]{\def\@closing{#1}}
\newcommand*{\enclosure}[2][]{%
  % if an optional argument is provided, use it to redefine \enclname
  \ifthenelse{\equal{#1}{}}{}{\renewcommand*{\enclname}{#1}}%
  \def\@enclosure{#2}}

% recompute all letter lengths
\newcommand*{\recomputeletterlengths}{}

% makes the letter title
% usage: \makelettertitle
\newcommand*{\makelettertitle}{}

% makes the letter footer
% usage: \makeletterfooter
\newcommand*{\makeletterfooter}{\makefooter}

% makes the letter closing
% usage: \makeletterclosing
\newcommand*{\makeletterclosing}{}


\endinput


%% end of file `moderncv.cls'.
"""
    
    def create(self, path:Path=None):
        path = Path.cwd() if path is None else Path(path)

        with open(path / self._filename, 'w') as f:
            f.write(self._text)



def main():
    print(__all__)


if __name__ == '__main__':
    main()