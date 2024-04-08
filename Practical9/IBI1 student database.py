class Students: #class
    #define a function
    def __init__(self,name,major,code_portfolio_score,group_score,exam):
        self.name=name
        self.major=major
        self.code_portfolio_score=code_portfolio_score
        self.group_score=group_score
        self.exam=exam
    
    def print_details(self):
        print(f'{self.name}, Major: {self.major}, Code Portfolio: {self.code_portfolio_score}/100, '
              f'Group Project: {self.group_score}/100, Exam: {self.exam}/100')

#example
student=Students('Anna','BMI', 55, 65, 63)
student.print_details()