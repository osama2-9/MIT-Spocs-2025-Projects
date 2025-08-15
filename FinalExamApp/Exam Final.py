import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import os
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.styles import get_style_by_name
import time
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

class ExamData:
    """Holds all exam questions and configurations"""
    
    def __init__(self):
        self.coding_questions = [
            """Triangle Pattern Generator

Write a Python program that prints a triangle pattern using * (asterisks).

Requirements:
- The program must have two functions:
    1) One function to generate the triangle pattern. The function should take an alignment type ("left", "right", or "center") as a parameter.
    2) Another function to take input from the user for the number of rows and alignment.
- Based on the inputs, your program should print the pattern accordingly.

Example Output:

If the user inputs:
Enter number of rows: 4
Enter alignment (left/right/center): right

Output:
   *
  **
 ***
****

If the user inputs:
Enter number of rows: 5
Enter alignment (left/right/center): left

Output:
*
**
***
****
*****

If the user inputs:
Enter number of rows: 4
Enter alignment (left/right/center): center

Output:
   *
  ***
 *****
*******
""",
            """Student Grade Lookup System

You need to build a Python program that stores school subjects, students, and their grades.
The program will allow a user to type a student's name and see their grades, average score, and pass/fail status.

Requirements:
1. Create a tuple containing exactly three subject names (for example: "Math", "Science", "English").
2. Create a dictionary where:
   - Each key is a student's name (string).
   - Each value is a list of grades corresponding to the subjects in your tuple.
   Example:
   {
       "Alice": [85, 90, 78],
       "Bob": [70, 60, 80]
   }
3. Ask the user to enter a student's name.
4. If the student exists in your dictionary:
   - Print each subject and their grade on a separate line (match tuple subject with list grade).
   - Calculate and display their average grade.
   - If the average is 60 or higher, print "Pass". Otherwise, print "Fail".
5. If the student does not exist, print "Student not found".

Example:
subjects = ("Math", "Science", "English")
grades = {
    "Alice": [85, 90, 78],
    "Bob": [70, 60, 80]
}

Case 1:
Enter student name: Alice
Math: 85
Science: 90
English: 78
Average: 84.33
Result: Pass

Case 2:
Enter student name: Tom
Student not found
"""
        ]
        
        self.mcq_questions = [
            {"question": "When does a while loop terminate?",
             "options": ["A) When the condition becomes False",
                         "B) When a break statement is encountered",
                         "C) When the loop runs 10 times",
                         "D) Both A and B are correct"],
             "answer": "D) Both A and B are correct",
             "explanation": "A while loop ends when its condition is False or a break is executed."},

            {"question": "Which of these is the time complexity?\nfor i in range(n):\n    for j in range(n):\n        print(i, j)",
             "options": ["A) O(n)", "B) O(n^2)", "C) O(log n)", "D) O(n log n)"],
             "answer": "B) O(n^2)",
             "explanation": "Two nested loops each running n times result in O(n^2)."},     

            {"question": "How many times will this loop iterate?\ni = 0\nwhile i < 3:\n    print(i)\n    i += 1",
             "options": ["A) 2", "B) 3", "C) Infinite times", "D) 4"],
             "answer": "B) 3",
             "explanation": "It runs for i = 0, 1, 2 → 3 iterations."},

            {"question": "What is a key benefit of functions in Python?",
             "options": ["A) Code reuse", "B) Improved modularity", "C) Easier debugging", "D) All of the above"],
             "answer": "D) All of the above",
             "explanation": "Functions help with code reuse, modularity, and debugging."},

            {"question": "Which keyword defines a function in Python?",
             "options": ["A) define", "B) function", "C) def", "D) func"],
             "answer": "C) def",
             "explanation": "'def' is the function definition keyword."},

            {"question": "What symbol ends an if statement condition line?",
             "options": ["A) Semicolon (;)", "B) Comma (,)", "C) Colon (:)", "D) Dot (.)"],
             "answer": "C) Colon (:)",
             "explanation": "In Python, ':' ends the if condition line."},

            {"question": "Which keyword adds an alternative condition?",
             "options": ["A) elif", "B) else if", "C) else if then", "D) otherwise"],
             "answer": "A) elif",
             "explanation": "'elif' is the correct Python keyword."},

            {"question": "What will this loop print?\nfor i in range(3):\n    print(i)",
             "options": ["A) 0 1 2", "B) 1 2 3", "C) 0 1 2 3", "D) 1 2 3 4"],
             "answer": "A) 0 1 2",
             "explanation": "range(3) yields 0, 1, 2."},

            {"question": "Output?\ndef sayHello():\n    print('Hello World!')\n\nsayHello()\nsayHello()",
             "options": ["A) Hello World! Hello World!", "B) 'Hello World!' 'Hello World!'", "C) Hello Hello", "D) None"],
             "answer": "A) Hello World! Hello World!",
             "explanation": "Function prints twice when called twice."},

            {"question": "What happens when calling a function with no return statement?",
             "options": ["A) It returns None", "B) It returns 0", "C) It errors", "D) It returns True"],
             "answer": "A) It returns None",
             "explanation": "Default return value is None in Python."}
        ]

        self.true_false_questions = [
            {"statement": "The first element in a Python list has index 1.",
             "answer": "False", "correction": "The first element has index 0.",
             "explanation": "Python lists are zero-indexed.",
             "keywords": ["index 0", "zero-indexed"]},

            {"statement": "A tuple in Python is mutable.",
             "answer": "False", "correction": "Tuples are immutable.",
             "explanation": "Tuples cannot be modified once created.",
             "keywords": ["immutable"]},

            {"statement": "A Python dictionary stores data as key-value pairs inside curly braces {}.",
             "answer": "True", "correction": "",
             "explanation": "Dictionaries store key-value pairs in {}.",
             "keywords": []},

            {"statement": "Every if and elif must end with a colon :",
             "answer": "True", "correction": "",
             "explanation": "Python syntax requires ':' after condition.",
             "keywords": []},

            {"statement": "Given x=5, if x>3: print('Yes') else print('No') outputs Yes.",
             "answer": "True", "correction": "",
             "explanation": "Condition is True, so Yes is printed.",
             "keywords": []},

            {"statement": "A tuple can contain mutable objects like lists, and those can be modified.",
             "answer": "True", "correction": "",
             "explanation": "Tuple structure immutable, but can hold mutable objects.",
             "keywords": []},

            {"statement": "Dictionary keys can be any type including lists.",
             "answer": "False", "correction": "Keys must be immutable types (strings, numbers, tuples).",
             "explanation": "Mutable types like lists cannot be dictionary keys.",
             "keywords": ["immutable", "string", "tuple"]},

            {"statement": "Non-empty strings, numbers, and collections are True in boolean context.",
             "answer": "True", "correction": "",
             "explanation": "Non-empty values are truthy in Python.",
             "keywords": []},

            {"statement": "list1.append(list2) merges elements of list2 into list1.",
             "answer": "False", "correction": "append() adds list2 as one element; use extend() to merge.",
             "explanation": "append() adds single object; extend() merges each element.",
             "keywords": ["append", "extend"]},

            {"statement": "Two nested loops each running n times have O(n^2) complexity.",
             "answer": "True", "correction": "",
             "explanation": "n × n = n².",
             "keywords": []}
        ]

        self.debug_questions = [
            {
                "snippet": "number = 5\nif number > 0\n    print(\"Positive number\")",
                "answer": "number = 5\nif number > 0:\n    print(\"Positive number\")",
                "explanation": "Missing colon."
            },
            {
                "snippet": "fruits = [\"apple\", \"banana\"]\nprint(fruits[2])",
                "answer": "fruits = [\"apple\", \"banana\"]\nprint(fruits[1])",
                "explanation": "Index fixed."
            },
            {
                "snippet": "age = \"20\"\nyears = 5\ntotal_age = age + years\nprint(total_age)",
                "answer": "age = int(\"20\")\nyears = 5\ntotal_age = age + years\nprint(total_age)",
                "explanation": "Type conversion."
            },
            {
                "snippet": "grades = {\n    \"Alice\": {\"Math\": 85, \"Science\": 90}\n}\n\nprint(grades[\"Alice\"][\"math\"])",
                "answer": "grades = {\n    \"Alice\": {\"Math\": 85, \"Science\": 90}\n}\n\nprint(grades[\"Alice\"][\"Math\"])",
                "explanation": "Key case corrected."
            },
            {
                "snippet": "count = 1\nwhile count > 5:\n    print(count)\n    count += 1",
                "answer": "count = 1\nwhile count <= 5:\n    print(count)\n    count += 1",
                "explanation": "Loop condition fixed."
            }
        ]
        
        # Points configuration
        self.POINTS_CODING = 10
        self.POINTS_MCQ = 1
        self.POINTS_TF = 1
        self.POINTS_DEBUG = 2

