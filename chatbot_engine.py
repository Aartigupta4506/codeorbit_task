"""
CodeOrbit Tech - AI Internship
Task 1: Rule-Based Chatbot

Improved Rule-Based Chatbot Engine

This chatbot uses:
- Predefined keywords
- Conditional statements
- If/elif rules
- Predefined responses
- Basic date and time functionality

No external API or Machine Learning model is used.
"""

from datetime import datetime


class RuleBasedChatbot:
    """A simple rule-based chatbot for CodeOrbit Tech Task 1."""

    def __init__(self):
        """Initialize the chatbot."""
        self.bot_name = "CodeOrbit Assistant"

    def get_response(self, user_input):
        """
        Process user input and return a predefined response.
        """

        # Convert input to string, lowercase and remove extra spaces.
        message = str(user_input).lower().strip()

        # ==========================================================
        # 1. EMPTY INPUT
        # ==========================================================
        if not message:
            return (
                "Please enter a message so I can help you. 😊"
            )

        # ==========================================================
        # 2. GREETINGS
        # ==========================================================
        if message in [
            "hello",
            "hi",
            "hey",
            "hii",
            "hiii",
            "hello there",
            "hey there",
            "good morning",
            "good afternoon",
            "good evening"
        ]:
            return (
                "Hello! 👋 I am CodeOrbit Assistant. "
                "It's great to chat with you! "
                "How can I help you today?"
            )

        # ==========================================================
        # 3. HOW ARE YOU
        # ==========================================================
        elif (
            "how are you" in message
            or "how r u" in message
            or "how are u" in message
        ):
            return (
                "I'm doing great! 😊 Thanks for asking. "
                "I'm ready to answer your questions."
            )

        # ==========================================================
        # 4. NICE TO MEET YOU
        # ==========================================================
        elif (
            "nice to meet you" in message
            or "glad to meet you" in message
        ):
            return (
                "Nice to meet you too! 😊 "
                "I'm happy to chat with you."
            )

        # ==========================================================
        # 5. BOT NAME / IDENTITY
        # ==========================================================
        elif (
            "your name" in message
            or "who are you" in message
            or "what are you" in message
            or "tell me about yourself" in message
        ):
            return (
                f"My name is {self.bot_name}. 🤖 "
                "I am a rule-based chatbot created for "
                "CodeOrbit Tech AI Internship Task 1."
            )

        # ==========================================================
        # 6. WHO CREATED YOU
        # ==========================================================
        elif (
            "who created you" in message
            or "who made you" in message
            or "who developed you" in message
        ):
            return (
                "I was developed as a Rule-Based Chatbot project "
                "for the CodeOrbit Tech Artificial Intelligence "
                "Internship."
            )

        # ==========================================================
        # 7. ARE YOU HUMAN
        # ==========================================================
        elif (
            "are you human" in message
            or "are you a human" in message
        ):
            return (
                "No. 🤖 I am a computer program designed to "
                "respond using predefined rules and keywords."
            )

        # ==========================================================
        # 8. ARE YOU AI
        # ==========================================================
        elif (
            "are you ai" in message
            or "are you an ai" in message
        ):
            return (
                "I am an AI-themed rule-based chatbot. "
                "My responses are generated using predefined "
                "rules rather than Machine Learning."
            )

        # ==========================================================
        # 9. INTERNSHIP
        # ==========================================================
        elif (
            "internship" in message
            or "codeorbit internship" in message
        ):
            return (
                "This chatbot is developed for Task 1 of the "
                "CodeOrbit Tech Artificial Intelligence Internship."
            )

        # ==========================================================
        # 10. TASK 1
        # ==========================================================
        elif (
            "task 1" in message
            or "task one" in message
            or "first task" in message
        ):
            return (
                "Task 1 is a Rule-Based Chatbot. 🤖 "
                "It uses predefined keywords, conditions and "
                "if-else rules to generate responses."
            )

        # ==========================================================
        # 11. WHAT IS AI
        # ==========================================================
        elif (
            "what is ai" in message
            or "what is artificial intelligence" in message
            or "define ai" in message
            or "define artificial intelligence" in message
        ):
            return (
                "Artificial Intelligence (AI) is a branch of "
                "computer science that enables machines to perform "
                "tasks that normally require human intelligence."
            )

        # ==========================================================
        # 12. AI APPLICATIONS
        # ==========================================================
        elif (
            "applications of ai" in message
            or "uses of ai" in message
            or "ai applications" in message
        ):
            return (
                "AI is used in healthcare, education, banking, "
                "robotics, recommendation systems, cybersecurity, "
                "transportation and virtual assistants."
            )

        # ==========================================================
        # 13. EXAMPLES OF AI
        # ==========================================================
        elif (
            "examples of ai" in message
            or "example of ai" in message
            or "ai examples" in message
        ):
            return (
                "Examples include chatbots, virtual assistants, "
                "face recognition, recommendation systems, "
                "self-driving technology and medical AI."
            )

        # ==========================================================
        # 14. BENEFITS OF AI
        # ==========================================================
        elif (
            "benefits of ai" in message
            or "advantages of ai" in message
        ):
            return (
                "AI can automate repetitive tasks, analyze large "
                "amounts of data, improve efficiency and support "
                "decision-making."
            )

        # ==========================================================
        # 15. MACHINE LEARNING
        # ==========================================================
        elif (
            "what is machine learning" in message
            or "define machine learning" in message
            or "what is ml" in message
        ):
            return (
                "Machine Learning (ML) is a branch of AI where "
                "computers learn patterns from data and use those "
                "patterns to make predictions or decisions."
            )

        # ==========================================================
        # 16. TYPES OF MACHINE LEARNING
        # ==========================================================
        elif (
            "types of machine learning" in message
            or "types of ml" in message
        ):
            return (
                "The three main types of Machine Learning are:\n\n"
                "• Supervised Learning\n"
                "• Unsupervised Learning\n"
                "• Reinforcement Learning"
            )

        # ==========================================================
        # 17. SUPERVISED LEARNING
        # ==========================================================
        elif "supervised learning" in message:
            return (
                "Supervised Learning uses labelled training data "
                "to learn the relationship between inputs and outputs. "
                "Examples include classification and regression."
            )

        # ==========================================================
        # 18. UNSUPERVISED LEARNING
        # ==========================================================
        elif "unsupervised learning" in message:
            return (
                "Unsupervised Learning works with unlabelled data "
                "and finds hidden patterns or groups. "
                "Clustering is a common example."
            )

        # ==========================================================
        # 19. REINFORCEMENT LEARNING
        # ==========================================================
        elif "reinforcement learning" in message:
            return (
                "Reinforcement Learning is a learning method where "
                "an agent learns by interacting with an environment "
                "and receiving rewards or penalties."
            )

        # ==========================================================
        # 20. DEEP LEARNING
        # ==========================================================
        elif (
            "what is deep learning" in message
            or "define deep learning" in message
        ):
            return (
                "Deep Learning is a subfield of Machine Learning "
                "that uses multi-layer artificial neural networks "
                "to learn complex patterns from data."
            )

        # ==========================================================
        # 21. NEURAL NETWORK
        # ==========================================================
        elif (
            "what is neural network" in message
            or "what are neural networks" in message
            or "neural network" in message
        ):
            return (
                "A neural network is a computing model inspired by "
                "the human brain. It consists of connected nodes "
                "called neurons that process information."
            )

        # ==========================================================
        # 22. AI VS ML
        # ==========================================================
        elif (
            "difference between ai and ml" in message
            or "ai vs ml" in message
            or "difference between ai and machine learning" in message
        ):
            return (
                "AI is the broader concept of intelligent machines. "
                "Machine Learning is a subset of AI that allows "
                "machines to learn patterns from data."
            )

        # ==========================================================
        # 23. NLP
        # ==========================================================
        elif (
            "what is nlp" in message
            or "natural language processing" in message
        ):
            return (
                "Natural Language Processing (NLP) is a field of AI "
                "that helps computers understand, process and generate "
                "human language."
            )

        # ==========================================================
        # 24. COMPUTER VISION
        # ==========================================================
        elif (
            "what is computer vision" in message
            or "computer vision" in message
        ):
            return (
                "Computer Vision is a field of AI that enables "
                "computers to analyze and understand images and videos."
            )

        # ==========================================================
        # 25. GENERATIVE AI
        # ==========================================================
        elif (
            "what is generative ai" in message
            or "generative ai" in message
        ):
            return (
                "Generative AI is a type of AI that can create new "
                "content such as text, images, audio, video or code."
            )

        # ==========================================================
        # 26. CHATBOT
        # ==========================================================
        elif (
            "what is chatbot" in message
            or "what is a chatbot" in message
            or "define chatbot" in message
        ):
            return (
                "A chatbot is a computer program designed to "
                "communicate with users through text or voice."
            )

        # ==========================================================
        # 27. RULE-BASED CHATBOT
        # ==========================================================
        elif (
            "rule based chatbot" in message
            or "what is a rule based chatbot" in message
            or "what is rule based chatbot" in message
        ):
            return (
                "A rule-based chatbot uses predefined keywords, "
                "conditions and rules to understand user input "
                "and provide predefined responses."
            )

        # ==========================================================
        # 28. HOW CHATBOT WORKS
        # ==========================================================
        elif (
            "how do you work" in message
            or "how does this work" in message
            or "how does chatbot work" in message
            or "how do chatbots work" in message
        ):
            return (
                "I work using predefined rules and keywords. "
                "I receive your message, convert it to lowercase, "
                "check predefined conditions and return the "
                "matching response."
            )

        # ==========================================================
        # 29. ADVANTAGES OF RULE-BASED CHATBOT
        # ==========================================================
        elif (
            "advantages of rule based chatbot" in message
            or "benefits of rule based chatbot" in message
        ):
            return (
                "Advantages include simple implementation, "
                "predictable responses, easy testing and no need "
                "for a large training dataset."
            )

        # ==========================================================
        # 30. LIMITATIONS OF RULE-BASED CHATBOT
        # ==========================================================
        elif (
            "limitations of rule based chatbot" in message
            or "disadvantages of rule based chatbot" in message
        ):
            return (
                "A rule-based chatbot has limited understanding. "
                "It cannot learn automatically and may fail when "
                "the user asks a question outside its predefined rules."
            )

        # ==========================================================
        # 31. PYTHON
        # ==========================================================
        elif (
            "what is python" in message
            or "define python" in message
            or "tell me about python" in message
        ):
            return (
                "Python is a high-level, interpreted programming "
                "language known for its simple and readable syntax. "
                "It is widely used in AI, ML, web development, "
                "automation and data science."
            )

        # ==========================================================
        # 32. WHY PYTHON
        # ==========================================================
        elif (
            "why python" in message
            or "why use python" in message
            or "advantages of python" in message
        ):
            return (
                "Python is popular because it has simple syntax, "
                "many libraries, a large community and applications "
                "in AI, Machine Learning, web development and automation."
            )

        # ==========================================================
        # 33. PYTHON APPLICATIONS
        # ==========================================================
        elif (
            "python applications" in message
            or "uses of python" in message
        ):
            return (
                "Python is used in AI, Machine Learning, data science, "
                "web development, automation, cybersecurity, scripting "
                "and software development."
            )

        # ==========================================================
        # 34. PROGRAMMING
        # ==========================================================
        elif (
            "what is programming" in message
            or "define programming" in message
        ):
            return (
                "Programming is the process of writing instructions "
                "that a computer can understand and execute to "
                "perform specific tasks."
            )

        # ==========================================================
        # 35. CODING
        # ==========================================================
        elif (
            "what is coding" in message
            or "define coding" in message
        ):
            return (
                "Coding is the process of writing computer programs "
                "using programming languages such as Python, Java, "
                "C++, JavaScript and others."
            )

        # ==========================================================
        # 36. C++
        # ==========================================================
        elif (
            "what is c++" in message
            or "what is cpp" in message
        ):
            return (
                "C++ is a general-purpose programming language "
                "known for performance and used in software, games, "
                "systems programming and competitive programming."
            )

        # ==========================================================
        # 37. JAVA
        # ==========================================================
        elif (
            "what is java" in message
            or "define java" in message
        ):
            return (
                "Java is a popular object-oriented programming "
                "language used for software, web, enterprise and "
                "Android-related development."
            )

        # ==========================================================
        # 38. HTML
        # ==========================================================
        elif (
            "what is html" in message
            or "define html" in message
        ):
            return (
                "HTML stands for HyperText Markup Language. "
                "It is used to structure content on web pages."
            )

        # ==========================================================
        # 39. CSS
        # ==========================================================
        elif (
            "what is css" in message
            or "define css" in message
        ):
            return (
                "CSS stands for Cascading Style Sheets. "
                "It is used to control the design, layout and "
                "appearance of web pages."
            )

        # ==========================================================
        # 40. JAVASCRIPT
        # ==========================================================
        elif (
            "what is javascript" in message
            or "define javascript" in message
        ):
            return (
                "JavaScript is a programming language commonly "
                "used to make web pages interactive and dynamic."
            )

        # ==========================================================
        # 41. STREAMLIT
        # ==========================================================
        elif (
            "what is streamlit" in message
            or "define streamlit" in message
        ):
            return (
                "Streamlit is a Python framework used to quickly "
                "create interactive web applications, especially "
                "for data science and AI projects."
            )

        # ==========================================================
        # 42. DATABASE
        # ==========================================================
        elif (
            "what is database" in message
            or "define database" in message
        ):
            return (
                "A database is an organized collection of data "
                "that can be stored, managed and retrieved efficiently."
            )

        # ==========================================================
        # 43. SQL
        # ==========================================================
        elif (
            "what is sql" in message
            or "define sql" in message
        ):
            return (
                "SQL stands for Structured Query Language. "
                "It is used to store, retrieve, update and manage "
                "data in relational databases."
            )

        # ==========================================================
        # 44. API
        # ==========================================================
        elif (
            "what is api" in message
            or "define api" in message
        ):
            return (
                "API stands for Application Programming Interface. "
                "It allows different software applications to "
                "communicate with each other."
            )

        # ==========================================================
        # 45. GIT
        # ==========================================================
        elif (
            "what is git" in message
            or "define git" in message
        ):
            return (
                "Git is a distributed version control system used "
                "to track changes in source code and collaborate "
                "on software projects."
            )

        # ==========================================================
        # 46. GITHUB
        # ==========================================================
        elif (
            "what is github" in message
            or "define github" in message
        ):
            return (
                "GitHub is a platform used to host Git repositories "
                "and collaborate on software development projects."
            )

        # ==========================================================
        # 47. PROJECT
        # ==========================================================
        elif (
            "tell me about the project" in message
            or "about the project" in message
            or "what is this project" in message
        ):
            return (
                "This project is a Rule-Based Chatbot created "
                "for CodeOrbit Tech AI Internship Task 1. "
                "It uses Python and predefined if-else rules "
                "to respond to user questions."
            )

        # ==========================================================
        # 48. TECHNOLOGIES USED
        # ==========================================================
        elif (
            "technologies used" in message
            or "technology used" in message
            or "what technology" in message
        ):
            return (
                "This project primarily uses Python for chatbot "
                "logic and Streamlit for the interactive web interface."
            )

        # ==========================================================
        # 49. CAREER IN AI
        # ==========================================================
        elif (
            "career in ai" in message
            or "ai career" in message
            or "career in artificial intelligence" in message
        ):
            return (
                "A career in AI can include roles such as AI Engineer, "
                "Machine Learning Engineer, Data Scientist, NLP Engineer, "
                "Computer Vision Engineer and AI Researcher."
            )

        # ==========================================================
        # 50. AI SKILLS
        # ==========================================================
        elif (
            "skills for ai" in message
            or "ai skills" in message
            or "skills needed for ai" in message
        ):
            return (
                "Important AI skills include Python, mathematics, "
                "Machine Learning, data handling, algorithms, "
                "problem-solving and basic knowledge of AI libraries."
            )

        # ==========================================================
        # 51. INTERVIEW PREPARATION
        # ==========================================================
        elif (
            "interview tips" in message
            or "how to prepare for interview" in message
            or "interview preparation" in message
        ):
            return (
                "For an interview, revise your fundamentals, "
                "understand your projects, practice common questions "
                "and explain your work clearly and confidently."
            )

        # ==========================================================
        # 52. STUDY TIPS
        # ==========================================================
        elif (
            "how to study" in message
            or "study tips" in message
            or "give me study tips" in message
        ):
            return (
                "Try these study tips:\n\n"
                "• Make a simple study schedule.\n"
                "• Study in focused sessions.\n"
                "• Practice instead of only reading.\n"
                "• Revise regularly.\n"
                "• Take short breaks."
            )

        # ==========================================================
        # 53. MOTIVATION
        # ==========================================================
        elif (
            "motivate me" in message
            or "i need motivation" in message
            or "give me motivation" in message
        ):
            return (
                "Keep going! 💪 Every small step you take while "
                "learning becomes part of your bigger success. "
                "Don't be afraid of mistakes—they are part of learning."
            )

        # ==========================================================
        # 54. HELP
        # ==========================================================
        elif (
            message == "help"
            or "what can you do" in message
            or "what can i ask" in message
            or "show commands" in message
        ):
            return (
                "I can answer questions about:\n\n"

                "🤖 CHATBOT\n"
                "• My name\n"
                "• Who created me\n"
                "• How I work\n"
                "• Rule-Based Chatbot\n\n"

                "🧠 AI & ML\n"
                "• Artificial Intelligence\n"
                "• AI applications\n"
                "• Machine Learning\n"
                "• Types of ML\n"
                "• Deep Learning\n"
                "• Neural Networks\n"
                "• NLP\n"
                "• Computer Vision\n"
                "• Generative AI\n\n"

                "💻 PROGRAMMING\n"
                "• Python\n"
                "• C++\n"
                "• Java\n"
                "• HTML\n"
                "• CSS\n"
                "• JavaScript\n"
                "• SQL\n"
                "• Git\n"
                "• GitHub\n"
                "• API\n"
                "• Database\n"
                "• Streamlit\n\n"

                "🎓 CAREER & STUDY\n"
                "• AI Career\n"
                "• AI Skills\n"
                "• Interview Tips\n"
                "• Study Tips\n"
                "• Motivation\n\n"

                "🎓 INTERNSHIP\n"
                "• CodeOrbit Internship\n"
                "• Task 1\n"
                "• Project Information"
            )

        # ==========================================================
        # 55. CURRENT DATE
        # ==========================================================
        elif (
            "what is today's date" in message
            or "what is the date today" in message
            or "today's date" in message
            or "today date" in message
        ):
            current_date = datetime.now().strftime("%d %B %Y")
            return f"Today's date is {current_date}. 📅"

        # ==========================================================
        # 56. CURRENT TIME
        # ==========================================================
        elif (
            "what time is it" in message
            or "current time" in message
            or "tell me the time" in message
            or "what is the time" in message
        ):
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current system time is {current_time}. ⏰"

        # ==========================================================
        # 57. COMPLIMENT
        # ==========================================================
        elif (
            "you are good" in message
            or "you are great" in message
            or "good bot" in message
            or "nice bot" in message
            or "awesome bot" in message
        ):
            return (
                "Thank you! 😊 I'm glad you liked my response."
            )

        # ==========================================================
        # 58. THANK YOU
        # ==========================================================
        elif (
            "thank you" in message
            or "thanks" in message
            or "thank u" in message
        ):
            return (
                "You're very welcome! 😊 "
                "I'm always happy to help."
            )

        # ==========================================================
        # 59. GOOD NIGHT
        # ==========================================================
        elif (
            message == "good night"
            or message == "gn"
        ):
            return (
                "Good night! 🌙 "
                "Sleep well and have a great tomorrow! 😊"
            )

        # ==========================================================
        # 60. GOODBYE
        # ==========================================================
        elif message in [
            "bye",
            "goodbye",
            "see you",
            "see you later"
        ]:
            return (
                "Goodbye! 👋 "
                "Have a great day and keep learning! 🚀"
            )

        # ==========================================================
        # 61. FALLBACK
        # ==========================================================
        else:
            return (
                "I'm sorry, I don't understand that question yet. 🤔\n\n"
                "Try asking me about:\n"
                "• AI\n"
                "• Machine Learning\n"
                "• Deep Learning\n"
                "• NLP\n"
                "• Computer Vision\n"
                "• Generative AI\n"
                "• Python\n"
                "• C++\n"
                "• Java\n"
                "• HTML/CSS/JavaScript\n"
                "• SQL\n"
                "• Git/GitHub\n"
                "• API\n"
                "• Rule-Based Chatbot\n"
                "• CodeOrbit Internship\n\n"
                "Or type 'help' to see all available topics."
            )