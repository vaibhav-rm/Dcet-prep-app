class Question:
    def __init__(self, question, options, correct_answer, subject):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.subject = subject

questions_list = [
    Question(
        "The project ______ relieves a project team from most regular work such as planning, tracking, and reporting responsibility?",
        ["Manager", "CEO", "Administration", "Leader"],
        "Administration",
        "Project Management Skills"
    ),
    Question(
        "The use of authority to channelize the activities of the project on desired lines is referred to as ______.",
        ["Project direction", "Project coordination", "Project communication", "Project execution"],
        "Project direction",
        "Project Management Skills"
    ),
    Question(
        "______ illustrates total project work into divisions of major work packages.",
        ["PERT", "CPM", "WBS", "PEP"],
        "WBS",
        "Project Management Skills"
    ),
    Question(
        "______ is a condition wherein a construction or manufacturing project does not complete well within its prescribed time schedule.",
        ["Time analysis", "Time estimate", "Time overrun", "Cost overrun"],
        "Time overrun",
        "Project Management Skills"
    ),
    Question(
        "A project ______ creates damages or adverse effects to either project activities or project deliverables.",
        ["Failure", "Undertaken", "Risk", "Analysis"],
        "Risk",
        "Project Management Skills"
    ),
    Question(
        "Identify the correct risk analysis which has typically one variable changed at a time.",
        ["Sensitivity Analysis", "Scenario Analysis", "Best and Worst Case Analysis", "Simulation Analysis"],
        "Sensitivity Analysis",
        "Project Management Skills"
    ),
    Question(
        "Risk usually ______ as the project progresses.",
        ["Increases", "Reduces", "Remains same", "Becomes negligible"],
        "Reduces",
        "Project Management Skills"
    ),
    Question(
        "In 'SMART', the letter R stands for ______.",
        ["Realistic", "Reliable", "Reasonable", "Relation"],
        "Realistic",
        "Project Management Skills"
    ),
    Question(
        "______ is a step-by-step process of collecting, recording, and organizing information about project results.",
        ["Project planning", "Project evaluation", "Project scheduling", "Project monitoring"],
        "Project evaluation",
        "Project Management Skills"
    ),
    Question(
        "In a square matrix, if the elements above the principal diagonal are zero, then it is called",
        ["Identity matrix", "Lower triangular matrix", "Upper triangular matrix", "Diagonal matrix"],
        "Lower triangular matrix",
        "Mathematics"
    ),
    Question(
        "Repair of a dam in case of damage due to natural calamities is an example of?",
        ["Normal project", "Crash project", "Risky project", "Disaster project"],
        "Disaster project",
        "Project Management Skills"
    ),
    Question(
        "A project performed due to the effect of natural calamities is known as?",
        ["Normal project", "Crash project", "Risky project", "Disaster project"],
        "Disaster project",
        "Project Management Skills"
    ),
    Question(
        "What refers to a detailed description of the expected outcome of a project?",
        ["Project scope", "Project operation", "Project objective", "Project process"],
        "Project objective",
        "Project Management Skills"
    ),
    Question(
        "In flowcharts, circles are used as connector symbols to show the continuation of the flow across multiple pages or through a complex chart.",
        ["Rectangle", "Diamond", "Oval", "Circle"],
        "Circle",
        "IT Skills"
    ),
    Question(
        "Which symbol is used to represent start or stop in a flowchart?",
        ["Rectangle", "Diamond", "Oval", "Circle"],
        "Oval",
        "IT Skills"
    ),
    Question(
        "What does CSS stand for?",
        ["Colourful Style Sheet", "Cascading Style Sheet", "Creative Style Sheet", "Computer Style Sheet"],
        "Cascading Style Sheet",
        "IT Skills"
    ),
    Question(
        "Which of the following is not a web browser?",
        ["Google Chrome", "Netscape Navigator", "Safari", "Apache"],
        "Apache",
        "IT Skills"
    ),
    Question(
        "What is the correct syntax to change the background colour with CSS?",
        ["background-color = 'purple';", "background – color : purple;", "background – color = orange", "change-background-color : purple"],
        "background – color : purple;",
        "IT Skills"
    ),
    Question(
        "Which HTML tag gives a scrolling effect to a given text?",
        ["<div>", "<scroll>", "<marquee>", "<effect>"],
        "<marquee>",
        "IT Skills"
    ),
    Question(
        "ERP package will handle ______ business functionality / functionalities.",
        ["One", "Two", "Three", "Multiple"],
        "Multiple",
        "IT Skills"
    ),
    Question(
        "Which one is a type of organizational structure?",
        ["Responsibility structure", "Behavioural structure", "Functional structure", "Relational structure"],
        "Functional structure",
        "Project Management Skills"
    ),
    Question(
        "______ describes how an actor uses a system to accomplish a particular goal for describing the activities.",
        ["Process case", "Work case", "Use case", "Sub process"],
        "Use case",
        "IT Skills"
    ),
    Question(
        "Which of the following is not a characteristic of First-generation ERP system?",
        ["They were based on mainframe computer", "They focused on accounting and finance", "They used centralized database", "They supported real-time data processing"],
        "They supported real-time data processing",
        "IT Skills"
    ),
    Question(
        "Which cloud service model enables users to develop, run, manage applications without worrying about underlying infrastructure?",
        ["IAAS", "PAAS", "SAAS", "NAAS"],
        "PAAS",
        "IT Skills"
    ),
    Question(
        "Which of the following is not a Google application?",
        ["Google Docs", "Google Slides", "Google Sheets", "Google Word"],
        "Google Word",
        "IT Skills"
    ),
    Question(
        "IoT is a ______.",
        ["Network of sensors", "Network of objects in a ring structure", "Network of virtual objects", "Network of physical objects embedded with sensors"],
        "Network of physical objects embedded with sensors",
        "IT Skills"
    ),
    Question(
        "______ is a file storage and synchronization service developed by Google which provides complete office tools with cloud storage.",
        ["Google Colab", "Google Drive", "Google Meet", "AWS Cloud"],
        "Google Drive",
        "IT Skills"
    ),
    Question(
        "Which of the following is not a security issue in a personal computer?",
        ["Ransomware Attack", "Data Breach", "Code Injection", "IoT"],
        "IoT",
        "IT Skills"
    ),
    Question(
        "Which of the following is not a firewall?",
        ["Packet filtering", "Stateful inspection", "Panda", "Circuit Level Gateway"],
        "Panda",
        "IT Skills"
    ),
    Question(
        "'S' in HTTPS stands for ______.",
        ["Safe", "Secure", "System", "Server"],
        "Secure",
        "IT Skills"
    ),
    Question(
        "Which Of The Following is a programing language?",
        ["Microsoft Word", "Adobe Photoshop", "Python", "Chrom"],
        "Python",
        "IT Skills"
    ),
    Question(
        "______ is not a data collection tool",
        ["Word", "Focus Group Dicussion ", "Survey", "Quetionnarlo"],
        "Word",
        "Statistics & Analytics"
    ),
    Question(
        "To Find third quartile in EXCEL,we use ___________ Formula",
        ["=QUARTER(3,RANGE)", "=QUARTILE(3,RANGE)","=QUARTER(RANGE,3)","=QUARTILE(RANGE,3)"],
        "=QUARTILE(RANGE,3)",
        "Statistics & Analytics"
    ),
    Question(
        "The Percentile devides a series into _________ equal parts",
        ["Fifty", "twenty","ten","hundred"],
        "hundred",
        "Statistics & Analytics"
    ),
    Question(
        "The EXCEL formula for 'MEAN' is",
        ["=MEDIAN(array of numbers)","=AVERAGE(array of numbers)","=MEAN(array of numbers)","=MODE(array of numbers"],
        "=AVERAGE(array of numbers)",
        "Statistics & Analytics"
    ),
    Question(
        "str is a ",
        ["Text Type", "Numeric Type","Binary Type","Sequence Type"],
        "Text Type",
        "IT Skills"
    ),
    Question(
        "DoS is abbreviated as _______",
        ["Denial Of Service", "Distribution of server","distribution of service","Denial of server"],
        "Denial Of Service",
        "IT Skills"
    ),
    Question(
        "In python,_____ is used to end physical line or ignore the comments",
        ["**", "#","&","\\"],
        "#",
        "IT Skills"
    ),
    Question(
        "Which of the following is not crime?",
        ["cryptography", "Denial of service","Man-in-middle attack","phising"],
        "cryptography",
        "IT Skills"
    ),
    Question(
        "The earliest method used for planning project was ",
        ["CPM", "PERT","Bar Chart","Milestone Chart"],
        "Bar Chart",
        "Project Management Skills"
    ),
    Question(
        "The binary equivalent of decimal number 9 is?",
        ["1001", "1000","1100","1010"],
        "1001",
        "Statistics & Analytics"
    ),
    Question(
        "The type of project which requires minimum ammount of capital is",
        ["crash project", "normal project","disaster project","consultant project"],
        "normal project",
        "Project Management Skills"
    ),
    Question(
        "Cell is an ______ device",
        ["electro-mechanical", "electro-chemical","electro-magnetic","electro-dynamic"],
        "electro-chemical",
        "Fundamentals Of Electrical and Electronic Engineering"
    ),
        Question(
        "What is a project?",
        ["A temporary endeavor with a defined beginnning and end", "An ongoing activity with no specific end date","electro-magnetic","electro-dynamic"],
        "A temporary endeavor with a defined beginnning and end",
        "Project Management Skills"
    ),
    Question(
        "What is a project?",
        ["A temporary endeavor with a defined beginnning and end", "An ongoing activity with no specific end date","electro-magnetic","electro-dynamic"],
        "A temporary endeavor with a defined beginnning and end",
        "Project Management Skills"
    )
    
]
