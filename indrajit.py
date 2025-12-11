# Class for Indrajit's details
# Author: Indrajit
# Created On: Mar 15, 2024

class Indrajit:
    first_name = "Indrajit"
    family_name = "Ghosh"
    address = ["Dept. of Mathematics, IIT Madras", "Chennai 600 036, India"]
    mobile = None
    email = "indrajitghosh2014@gmail.com"
    homepage = "https://indrajitghosh.onrender.com/"

    employment = [
        {
            'years': "Nov 2025 -- Present",
            'position': "Postdoctoral Researcher",
            'institute': "Indian Institute of Technology Madras",
            'location': "Chennai, India"
        }
    ]

    education = [
        {
            'years': "Jul 2019 -- Oct 2025",
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

    # Invited Talks
    invited_talks = [
        {
            'title': "Young Mathematicians in Operator Algebras",
            'date': "Mar 24 -- 28, 2025",
            'institute': "Indian Statistical Institute Delhi",
            'country': "Delhi, India"
        },
    ]

    ##########################################################
    """
    Contributed Talk
    Sample entry:
    {
        'title': "PDF-RS Annual Symposium 2025",
        'date': "Jan 29, 2025",
        'institute': "Indian Statistical Institute Bangalore",
        'country': "Bangalore, India",
        'venue': "Platinum Jubilee Auditoriam, ISI",
        'website': {'url': "https://indrajitghosh.onrender.com/misc/isi_symposium_25", 'url_text': 'Click here'},
        'abstract': {'url':"https://indrajitghosh.onrender.com/misc/isi_symposium_25", 'url_text': 'Click here'}
    }
    """
    ##########################################################

    contri_talks = [
        {
            'title': "Young Mathematicians in \(C^*\)-Algebras (YMC*A-2025)",
            'date': "Jul 21 -- 25, 2025",
            'institute': "University of Southern Denmark",
            'country': "Odense, Denmark"
        },
        {
            'title': "Conference on Operator Algebra and Related Topics (COART-2025)",
            'date': "Feb 24 -- 28, 2025",
            'institute': "Indian Institute of Technology Bombay",
            'country': "Bombay, India"
        },
        {
            'title': "PDF-RS Annual Symposium 2025",
            'date': "Jan 29 -- 31, 2025",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
        },
        {
            'title': "Workshop on Completely Positive Maps",
            'date': "Jan 15 -- Jun 04, 2024",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India"
        },
        {
            'title': "Young Mathematicians in Operator Algebras",
            'date': "Feb 26 -- Mar 02, 2024",
            'institute': "Indian Statistical Institute Delhi",
            'country': "Delhi, India",
        },
        {
            'title': "International Conference on Spectral and Approximation Theory",
            'date': "Nov 27 -- 30, 2023",
            'institute': "Cochin University of Science and Technology",
            'country': "Kerala, India"
        },
    ]

    
    #################################################################
    """
    Conferences
     Sample entry:
      {
          'title': "Noncommutative Mathematics and Applications (NCMA)",
          'date': "Oct 24 -- 26, 2024",
          'institute': "Indian Statistical Institute Bangalore",
          'country': "Bangalore, India",
          'venue': "Stat-Math Unit, ISI",
          'website': {'url': "https://www.isibang.ac.in/~statmath/conferences/QPIDA-2022.html", 'url_text': ''},
      }
    """
    #################################################################
    conferences = [
        {
            'title': "Noncommutative Mathematics and Applications (NCMA)",
            'date': "Oct 24 -- 26, 2024",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India"
        },
        {
            'title': "Conference on Functional Analysis and Related Topics-2023",
            'date': "Feb 21 -- 25, 2023",
            'institute': "Indian Institute of Technology Bombay, India",
            'country': "Bombay, India"
        },
        {
            'title': "Ergodic Theory and Dynamical Systems",
            'date': "Dec 05 -- 16, 2022",
            'institute': "International Centre for Theoretical Sciences",
            'country': "Bangalore, India"
        },
        {
            'title': "Baby Steps Beyond the Horizon (Online)",
            'date': "Aug 29 - Sep 02, 2022",
            'institute': "Institute of Mathematics Polish Academy of Sciences",
            'country': "Warszawa, Poland"
        },
        {
            'title': "A Conference on Ergodic Theory and von-Neumann Algebra (Online)",
            'date': "Aug 04 -- 06, 2022",
            'institute': "National Institute of Science Education and Research",
            'country': "Odisha, India"
        },
        {
            'title': "IFCAM - Mathematical Aspects of Quantum Mechanics",
            'date': "Jun 01 -- 12, 2022",
            'institute': "Indian Institute of Science Bangalore",
            'country': "Bangalore, India"
        },
        {
            'title': "Quantum Probability and Infinite Dimensional Analysis",
            'date': "Jan 17 -- 20, 2022",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
        }
    ]

    ###################################################################
    """
    Teaching Experience
    Sample Entry:
    {
        'role': "Teaching Assistant",
        'year': "Sep 21 -- Dec 23, 2021",
        'institute': "Indian Statistical Institute Bangalore",
        'country': "Bangalore, India",
        'course': " Optimization (B. Math II)",
        'instructor': "Soumyashant Nayak",
        'webpage': "https://indrajitghosh.onrender.com/teaching/isibc/optimization_odd_sem_2021.html"
    },
    """
    ###################################################################

    teaching_experience = [
        {
            'role': "Teaching Assistant",
            'year': "Jan 01 -- Apr 15, 2025",
            'institute': "Indian Statistical Institute Bangalore",
            'country': "Bangalore, India",
            'course': "Optimization (B. Math III)",
            'instructor': "Soumyashant Nayak",
            'webpage': "https://indrajitghosh.onrender.com/teaching/isibc/optimization_even2025.html"
        },
        {
            'role': "Teaching Assistant",
            'year': "Jan -- Apr 2024",
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

    #################################################################
    """
    References:
    {
        'name': "Prof. Soumyashant Nayak",
        'email': "soumyashant@isibang.ac.com",
        'designation': "Assistant Professor",
        'address': "Office A-14, Stat-Math Unit, Indian Statistical Institute Bangalore"
    },
    """
    #################################################################
    references = []
