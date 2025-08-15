# controller.py

class QuizController:
    def __init__(self):
        self.questions = [
            {
                "question": "كم تستغرق أشعة وحدة من الشمس حتى تصل إلى سطحها من باطن الشمس؟",
                "options": ["8 دقائق", "6 ساعات", "3 أيام", "100,000 سنة"],
                "answer": "100,000 سنة"
            },
            {
                "question": "ما لون المرآة؟",
                "options": ["شفاف", "ما الها لون", "أبيض", "أخضر"],
                "answer": "أخضر"
            },
            {
                "question": "ما هو أول كائن حي على كوكب الأرض؟",
                "options": ["سيدنا آدم", "الأسماك", "الديناصورات", "البكتيريا"],
                "answer": "البكتيريا"
            },
            {
                "question": "ما هو العضو الوحيد في جسم الإنسان الذي لا يصله الدم؟",
                "options": ["القرنية", "الكبد", "الأذن", "الرئة"],
                "answer": "القرنية"
            },
            {
                "question": "لماذا تبدو السماء مظلمة في الفضاء رغم وجود الشمس؟",
                "options": ["لأنه لا يوجد هواء", "لأن الشمس لا تضيء هناك", "لأن الفضاء بارد", "لأن الضوء لا يصل"],
                "answer": "لأنه لا يوجد هواء"
            },
            {
                "question": "شو اللي بيصير إذا دخلت للثقب الأسود؟",
                "options": ["بتتحول لذرات", "بتعلق في الزمن", "بتصير غير مرئي", "ما حدا بيعرف "],
                "answer": "ما حدا بيعرف "
            },
            {
                "question": "ليش الموز منحني؟",
                "options": ["لأنه بيتأثر بالجاذبية", "لأنه بينمو ضد الجاذبية", "لأن الشمس بتشده", "بسبب نوع التربة"],
                "answer": "لأنه بينمو ضد الجاذبية"
            },
            {
                "question": "ما هو أثقل شيء في جسم الإنسان؟",
                "options": ["العظام", "الدماغ", "الكبد", "الجلد"],
                "answer": "الجلد"
            },
            {
                "question": "ما هو الحيوان الذي لا يُصدر أي صوت؟",
                "options": ["نجم البحر", "الدودة", "السلحفاة", "الأرنب"],
                "answer": "نجم البحر"
            }
        ]
        self.score = 0
        self.current = 0

    def get_current_question(self):
        if self.current < len(self.questions):
            return self.questions[self.current]
        return None

    def check_answer(self, selected_text):
        if self.current >= len(self.questions):
            return False
        correct = selected_text == self.questions[self.current]["answer"]
        if correct:
            self.score += 1
        self.current += 1
        return correct

    def get_score(self):
        return self.score

    def total(self):
        return len(self.questions)

    def reset(self):
        self.score = 0
        self.current = 0