class AntiCheatMonitor:
    """Monitors and tracks anti-cheat violations with exceptions for coding tab"""
    
    def __init__(self, exam_controller):
        self.exam_controller = exam_controller
        self.fullscreen_exits = 0
        self.is_fullscreen = False
        self.start_time = None
        self.violations = []
        self.monitoring_active = True
        
    def enable_fullscreen(self):
        """Enable fullscreen mode and start monitoring"""
        self.exam_controller.root.attributes("-fullscreen", True)
        self.is_fullscreen = True
        self.start_time = time.time()
        self.bind_events()
        self.exam_controller.root.focus_force()
        
    def disable_fullscreen(self):
        """Disable fullscreen mode"""
        self.exam_controller.root.attributes("-fullscreen", False)
        self.is_fullscreen = False
        
    def bind_events(self):
        """Bind keyboard and focus events"""
        self.exam_controller.root.bind("<Alt-Tab>", self.on_alt_tab)
        self.exam_controller.root.bind("<Control-c>", self.block_shortcut)
        self.exam_controller.root.bind("<Control-v>", self.block_shortcut)
        self.exam_controller.root.bind("<F11>", self.on_f11)
        self.exam_controller.root.bind("<Escape>", self.on_escape)
        
    def is_coding_section_active(self):
        """Check if currently in coding section"""
        try:
            return self.exam_controller.navigator.current_section == 0  # Coding is section 0
        except:
            return False
            
    def on_alt_tab(self, event=None):
        """Handle Alt+Tab attempts - only track if not in coding section"""
        if not self.is_coding_section_active():
            self.record_violation("Attempted to switch windows (Alt+Tab)")
            return "break"
        # Allow Alt+Tab in coding section
        return None
        
    def on_f11(self, event=None):
        """Handle F11 key press - only track if not in coding section"""
        if not self.is_coding_section_active():
            self.record_violation("Attempted to exit fullscreen (F11)")
            return "break"
        # Allow F11 in coding section
        return None
        
    def on_escape(self, event=None):
        """Handle Escape key - only track if not in coding section"""
        if not self.is_coding_section_active():
            self.record_violation("Attempted to use Escape key")
            return "break"
        # Allow Escape in coding section
        return None
        
    def block_shortcut(self, event=None):
        """Block copy/paste shortcuts only outside coding section"""
        if not self.is_coding_section_active():
            self.record_violation(f"Attempted to use {event.keysym} shortcut")
            return "break"
        # Allow copy/paste in coding section
        return None
        
    def check_focus(self):
        """Check if window has focus - only track if not in coding section"""
        if self.is_fullscreen and hasattr(self.exam_controller, 'exam_started') and self.exam_controller.exam_started:
            try:
                # Check if window lost focus
                if not self.exam_controller.root.focus_displayof():
                    if not self.is_coding_section_active():
                        self.fullscreen_exits += 1
                        self.record_violation(f"Lost window focus (Exit #{self.fullscreen_exits})")
                        
                        if self.fullscreen_exits >= 3:
                            messagebox.showwarning(
                                "Anti-Cheat Warning", 
                                f"You have exited fullscreen {self.fullscreen_exits} times.\n"
                                "Further violations may result in exam termination.\n"
                                "Note: Anti-cheat is disabled during coding questions."
                            )
            except:
                pass  # Ignore focus check errors
        
        # Schedule next check
        self.exam_controller.root.after(1000, self.check_focus)
        
    def record_violation(self, violation_type):
        """Record a violation with timestamp"""
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        self.violations.append(f"[{timestamp}] {violation_type}")
        print(f"Anti-cheat violation recorded: {violation_type}")  # Debug output
        
    def get_violations_report(self):
        """Get formatted violations report"""
        if not self.violations:
            return "No violations detected."
        
        report = f"Total violations: {len(self.violations)}\n"
        report += f"Focus losses: {self.fullscreen_exits}\n\n"
        report += "Detailed violations:\n"
        report += "\n".join(self.violations)
        report += "\n\nNote: Anti-cheat monitoring was disabled during coding questions."
        return report
        
    def update_monitoring_status(self):
        """Update monitoring status based on current section"""
        is_coding = self.is_coding_section_active()
        status = "DISABLED (Coding Section)" if is_coding else "ACTIVE"
        
        try:
            # Update status display if available
            if hasattr(self.exam_controller, 'anti_cheat_status_label'):
                self.exam_controller.anti_cheat_status_label.config(
                    text=f"Anti-cheat: {status}",
                    fg="orange" if is_coding else "red"
                )
        except:
            pass

