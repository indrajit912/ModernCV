# Class for Indrajit's details
# Author: Indrajit
# Created On: Mar 15, 2024

class Indrajit:
    first_name = "Indrajit"
    family_name = "Ghosh"
    address = ["8th Mile Mysore Road, RVCE Post", "Bangalore 560 059, India"]
    mobile = None
    email = "rs_math1902@isibang.ac.in"
    homepage = "https://indrajitghosh.onrender.com/"

    education = [
        {
            'years': "Jul 2019 -- Present",
            'degree': "Philosophiae Doctorate in Mathematics",
            'institute': "Stat-Math Unit, Indian Statistical Institute Bangalore",
            'location': "Bangalore, India",
            'grade': "Advisor: Dr. Soumyashant Nayak",
            'description': "Thesis: On Algebraic Aspects and Functoriality of the Set of Unbounded Operators Affiliated with a von Neumann Algebra",
        },
        {
            'years': "2016 -- 2018",
            'degree': "Master of Science in Pure Mathematics",
            'institute': "Department of Pure Mathematics, University of Calcutta",
            'location': "Kolkata, India"
        },
        {
            'years': "2013 -- 2016",
            'degree': "Bachelor of Science in Mathematics (Hons.)",
            'institute': "Barasat Government College",
            'location': "Barasat, India"
        },
    ]

    research_interest = r"Operator Algebras: von Neumann Algebras, Type $II_1$ Factors, $C^*$-Algebras; Functional Analysis"
    
    publication = [
        {
            'authors': ["Me", "S. Nayak"],
            'title': "Affiliated operators for monotone $\sigma$-complete $C^*$-algebras",
            'status': "pre-print, under preparation, 2025 ", # For example 'pre-print, 2023'
            'links': []
        },
        {
            'authors': ["Me", "S. Nayak"],
            'title': "Algebraic aspects and functoriality of the set of affiliated operators",
            'status': "International Mathematics Research Notices, Volume 2024, Issue 21, Nov 2024, Pages 13525-13562", # For example 'pre-print, 2023'
            'links': [
                {'link': "https://doi.org/10.1093/imrn/rnae203", 'link-text': "DOI"},
                {'link': "https://arxiv.org/abs/2311.16170", 'link-text': "arXiv:2311.16170"}
            ]
        },
    ]
    
    fellowship_achievement = [
        {
            'year': '2019',
            'description': r"Selected for \textbf{NBHM JRF} fellowship, \emph{National Board for Higher Mathematics}, Dept. Of Atomic Energy, Govt. of India, 2019, Ref No. \texttt{0203/11/2019-R\&D-II/9261}."
        },
        {
            'year': '2019',
            'description': r"Selected as JRF at Indian Statistical Institute, 2019"
        },
        {
            'year': '2019',
            'description': r"Selected as JRF at IIT Madras, 2019",
        },
        {
            'year': '2019',
            'description': r"Selected as JRF at IISER Bhopal, 2019"
        },
        {
            'year': '2019',
            'description': r"Qualified \textbf{GATE} in Mathematics(MA), 2019"
        },
        {
            'year': '2018',
            'description': r"Qualified Joint \textbf{CSIR-UGC NET JRF} fellowship, Dec 2018"
        }
    ]

    contri_talks = [
        {
            'title': "Young Mathematicians in Operator Algebras",
            'date': "Mar 24, 2025",
            'institute': "Indian Statistical Institute Delhi",
            'country': "Delhi, India",
            'venue': "Stat-Math Unit, ISI",
            'website': {},
            'abstract': {}
        },
        {
            'title': "Conference on Operator Algebra and Related Topics COART-2025",
            'date': "Feb 24 -- 28, 2025",
            'institute': "Indian Institute of Technology Bombay",
            'country': "Bombay, India",
            'venue': "Math Department, IIT",
            'website': {'url': "https://sites.google.com/view/coart-2025iitb/home", 'url_text': 'Click here'},
            'abstract': {}
        },
        {
            'title': "PDF-RS Annual Symposium 2025",
            'date': "Jan 29, 2025",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'venue': "Platinum Jubilee Auditoriam, ISI",
            'website': {'url': "https://indrajitghosh.onrender.com/misc/isi_symposium_25", 'url_text': 'Click here'},
            'abstract': {'url':"https://indrajitghosh.onrender.com/misc/isi_symposium_25\#indrajit-abs", 'url_text': 'Click here'}
        },
        {
            'title': "Workshop on Completely Positive Maps",
            'date': "Jan 15 -- Jun 04, 2024",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'venue': "Stat-Math Unit, ISI",
            'website': {'url': "https://indrajitghosh.onrender.com/teaching/isibc/intro_to_cp_even_2024.html", 'url_text': 'Click here'},
            'abstract': {}
        },
        {
            'title': "Young Mathematicians in Operator Algebras",
            'date': "Feb 27, 2024",
            'institute': "Indian Statistical Institute Delhi",
            'country': "Delhi, India",
            'venue': "Stat-Math Unit, ISI",
            'website': {'url': "https://sites.google.com/view/ymoa/home", 'url_text': ''},
            'abstract': {'url':"https://sites.google.com/view/ymoa/talks?authuser=0", 'url_text': "Click here"}
        },
        {
            'title': "International Conference on Spectral and Approximation Theory",
            'date': "Nov 29, 2023",
            'institute': "Cochin University of Science and Technology",
            'country': "Kerala, India",
            'venue': "Department of Mathematics, CUSAT",
            'website': {'url': "https://sites.google.com/view/icsat-23/", 'url_text': ''},
            'abstract': {'url':"https://sites.google.com/view/icsat-23/abstracts?authuser=0", 'url_text': "Click here"}
        },
    ]

    teaching_experience = [
        {
            'role': "Teaching Assistant",
            'year': "Jan 01, 2025 -- Present",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'course': "Optimization (B. Math III)",
            'instructor': "Soumyashant Nayak",
            'webpage': "https://indrajitghosh.onrender.com/teaching/isibc/optimization_even2025.html"
        },
        {
            'role': "Teaching Assistant",
            'year': "Jan 2024 -- Apr 2024",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'course': "A Course in Harmonic Analysis (B. Math III)",
            'instructor': "Soumyashant Nayak",
            'webpage': "https://indrajitghosh.onrender.com/teaching/isibc/course_harmonic_even2024.html"
        },
        {
            'role': "Teaching Assistant",
            'year': "Aug 01 -- Nov 25, 2023",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'course': "Analysis of Several Variables (B. Math II)",
            'instructor': "Mathew Joseph",
            'webpage': "https://indrajitghosh.onrender.com/teaching/isibc/anal_several_vars_odd_2023.html"
        },
        {
            'role': "Teaching Assistant",
            'year': "Aug 2022 -- Nov 2022",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'course': "Complex Analysis I (B. Math III)",
            'instructor': "Mathew Joseph",
            'webpage': "https://indrajitghosh.onrender.com/teaching/isibc/comp_anal_odd_sem_2022.html"
        },
        {
            'role': "Teaching Assistant",
            'year': "Jan 2022 -- Apr 2022",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'course': "Functional Analysis (M. Math I)",
            'instructor': "Soumyashant Nayak",
            'webpage': "https://indrajitghosh.onrender.com/teaching/isibc/func_anal_even_sem_2021.html"
        },
        {
            'role': "Teaching Assistant",
            'year': "Sep 21 -- Dec 23, 2021",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'course': " Optimization (B. Math II)",
            'instructor': "Soumyashant Nayak",
            'webpage': "https://indrajitghosh.onrender.com/teaching/isibc/optimization_odd_sem_2021.html"
        },
    ]


    conferences = [
        {
            'title': "Noncommutative Mathematics and Applications (NCMA)",
            'date': "Oct 24 -- 26, 2024",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'venue': "Stat-Math Unit, ISI",
            'website': {'url': "https://www.isibang.ac.in/\\textasciitilde jay/NC/NC.html", 'url_text': ''}
        },
        {
            'title': "Young Mathematicians in Operator Algebras",
            'date': "Feb 26 -- Mar 02, 2024",
            'institute': "Indian Statistical Institute Delhi",
            'country': "Delhi, India",
            'venue': "Stat-Math Unit, ISI",
            'website': {'url': "https://sites.google.com/view/ymoa/home", 'url_text': ''}
        },
        {
            'title': "International Conference on Spectral and Approximation Theory",
            'date': "Nov 27 -- 30, 2023",
            'institute': "Cochin University of Science and Technology",
            'country': "Kerala, India",
            'venue': "Department of Mathematics, CUSAT",
            'website': {'url': "https://sites.google.com/view/icsat-23/", 'url_text': ''},
        },
        {
            'title': "Conference on Functional Analysis and Related Topics-2023",
            'date': "Feb 21 -- 25, 2023",
            'institute': "Indian Institute of Technology Bombay, India",
            'country': "Bombay, India",
            'venue': "Victor Menezes Convention Centre (VMCC), IIT Bombay",
            'website': {'url': "https://sites.google.com/view/cfart-2023-iitb/", 'url_text': ''}
        },
        {
            'title': "Tomita-Takesaki Modular Theory",
            'date': "Jan 18 -- Apr 26, 2023",
            'institute': "Indian Statistical Institute, Bangalore, India",
            'country': "Bangalore, India",
            'venue': "Stat-Math Unit, ISI",
            'website': {'url': "https://www.isibang.ac.in/~soumyashant/teaching/MODULAR_THEORY-EVEN2023/CourseWebpage.html", 'url_text': 'Click here'},
        },
        {
            'title': "Ergodic Theory and Dynamical Systems",
            'date': "Dec 05 -- 16, 2022",
            'institute': "International Centre for Theoretical Sciences",
            'country': "Bangalore, India",
            'venue': "Ramanujan Lecture Hall (ICTS) and Online",
            'website': {'url': "https://www.icts.res.in/program/ETDS2022", 'url_text': ''},
        },
        {
            'title': "Baby Steps Beyond the Horizon",
            'date': "Aug 29 - Sep 02, 2022",
            'institute': "Institute of Mathematics Polish Academy of Sciences",
            'country': "Warszawa, Poland",
            'venue': "Online",
            'website': {'url': "https://www.impan.pl/en/activities/banach-center/conferences/22-babysteps", 'url_text': ''},
        },
        {
            'title': "A Conference on Ergodic Theory and von-Neumann Algebra",
            'date': "Aug 04 -- 06, 2022",
            'institute': "National Institute of Science Education and Research",
            'country': "Odisha, India",
            'venue': "Online",
            'website': {'url': "https://www.niser.ac.in/etvna", 'url_text': ''},
        },
        {
            'title': "IFCAM - Mathematical Aspects of Quantum Mechanics",
            'date': "Jun 01 -- 12, 2022",
            'institute': "Indian Institute of Science Bangalore",
            'country': "Bangalore, India",
            'venue': "Math Dept., IISc",
            'website': {'url': "https://ifcam.sciencesconf.org/", 'url_text': ''},
        },
        {
            'title': "Quantum Probability and Infinite Dimensional Analysis",
            'date': "Jan 17 -- 20, 2022",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'venue': "Stat-Math Unit, ISI",
            'website': {'url': "https://www.isibang.ac.in/~statmath/conferences/QPIDA-2022.html", 'url_text': ''},
        }
    ]


    references = [
        {
            'name': "Prof. Soumyashant Nayak",
            'email': "soumyashant@isibang.ac.com",
            'designation': "Assistant Professor",
            'address': "Office A-14, Stat-Math Unit, Indian Statistical Institute Bangalore"
        },
        {
            'name': "Prof. B.V. Rajarama Bhat",
            'email': "bvrajaramabhat@gmail.com",
            'designation': "Professor",
            'address': "Stat-Math Unit, Indian Statistical Institute Bangalore"
        },
        {
            'name': "Prof. Jaydeb Sarkar",
            'email': "jaydeb@gmail.com",
            'designation': "Professor",
            'address': "Stat-Math Unit, Indian Statistical Institute Bangalore"
        }
    ]