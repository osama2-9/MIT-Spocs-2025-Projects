# 📝 Python Exam System

A comprehensive Python-based application for administering programming exams with **built-in anti-cheat measures** and professional **PDF reporting**.

---

## 📌 Overview
This Python Exam System allows instructors to conduct exams that include various question types, enforce fullscreen mode, track cheating attempts, and generate detailed reports.

---

## ✨ Features

### **Question Types**
- **Coding Questions**
  - Students write Python code to solve problems
  - Anti-cheat disabled to allow IDE use
  - Syntax highlighting for questions
- **Multiple Choice Questions**
  - Single-select format
  - Immediate feedback on correct answers
- **True/False Questions**
  - Option to provide corrections for false statements
  - Detailed explanations
- **Debugging Questions**
  - Identify and fix errors in code snippets
  - Points awarded for correct fixes

### **Anti-Cheat System**
- Fullscreen mode enforcement
- Window focus monitoring
- Shortcut blocking (except in coding sections)
- Violation tracking and reporting
- Visual indicators of monitoring status

### **Reporting**
- Professional PDF generation with:
  - Student information
  - Question responses
  - Score calculation
  - Anti-cheat violation report
- Fallback text file generation if PDF creation fails

---
## 🛠 Technical Details

### **Key Components**
- **ExamController** — Main application controller
- **AntiCheatMonitor** — Handles fullscreen enforcement and monitoring
- **PDFGenerator** — Creates professional PDF reports
- **QuestionRenderer** — Displays different question types
- **ExamNavigator** — Manages question navigation