class PDFGenerator:
    """Handles PDF generation for exam results with improved design and error handling"""
    
    def __init__(self):
        self.header_color = colors.HexColor("#2c3e50")  # Dark blue
        self.correct_color = colors.HexColor("#27ae60")  # Green
        self.incorrect_color = colors.HexColor("#e74c3c")  # Red
        self.text_color = colors.HexColor("#2c3e50")  # Dark blue
        self.light_bg = colors.HexColor("#ecf0f1")  # Light gray
    
    def sanitize_text(self, text):
        """Sanitize text but allow basic HTML tags like <b>, <i>, <u>."""
        if text is None:
            return ""
        text = str(text)
        allowed_tags = ["<b>", "</b>", "<i>", "</i>", "<u>", "</u>"]
        for idx, tag in enumerate(allowed_tags):
            text = text.replace(tag, f"__ALLOWEDTAG{idx}__")
        from xml.sax.saxutils import escape
        text = escape(text, entities={'"': '&quot;', "'": '&apos;'})
        for idx, tag in enumerate(allowed_tags):
            text = text.replace(f"__ALLOWEDTAG{idx}__", tag)
        return text
    
    def safe_paragraph(self, text, style, raw=False):
        """Create a paragraph with error handling; raw=True skips HTML escaping"""
        try:
            if raw:
                return Paragraph(f"<pre>{text}</pre>", style)
            sanitized_text = self.sanitize_text(text)
            return Paragraph(sanitized_text, style)
        except Exception as e:
            print(f"Error creating paragraph: {e}")
            # Fallback to plain text
            return Paragraph(str(text).replace('<', '&lt;').replace('>', '&gt;'), style)
    
    def ensure_directory_exists(self, filepath):
        """Ensure the directory exists for the file path"""
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
    
    def generate_pdf(self, answers, exam_data, score, violations_report):
        """Generate professional exam results PDF with comprehensive error handling"""
        
        try:
            # Ensure we have valid data
            if not answers or 'student_name' not in answers:
                answers = answers or {}
                answers.setdefault('student_name', 'Unknown Student')
                answers.setdefault('student_email', 'unknown@email.com')
            
            # Create safe filename
            safe_name = "".join(c for c in answers['student_name'] if c.isalnum() or c in (' ', '_')).replace(' ', '_')
            if not safe_name:
                safe_name = "Student"
            
            # Determine file path
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            if not os.path.exists(desktop_path):
                # Fallback to current directory if Desktop doesn't exist
                desktop_path = os.getcwd()
            
            filename = f"{safe_name}_Exam_Results.pdf"
            filepath = os.path.join(desktop_path, filename)
            
            # Ensure directory exists
            self.ensure_directory_exists(filepath)
            
            print(f"Generating PDF at: {filepath}")
            
            # Create PDF document
            doc = SimpleDocTemplate(
                filepath, 
                pagesize=A4,
                rightMargin=40, 
                leftMargin=40,
                topMargin=40, 
                bottomMargin=40
            )
            
            # Setup styles
            styles = getSampleStyleSheet()
            custom_styles = {
                'Header': ParagraphStyle(
                    'Header',
                    parent=styles['Heading1'],
                    fontSize=18,
                    textColor=self.header_color,
                    spaceAfter=20
                ),
                'SectionHeader': ParagraphStyle(
                    'SectionHeader',
                    parent=styles['Heading2'],
                    fontSize=14,
                    textColor=colors.white,
                    backColor=self.header_color,
                    spaceBefore=20,
                    spaceAfter=10,
                    leftIndent=10
                ),
                'Question': ParagraphStyle(
                    'Question',
                    parent=styles['Normal'],
                    fontSize=12,
                    textColor=self.text_color,
                    spaceAfter=8,
                    spaceBefore=8
                ),
                'Answer': ParagraphStyle(
                    'Answer',
                    parent=styles['Normal'],
                    fontSize=11,
                    textColor=self.text_color,
                    leftIndent=20,
                    spaceAfter=12
                ),
                'Correct': ParagraphStyle(
                    'Correct',
                    parent=styles['Normal'],
                    fontSize=11,
                    textColor=self.correct_color,
                    leftIndent=20,
                    spaceAfter=8
                ),
                'Incorrect': ParagraphStyle(
                    'Incorrect',
                    parent=styles['Normal'],
                    fontSize=11,
                    textColor=self.incorrect_color,
                    leftIndent=20,
                    spaceAfter=8
                )
            }
            
            story = []
            
            # Title and student info
            story.append(self.safe_paragraph("Python Course Exam Results", custom_styles['Header']))
            story.append(Spacer(1, 20))
            
            # Student information
            info_lines = [
                f"<b>Name:</b> {self.sanitize_text(answers.get('student_name', 'N/A'))}",
                f"<b>Email:</b> {self.sanitize_text(answers.get('student_email', 'N/A'))}",
                f"<b>Final Score:</b> {score}",
                f"<b>Exam Date:</b> {time.strftime('%Y-%m-%d %H:%M:%S')}"
            ]
            
            for line in info_lines:
                story.append(self.safe_paragraph(line, custom_styles['Answer'], raw=True))
            
            story.append(Spacer(1, 30))
            
            # Anti-cheat report
            story.append(self.safe_paragraph("<b>Anti-Cheat Report</b>", custom_styles['SectionHeader']))
            violations_text = violations_report if violations_report else "No violations detected"
            story.append(self.safe_paragraph(violations_text, custom_styles['Answer']))
            story.append(Spacer(1, 30))
            
            # Coding Questions Section
            story.append(self.safe_paragraph("<b>Coding Questions</b>", custom_styles['SectionHeader']))
            story.append(Spacer(1, 15))
            
            coding_answers = answers.get("Coding", {})
            for i, question in enumerate(exam_data.coding_questions):
                # Question number and text
                story.append(self.safe_paragraph(f"<b>Question {i+1}:</b>", custom_styles['Question']))
                
                # Break long question into manageable chunks
                question_text = self.sanitize_text(question)
                question_lines = question_text.split('\n')
                
                for line in question_lines[:20]:  # Limit lines to prevent PDF issues
                    if line.strip():
                        story.append(self.safe_paragraph(line, custom_styles['Answer'], raw=True))
                
                if len(question_lines) > 20:
                    story.append(self.safe_paragraph("... (question truncated for PDF)", custom_styles['Answer']))
                
                story.append(Spacer(1, 10))
                
                # Student answer
                answer = coding_answers.get(i, "No answer provided")
                story.append(self.safe_paragraph("<b>Your Answer:</b>", custom_styles['Question']))
                
                answer_text = self.sanitize_text(answer)
                answer_lines = answer_text.split('\n')
                
                for line in answer_lines[:30]:  # Limit answer lines
                    if line.strip():
                        story.append(self.safe_paragraph(line, custom_styles['Answer'], raw=True))
                
                if len(answer_lines) > 30:
                    story.append(self.safe_paragraph("... (answer truncated for PDF)", custom_styles['Answer']))
                
                story.append(Spacer(1, 20))
                
                # Add page break after every 2 coding questions to prevent overflow
                if (i + 1) % 2 == 0 and i < len(exam_data.coding_questions) - 1:
                    story.append(PageBreak())
            
            # MCQ Section
            story.append(PageBreak())
            story.append(self.safe_paragraph("<b>Multiple Choice Questions</b>", custom_styles['SectionHeader']))
            story.append(Spacer(1, 15))
            
            mcq_answers = answers.get("MCQ", {})
            for i, q in enumerate(exam_data.mcq_questions):
                story.append(self.safe_paragraph(f"<b>Question {i+1}:</b> {self.sanitize_text(q['question'])}", custom_styles['Question']))
                
                student_answer = mcq_answers.get(i, "No answer provided")
                is_correct = student_answer == q["answer"]
                
                style_name = 'Correct' if is_correct else 'Incorrect'
                story.append(self.safe_paragraph(f"<b>Your Answer:</b> {self.sanitize_text(student_answer)}", custom_styles[style_name]))
                
                if not is_correct:
                    story.append(self.safe_paragraph(f"<b>Correct Answer:</b> {self.sanitize_text(q['answer'])}", custom_styles['Correct']))
                    story.append(self.safe_paragraph(f"<b>Explanation:</b> {self.sanitize_text(q['explanation'])}", custom_styles['Answer']))
                
                story.append(Spacer(1, 15))
            
            # True/False Section
            story.append(PageBreak())
            story.append(self.safe_paragraph("<b>True/False Questions</b>", custom_styles['SectionHeader']))
            story.append(Spacer(1, 15))
            
            tf_answers = answers.get("TF", {})
            for i, q in enumerate(exam_data.true_false_questions):
                story.append(self.safe_paragraph(f"<b>Question {i+1}:</b> {self.sanitize_text(q['statement'])}", custom_styles['Question']))
                
                student_answer = tf_answers.get(i, {})
                choice = student_answer.get("choice", "No answer provided")
                correction = student_answer.get("correction", "")
                is_correct = choice == q["answer"]
                
                style_name = 'Correct' if is_correct else 'Incorrect'
                story.append(self.safe_paragraph(f"<b>Your Answer:</b> {self.sanitize_text(choice)}", custom_styles[style_name]))
                
                if correction:
                    story.append(self.safe_paragraph(f"<b>Your Correction:</b> {self.sanitize_text(correction)}", custom_styles['Answer']))
                
                if not is_correct:
                    if q.get("correction"):
                        story.append(self.safe_paragraph(f"<b>Expected Correction:</b> {self.sanitize_text(q['correction'])}", custom_styles['Correct']))
                    story.append(self.safe_paragraph(f"<b>Explanation:</b> {self.sanitize_text(q['explanation'])}", custom_styles['Answer']))
                
                story.append(Spacer(1, 15))
            
            # Debugging Section
            story.append(PageBreak())
            story.append(self.safe_paragraph("<b>Debugging Questions</b>", custom_styles['SectionHeader']))
            story.append(Spacer(1, 15))
            
            debug_answers = answers.get("Debug", {})
            for i, q in enumerate(exam_data.debug_questions):
                story.append(self.safe_paragraph(f"<b>Question {i+1}: Original Code</b>", custom_styles['Question']))
                
                # Original code
                snippet_lines = self.sanitize_text(q["snippet"]).split('\n')
                for line in snippet_lines:
                    if line.strip():
                        story.append(self.safe_paragraph(line, custom_styles['Answer'], raw=True))
                
                story.append(Spacer(1, 10))
                
                # Student answer
                answer = debug_answers.get(i, "No answer provided")
                story.append(self.safe_paragraph("<b>Your Corrected Code:</b>", custom_styles['Question']))
                
                answer_lines = self.sanitize_text(answer).split('\n')
                for line in answer_lines:
                    if line.strip():
                        story.append(self.safe_paragraph(line, custom_styles['Answer'], raw=True))
                
                story.append(Spacer(1, 10))
                
                # Expected answer
                story.append(self.safe_paragraph("<b>Expected Correction:</b>", custom_styles['Question']))
                expected_lines = self.sanitize_text(q["answer"]).split('\n')
                for line in expected_lines:
                    if line.strip():
                        story.append(self.safe_paragraph(line, custom_styles['Correct']))
                
                story.append(Spacer(1, 8))
                story.append(self.safe_paragraph(f"<b>Explanation:</b> {self.sanitize_text(q['explanation'])}", custom_styles['Answer']))
                story.append(Spacer(1, 20))
            
            # Build the PDF
            print("Building PDF document...")
            doc.build(story)
            
            print(f"PDF successfully generated: {filepath}")
            return filepath
            
        except Exception as e:
            print(f"Error generating PDF: {e}")
            # Create a simple fallback PDF
            try:
                fallback_path = os.path.join(os.getcwd(), f"exam_results_fallback_{int(time.time())}.pdf")
                c = canvas.Canvas(fallback_path, pagesize=A4)
                
                # Simple fallback content
                c.setFont("Helvetica-Bold", 16)
                c.drawString(50, 750, "Python Course Exam Results")
                c.setFont("Helvetica", 12)
                c.drawString(50, 720, f"Student: {answers.get('student_name', 'N/A')}")
                c.drawString(50, 700, f"Email: {answers.get('student_email', 'N/A')}")
                c.drawString(50, 680, f"Score: {score}")
                c.drawString(50, 660, f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
                
                c.drawString(50, 620, "Anti-cheat Report:")
                violations_lines = str(violations_report).split('\n')[:20]
                y = 600
                for line in violations_lines:
                    c.drawString(70, y, line[:80])  # Limit line length
                    y -= 15
                    if y < 100:
                        break
                
                c.drawString(50, y-20, "Detailed answers available in application data.")
                c.save()
                
                print(f"Fallback PDF created: {fallback_path}")
                return fallback_path
                
            except Exception as e2:
                print(f"Failed to create fallback PDF: {e2}")
                return None

class QuestionRenderer:
    """Handles rendering different types of questions"""
    
    def __init__(self, question_frame):
        self.question_frame = question_frame
    
    def clear_frame(self):
        """Clear all widgets from question frame"""
        for widget in self.question_frame.winfo_children():
            widget.destroy()
    
    def highlight_code(self, text_widget, code):
        """Apply syntax highlighting to code"""
        try:
            style = get_style_by_name("monokai")
            for token, content in lex(code, PythonLexer()):
                tag_name = str(token)
                text_widget.insert("end", content, tag_name)
                color = style.styles.get(token)
                if color and color.startswith("#"):
                    text_widget.tag_config(tag_name, foreground=color)
        except:
            # Fallback to plain text if syntax highlighting fails
            text_widget.insert("end", code)
    
    def render_coding_question(self, question_text, question_num, total_questions, points, current_answer=""):
        """Render coding question interface"""
        self.clear_frame()
        
        # Title
        title_label = tk.Label(
            self.question_frame,
            text=f"Coding Question {question_num} of {total_questions} — ({points} points)",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=10
        )
        title_label.pack(fill="x", padx=5, pady=5)
        
        # Anti-cheat status for coding section
        status_label = tk.Label(
            self.question_frame,
            text="🔓 Anti-cheat monitoring disabled for coding questions",
            font=("Arial", 11),
            bg="#f39c12",
            fg="white",
            pady=5
        )
        status_label.pack(fill="x", padx=5)
        
        # Question display with syntax highlighting
        question_display = tk.Text(
            self.question_frame,
            width=90, height=12,
            font=("Consolas", 11),
            wrap="word",
            bg="#272822",
            fg="#f8f8f2",
            insertbackground="white",
            state="normal"
        )
        self.highlight_code(question_display, question_text)
        question_display.config(state="disabled")
        question_display.pack(fill="both", expand=False, padx=10, pady=5)
        
        # Answer area
        answer_label = tk.Label(
            self.question_frame,
            text="Your Answer:",
            font=("Arial", 12, "bold")
        )
        answer_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        answer_text = scrolledtext.ScrolledText(
            self.question_frame,
            width=80, height=10,
            font=("Consolas", 11),
            bg="#f8f9fa",
            fg="#2c3e50"
        )
        answer_text.insert("1.0", current_answer)
        answer_text.pack(pady=5, padx=10, fill="both", expand=True)
        
        return answer_text
    
    def render_mcq_question(self, question_data, question_num, total_questions, points, current_answer=""):
        """Render multiple choice question interface"""
        self.clear_frame()
        
        # Title
        title_label = tk.Label(
            self.question_frame,
            text=f"MCQ Question {question_num} of {total_questions} — ({points} point)",
            font=("Arial", 16, "bold"),
            bg="#27ae60",
            fg="white",
            pady=10
        )
        title_label.pack(fill="x", padx=5, pady=5)
        
        # Anti-cheat status
        status_label = tk.Label(
            self.question_frame,
            text="🔒 Anti-cheat monitoring active",
            font=("Arial", 11),
            bg="#e74c3c",
            fg="white",
            pady=5
        )
        status_label.pack(fill="x", padx=5)
        
        # Question text
        question_label = tk.Label(
            self.question_frame,
            text=question_data["question"],
            font=("Arial", 14, "bold"),
            wraplength=750,
            justify="left",
            anchor="w",
            bg="#ecf0f1",
            pady=15,
            padx=15
        )
        question_label.pack(fill="x", padx=10, pady=10)
        
        # Options
        selected_var = tk.StringVar(value=current_answer)
        option_vars = []
        
        options_frame = tk.Frame(self.question_frame, bg="#f8f9fa")
        options_frame.pack(fill="x", padx=20, pady=10)
        
        for i, option in enumerate(question_data["options"]):
            var = tk.BooleanVar(value=(option == current_answer))
            option_vars.append((var, option))
            
            chk = tk.Checkbutton(
                options_frame,
                text=option,
                font=("Arial", 13),
                variable=var,
                anchor="w",
                bg="#f8f9fa",
                activebackground="#e8f4f8",
                pady=8,
                command=lambda o=option, v=var: self._select_single_option(o, v, option_vars, selected_var)
            )
            chk.pack(anchor="w", pady=5, padx=10, fill="x")
        
        return selected_var
    
    def _select_single_option(self, selected_option, selected_var_obj, all_options, string_var):
        """Handle single selection for MCQ"""
        if selected_var_obj.get():
            # Uncheck all others
            for var, option in all_options:
                if option != selected_option:
                    var.set(False)
            string_var.set(selected_option)
        else:
            string_var.set("")


class ExamNavigator:
    """Handles navigation between questions and sections"""
    
    def __init__(self, exam_controller):
        self.exam_controller = exam_controller
        self.current_section = 0
        self.current_question = 0
        self.sections = ['coding', 'mcq', 'true_false', 'debug']
    
    def get_section_info(self):
        """Get current section and question info"""
        section_name = self.sections[self.current_section]
        section_lengths = {
            'coding': len(self.exam_controller.exam_data.coding_questions),
            'mcq': len(self.exam_controller.exam_data.mcq_questions),
            'true_false': len(self.exam_controller.exam_data.true_false_questions),
            'debug': len(self.exam_controller.exam_data.debug_questions)
        }
        return section_name, section_lengths[section_name]
    
    def can_go_back(self):
        """Check if can navigate back"""
        return self.current_section > 0 or self.current_question > 0
    
    def can_go_forward(self):
        """Check if can navigate forward"""
        section_name, section_length = self.get_section_info()
        return not (self.current_section == len(self.sections) - 1 and 
                   self.current_question == section_length - 1)
    
    def go_back(self):
        """Navigate to previous question"""
        if self.current_question > 0:
            self.current_question -= 1
        elif self.current_section > 0:
            self.current_section -= 1
            _, section_length = self.get_section_info()
            self.current_question = section_length - 1
    
    def go_forward(self):
        """Navigate to next question"""
        section_name, section_length = self.get_section_info()
        if self.current_question < section_length - 1:
            self.current_question += 1
        else:
            self.current_section += 1
            self.current_question = 0
    
    def jump_to_section(self, section_index):
        """Jump directly to a section"""
        if 0 <= section_index < len(self.sections):
            self.current_section = section_index
            self.current_question = 0
            return True
        return False


class ExamController:
    """Main controller for the exam application"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.exam_data = ExamData()
        self.anti_cheat = AntiCheatMonitor(self)
        self.pdf_generator = PDFGenerator()
        self.navigator = ExamNavigator(self)
        
        self.answers = {"student_name": "", "student_email": ""}
        self.score = 0
        self.exam_started = False
        
        self.setup_gui()
        
    def setup_gui(self):
        """Setup the main GUI"""
        self.root.title("Python Course Exam System")
        self.root.attributes("-fullscreen", True)  # start in fullscreen
        self.root.configure(bg="#34495e")
        
        # Apply modern styling
        style = ttk.Style()
        style.theme_use('clam')
        
        # Create main container
        self.main_container = tk.Frame(self.root, bg="#34495e")
        self.main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Header frame
        self.header_frame = tk.Frame(self.main_container, bg="#2c3e50", height=80)
        self.header_frame.pack(fill="x", pady=(0, 10))
        self.header_frame.pack_propagate(False)
        
        self.title_label = tk.Label(
            self.header_frame,
            text="Python Course Examination System",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#2c3e50"
        )
        self.title_label.pack(pady=20)
        
        # Content area
        self.content_frame = tk.Frame(self.main_container, bg="white")
        self.content_frame.pack(fill="both", expand=True)
        
        # Navigation tabs (initially hidden)
        self.nav_notebook = ttk.Notebook(self.content_frame)
        
        # Question display area
        self.question_frame = tk.Frame(self.content_frame, bg="white")
        self.question_frame.pack(fill="both", expand=True)
        
        self.renderer = QuestionRenderer(self.question_frame)
        
        # Control buttons frame
        self.controls_frame = tk.Frame(self.main_container, bg="#34495e", height=60)
        self.controls_frame.pack(fill="x", pady=(10, 0))
        self.controls_frame.lift()  # Ensure navigation buttons always visible
        self.controls_frame.pack_propagate(False)
        
        self.back_btn = tk.Button(
            self.controls_frame,
            text="← Back",
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=10,
            command=self.go_back
        )
        self.back_btn.pack(side="left", padx=10, pady=10)
        
        self.next_btn = tk.Button(
            self.controls_frame,
            text="Next →",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            command=self.go_forward
        )
        self.next_btn.pack(side="right", padx=10, pady=10)
        
        # Status label
        self.status_label = tk.Label(
            self.controls_frame,
            text="Ready to start exam",
            font=("Arial", 11),
            fg="white",
            bg="#34495e"
        )
        self.status_label.pack(pady=20)
        
        self.show_start_screen()
    
    def show_start_screen(self):
        """Display the exam start screen"""
        self.renderer.clear_frame()
        
        start_frame = tk.Frame(self.question_frame, bg="white")
        start_frame.pack(fill="both", expand=True)
        
        # Welcome message
        welcome_label = tk.Label(
            start_frame,
            text="Welcome to the Python Programming Exam",
            font=("Arial", 18, "bold"),
            fg="#2c3e50",
            bg="white"
        )
        welcome_label.pack(pady=30)
        
        # Instructions
        instructions = """
        EXAM INSTRUCTIONS:
        
        • This exam consists of 4 sections: Coding, Multiple Choice, True/False, and Debugging
        • The exam will run in fullscreen mode to prevent cheating
        • Anti-cheat monitoring is DISABLED during coding questions to allow external tools
        • Anti-cheat monitoring is ACTIVE during MCQ, True/False, and Debugging sections
        • You can navigate between questions using the Back/Next buttons
        • Make sure to answer all questions before finishing
        • Your answers are automatically saved as you progress
        
        ANTI-CHEAT MEASURES:
        • Fullscreen mode is mandatory during the exam
        • In NON-CODING sections: Alt+Tab and shortcuts are disabled, focus changes are monitored
        • In CODING sections: All shortcuts and window switching are allowed
        • Multiple violations in monitored sections may result in exam termination
        """
        
        instructions_label = tk.Label(
            start_frame,
            text=instructions,
            font=("Arial", 11),
            justify="left",
            fg="#34495e",
            bg="#ecf0f1",
            padx=20,
            pady=20
        )
        instructions_label.pack(pady=20, padx=50, fill="x")
        
        # Student info form
        info_frame = tk.Frame(start_frame, bg="white")
        info_frame.pack(pady=20)
        
        # Name field
        tk.Label(info_frame, text="Full Name:", font=("Arial", 12, "bold"), 
                bg="white", fg="#2c3e50").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.name_var = tk.StringVar()
        name_entry = tk.Entry(info_frame, textvariable=self.name_var, 
                             font=("Arial", 12), width=40, relief="solid", bd=1)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Email field
        tk.Label(info_frame, text="Email:", font=("Arial", 12, "bold"), 
                bg="white", fg="#2c3e50").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.email_var = tk.StringVar()
        email_entry = tk.Entry(info_frame, textvariable=self.email_var, 
                              font=("Arial", 12), width=40, relief="solid", bd=1)
        email_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Start button
        start_btn = tk.Button(
            start_frame,
            text="🚀 Start Exam",
            font=("Arial", 16, "bold"),
            bg="#27ae60",
            fg="white",
            padx=40,
            pady=15,
            command=self.start_exam
        )
        start_btn.pack(pady=30)
        
        # Hide navigation controls
        self.back_btn.config(state="disabled")
        self.next_btn.config(state="disabled")
    
    def start_exam(self):
        """Start the exam after validation"""
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        
        if not name or not email:
            messagebox.showerror("Missing Information", 
                               "Please enter your full name and email address.")
            return
            
        if "@" not in email:
            messagebox.showerror("Invalid Email", 
                               "Please enter a valid email address.")
            return
        
        # Confirm exam start
        if not messagebox.askyesno("Start Exam", 
                                  "Are you ready to start the exam?\n\n" +
                                  "The exam will switch to fullscreen mode.\n" +
                                  "Anti-cheat monitoring will be active except during coding questions."):
            return
        
        self.answers["student_name"] = name
        self.answers["student_email"] = email
        self.exam_started = True
        
        # Enable fullscreen and anti-cheat monitoring
        self.anti_cheat.enable_fullscreen()
        self.anti_cheat.check_focus()
        
        # Setup navigation tabs
        self.setup_navigation_tabs()
        
        # Start with first question
        self.navigator.current_section = 0
        self.navigator.current_question = 0
        self.show_current_question()
        
        # Enable navigation controls
        self.back_btn.config(state="normal")
        self.next_btn.config(state="normal")
        
        messagebox.showinfo("Exam Started", 
                           "Exam has started! You are now in fullscreen mode.\n" +
                           "Anti-cheat monitoring is disabled for coding questions.")
    
    def setup_navigation_tabs(self):
        """Setup navigation tabs for different question types"""
        self.nav_notebook.pack(fill="x", pady=10)
        
        # Create tabs for each section
        sections = [
            ("📝 Coding", "#3498db"),
            ("🔤 Multiple Choice", "#27ae60"), 
            ("✓ True/False", "#f39c12"),
            ("🐛 Debugging", "#e74c3c")
        ]
        
        self.section_frames = {}
        for i, (tab_name, color) in enumerate(sections):
            frame = tk.Frame(self.nav_notebook, bg="white")
            self.nav_notebook.add(frame, text=tab_name)
            self.section_frames[i] = frame
            
            # Add section summary
            summary_label = tk.Label(
                frame, 
                text=f"Section {i+1}: {tab_name.split()[1]}",
                font=("Arial", 14, "bold"),
                fg=color,
                bg="white"
            )
            summary_label.pack(pady=20)
        
        # Bind tab selection
        self.nav_notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)
    
    def on_tab_changed(self, event=None):
        """Handle tab change events"""
        if hasattr(self, 'exam_started') and self.exam_started:
            # Save current answer before switching tabs
            self.save_current_answer()
            selected_tab = self.nav_notebook.index(self.nav_notebook.select())
            if self.navigator.jump_to_section(selected_tab):
                self.show_current_question()
                # Update anti-cheat status when section changes
                self.anti_cheat.update_monitoring_status()
    
    def show_current_question(self):
        """Display the current question based on navigator state"""
        section_name, section_length = self.navigator.get_section_info()
        question_num = self.navigator.current_question + 1
        
        # Update status
        anti_cheat_status = "DISABLED" if section_name == 'coding' else "ACTIVE"
        self.status_label.config(
            text=f"Section: {section_name.title()} | Q: {question_num}/{section_length} | Anti-cheat: {anti_cheat_status}"
        )
        
        # Update navigation buttons
        self.back_btn.config(state="normal" if self.navigator.can_go_back() else "disabled")
        self.next_btn.config(state="normal")
        if self.navigator.can_go_forward():
            self.next_btn.config(text="Next →", command=self.go_forward)
        else:
            self.next_btn.config(text="🏁 Finish Exam", command=self.finish_exam)
        
        # Show appropriate question type
        if section_name == 'coding':
            self.show_coding_question()
        elif section_name == 'mcq':
            self.show_mcq_question()
        elif section_name == 'true_false':
            self.show_true_false_question()
        elif section_name == 'debug':
            self.show_debug_question()
            
        # Update anti-cheat monitoring status
        self.anti_cheat.update_monitoring_status()
    
    def show_coding_question(self):
        """Display coding question"""
        question_idx = self.navigator.current_question
        question_text = self.exam_data.coding_questions[question_idx]
        current_answer = self.answers.get("Coding", {}).get(question_idx, "")
        
        self.current_input = self.renderer.render_coding_question(
            question_text,
            question_idx + 1,
            len(self.exam_data.coding_questions),
            self.exam_data.POINTS_CODING,
            current_answer
        )
    
    def show_mcq_question(self):
        """Display multiple choice question"""
        question_idx = self.navigator.current_question
        question_data = self.exam_data.mcq_questions[question_idx]
        current_answer = self.answers.get("MCQ", {}).get(question_idx, "")
        
        self.current_input = self.renderer.render_mcq_question(
            question_data,
            question_idx + 1,
            len(self.exam_data.mcq_questions),
            self.exam_data.POINTS_MCQ,
            current_answer
        )
    
    def show_true_false_question(self):
        """Display true/false question"""
        question_idx = self.navigator.current_question
        question_data = self.exam_data.true_false_questions[question_idx]
        
        self.renderer.clear_frame()
        
        # Title
        title_label = tk.Label(
            self.renderer.question_frame,
            text=f"True/False Question {question_idx + 1} of {len(self.exam_data.true_false_questions)} — ({self.exam_data.POINTS_TF} point)",
            font=("Arial", 16, "bold"),
            bg="#f39c12",
            fg="white",
            pady=10
        )
        title_label.pack(fill="x", padx=5, pady=5)
        
        # Anti-cheat status
        status_label = tk.Label(
            self.renderer.question_frame,
            text="🔒 Anti-cheat monitoring active",
            font=("Arial", 11),
            bg="#e74c3c",
            fg="white",
            pady=5
        )
        status_label.pack(fill="x", padx=5)
        
        # Statement
        statement_label = tk.Label(
            self.renderer.question_frame,
            text=question_data["statement"],
            font=("Arial", 14, "bold"),
            wraplength=750,
            justify="left",
            anchor="w",
            bg="#fef9e7",
            pady=15,
            padx=15
        )
        statement_label.pack(fill="x", padx=10, pady=10)
        
        # True/False options
        current_answers = self.answers.get("TF", {}).get(question_idx, {})
        choice = tk.StringVar(value=current_answers.get("choice", ""))
        
        options_frame = tk.Frame(self.renderer.question_frame, bg="#f8f9fa")
        options_frame.pack(fill="x", padx=20, pady=10)
        
        option_vars = []
        for option in ["True", "False"]:
            var = tk.BooleanVar(value=(option == choice.get()))
            option_vars.append((var, option))
            
            chk = tk.Checkbutton(
                options_frame,
                text=option,
                font=("Arial", 13, "bold"),
                variable=var,
                anchor="w",
                bg="#f8f9fa",
                activebackground="#fff3cd",
                pady=8,
                command=lambda o=option, v=var: self.renderer._select_single_option(o, v, option_vars, choice)
            )
            chk.pack(anchor="w", pady=5, padx=10, fill="x")
        
        # Correction field (for False answers)
        correction_label = tk.Label(
            self.renderer.question_frame,
            text="If False, provide correction:",
            font=("Arial", 12, "bold"),
            anchor="w"
        )
        correction_label.pack(fill="x", padx=20, pady=(20, 5))
        
        correction_var = tk.StringVar(value=current_answers.get("correction", ""))
        correction_entry = tk.Text(
            self.renderer.question_frame,
            height=3,
            font=("Arial", 11),
            wrap="word"
        )
        correction_entry.insert("1.0", correction_var.get())
        correction_entry.pack(fill="x", padx=20, pady=5)
        
        self.current_input = {"choice": choice, "correction": correction_entry}
    
    def show_debug_question(self):
        """Display debugging question"""
        question_idx = self.navigator.current_question
        question_data = self.exam_data.debug_questions[question_idx]
        current_answer = self.answers.get("Debug", {}).get(question_idx, "")
        
        self.renderer.clear_frame()
        
        # Title
        title_label = tk.Label(
            self.renderer.question_frame,
            text=f"Debugging Question {question_idx + 1} of {len(self.exam_data.debug_questions)} — ({self.exam_data.POINTS_DEBUG} points)",
            font=("Arial", 16, "bold"),
            bg="#e74c3c",
            fg="white",
            pady=10
        )
        title_label.pack(fill="x", padx=5, pady=5)
        
        # Anti-cheat status
        status_label = tk.Label(
            self.renderer.question_frame,
            text="🔒 Anti-cheat monitoring active",
            font=("Arial", 11),
            bg="#e74c3c",
            fg="white",
            pady=5
        )
        status_label.pack(fill="x", padx=5)
        
        # Instructions
        instruction_label = tk.Label(
            self.renderer.question_frame,
            text="Find and fix the error in this code snippet:",
            font=("Arial", 14, "bold"),
            bg="#fadbd8",
            pady=10
        )
        instruction_label.pack(fill="x", padx=10, pady=5)
        
        # Code snippet
        code_frame = tk.Frame(self.renderer.question_frame, bg="#2c3e50")
        code_frame.pack(fill="x", padx=10, pady=5)
        
        code_label = tk.Label(
            code_frame,
            text=question_data["snippet"],
            font=("Consolas", 12),
            bg="#2c3e50",
            fg="#ecf0f1",
            anchor="w",
            justify="left",
            padx=15,
            pady=15
        )
        code_label.pack(fill="x")
        
        # Answer area
        answer_label = tk.Label(
            self.renderer.question_frame,
            text="Your corrected code:",
            font=("Arial", 12, "bold")
        )
        answer_label.pack(anchor="w", padx=10, pady=(15, 5))
        
        answer_text = scrolledtext.ScrolledText(
            self.renderer.question_frame,
            width=80, height=8,
            font=("Consolas", 11),
            bg="#f8f9fa"
        )
        answer_text.insert("1.0", current_answer)
        answer_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.current_input = answer_text
    
    def save_current_answer(self):
        """Save the current question's answer"""
        section_name, _ = self.navigator.get_section_info()
        question_idx = self.navigator.current_question
        
        if section_name == 'coding':
            if hasattr(self, 'current_input'):
                answer = self.current_input.get("1.0", tk.END).strip()
                self.answers.setdefault("Coding", {})[question_idx] = answer
                
        elif section_name == 'mcq':
            if hasattr(self, 'current_input'):
                answer = self.current_input.get()
                self.answers.setdefault("MCQ", {})[question_idx] = answer
                
        elif section_name == 'true_false':
            if hasattr(self, 'current_input'):
                choice = self.current_input["choice"].get()
                correction = self.current_input["correction"].get("1.0", tk.END).strip()
                self.answers.setdefault("TF", {})[question_idx] = {
                    "choice": choice,
                    "correction": correction
                }
                
        elif section_name == 'debug':
            if hasattr(self, 'current_input'):
                answer = self.current_input.get("1.0", tk.END).strip()
                self.answers.setdefault("Debug", {})[question_idx] = answer
    
    def go_back(self):
        """Go to previous question"""
        self.save_current_answer()
        self.navigator.go_back()
        self.show_current_question()
        
        # Update tab selection
        self.nav_notebook.select(self.navigator.current_section)
    
    def go_forward(self):
        """Go to next question"""
        self.save_current_answer()
        self.navigator.go_forward()
        self.show_current_question()
        
        # Update tab selection
        self.nav_notebook.select(self.navigator.current_section)
    
    def calculate_score(self):
        """Calculate the final exam score"""
        score = 0
        
        # Coding questions - full points if answer provided
        for i in range(len(self.exam_data.coding_questions)):
            if self.answers.get("Coding", {}).get(i, "").strip():
                score += self.exam_data.POINTS_CODING
        
        # MCQ questions
        for i, question in enumerate(self.exam_data.mcq_questions):
            if self.answers.get("MCQ", {}).get(i, "") == question["answer"]:
                score += self.exam_data.POINTS_MCQ
        
        # True/False questions
        for i, question in enumerate(self.exam_data.true_false_questions):
            tf_answer = self.answers.get("TF", {}).get(i, {})
            if tf_answer.get("choice", "") == question["answer"]:
                score += self.exam_data.POINTS_TF
        
        # Debug questions - full points if answer provided
        for i in range(len(self.exam_data.debug_questions)):
            if self.answers.get("Debug", {}).get(i, "").strip():
                score += self.exam_data.POINTS_DEBUG
        
        return score
    
    def finish_exam(self):
        """Finish the exam and generate results"""
        # Save current answer before finishing
        self.save_current_answer()
        
        # Confirm finish
        if not messagebox.askyesno("Finish Exam", 
                                  "Are you sure you want to finish the exam?\n\n" +
                                  "This action cannot be undone."):
            return
        
        # Calculate score
        self.score = self.calculate_score()
        
        # Calculate maximum possible score
        max_score = (len(self.exam_data.coding_questions) * self.exam_data.POINTS_CODING +
                    len(self.exam_data.mcq_questions) * self.exam_data.POINTS_MCQ +
                    len(self.exam_data.true_false_questions) * self.exam_data.POINTS_TF +
                    len(self.exam_data.debug_questions) * self.exam_data.POINTS_DEBUG)
        
        # Disable fullscreen
        self.anti_cheat.disable_fullscreen()
        
        # Generate PDF report with error handling
        violations_report = self.anti_cheat.get_violations_report()
        
        try:
            print("Starting PDF generation...")
            pdf_path = self.pdf_generator.generate_pdf(
                self.answers, self.exam_data, self.score, violations_report
            )
            
            if pdf_path and os.path.exists(pdf_path):
                pdf_message = f"Results PDF saved to:\n{pdf_path}"
                print(f"PDF generated successfully: {pdf_path}")
            else:
                pdf_message = "PDF generation failed, but exam data is saved in memory."
                print("PDF generation failed")
                
        except Exception as e:
            print(f"PDF generation error: {e}")
            pdf_message = f"PDF generation encountered an error: {str(e)[:100]}..."
            
            # Try to save basic results to a text file as backup
            try:
                backup_path = os.path.join(os.path.expanduser("~"), "Desktop", f"exam_results_backup_{int(time.time())}.txt")
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(f"Python Course Exam Results\n")
                    f.write(f"=" * 50 + "\n")
                    f.write(f"Student: {self.answers.get('student_name', 'N/A')}\n")
                    f.write(f"Email: {self.answers.get('student_email', 'N/A')}\n")
                    f.write(f"Score: {self.score}/{max_score} ({(self.score/max_score)*100:.1f}%)\n")
                    f.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"Anti-cheat violations: {self.anti_cheat.fullscreen_exits}\n\n")
                    f.write("Anti-cheat Report:\n")
                    f.write(violations_report)
                    f.write("\n\nAnswers:\n")
                    for section, section_answers in self.answers.items():
                        if section not in ['student_name', 'student_email']:
                            f.write(f"\n{section}:\n")
                            f.write(str(section_answers))
                            f.write("\n")
                
                pdf_message += f"\nBackup text file created: {backup_path}"
                print(f"Backup text file created: {backup_path}")
                
            except Exception as backup_error:
                print(f"Backup file creation failed: {backup_error}")
                pdf_message += "\nBackup file creation also failed."
        
        # Show completion message
        completion_message = f"""Exam Completed Successfully!

Final Score: {self.score}/{max_score} ({(self.score/max_score)*100:.1f}%)

Anti-cheat violations: {self.anti_cheat.fullscreen_exits}

{pdf_message}

Thank you for taking the exam!"""
        
        messagebox.showinfo("Exam Completed", completion_message)
        
        # Also print to console for debugging
        print("=" * 50)
        print("EXAM COMPLETED")
        print("=" * 50)
        print(f"Student: {self.answers.get('student_name', 'N/A')}")
        print(f"Email: {self.answers.get('student_email', 'N/A')}")
        print(f"Final Score: {self.score}/{max_score} ({(self.score/max_score)*100:.1f}%)")
        print(f"Anti-cheat violations: {self.anti_cheat.fullscreen_exits}")
        print("=" * 50)
        
        # Close application
        self.root.destroy()
    
    def run(self):
        """Start the exam application"""
        try:
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Main execution
if __name__ == "__main__":
    try:
        exam = ExamController()
        exam.run()
    except ImportError as e:
        print(f"Missing required library: {e}")
        print("Please install required packages:")
        print("pip install reportlab pygments")
    except Exception as e:
        print(f"Error starting exam system: {e}")