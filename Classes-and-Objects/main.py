class Student:
    # Class for Student
    def __init__(self, name, age, tracks, score):
        # The init method or constructor
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    def __str__(self):
        return self.name
    def change_name(self, new_name):
        self.name = new_name
    def change_age(self, new_age):
        try:
            self.age = int(new_age)
        except:
            return
    def add_track(self, track):
        self.tracks.append(track)
    def get_score(self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(54.898)
Bob.add_track("UI/UX")
Bob.get_score()
print(Bob)
print(Bob.get_score())
print(Bob.tracks)
print(Bob.age)