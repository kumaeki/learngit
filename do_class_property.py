class Student(object):

    def get_score(self):
        return self.score

    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError("score must be a integer")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 ~ 100")
        self.score=score



s = Student()
s.set_score(60)
print(s.get_score())



class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be a integer")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100")
        self._score=value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth=value

    @property
    def age(self):
        return 2018 - self._birth


s2 = Student2()
s2.score=100
print(s2.score)
s2.birth=1986
print(s2.age)
