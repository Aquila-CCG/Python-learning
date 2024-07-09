# Sample solution to Chapter 8 exercise

class teacher:
    ### BEGIN SOLUTION
    this_year = 2023
    
    
    
    def __init__(self, first_name, last_name, year_birth, student_rating):
        self.first_name = first_name
        self.last_name = last_name
        self.year_birth = year_birth
        self.courses = []
        self.student_rating = min(100, student_rating)
        self.email = first_name.lower() + last_name.lower() + "@uic.edu.cn"
        self.age = self.this_year - year_birth
        self.friendliness = 50.0
    
    
    
    def quality_class(self):
        if self.student_rating >= 80:
            quality = "excellent"
        elif self.student_rating >= 60 and self.student_rating < 80:
            quality = "good"
        elif self.student_rating >= 40 and self.student_rating < 60:
            quality = "average"
        elif self.student_rating < 40:
            quality = "bad"
        return quality
    
    
    
    def introduce(self):
        quality = self.quality_class()
        msg = "Hi, my name is {}. I am your teacher. Students think that I am a(n) {} teacher.".format(self.first_name, quality)
        return msg
    
    
    
    def add_course(self, new_course_name):      
        n_courses = len(self.courses)
        if n_courses > 4:
            msg = "Course limit reached: {} not added.".format(new_course_name)
        else:
            self.courses.append(new_course_name)
            msg = "{} added. Total courses to teach is {}.".format(new_course_name, n_courses+1)
        return msg
    
    
    
    def scold_student(self):
        self.student_rating = max(0, self.student_rating-10)
        msg = "teacher {} scold the students because they do not submit the assignment. His/her rating decreased to {}.".format(self.last_name, self.student_rating)
        return msg
    
    
    
    def help_student(self):
        self.student_rating = min(100, self.student_rating+10)
        msg = "teacher {} help the students to work on the assignment. His/her rating increased to {}.".format(self.last_name,  self.student_rating)
        return msg
    
    
    
    def friendly_score(self):
        n_courses = len(self.courses)
        score = 0.5 * self.student_rating + 50 * (1 - n_courses/5)
        self.friendliness = score
        return score 