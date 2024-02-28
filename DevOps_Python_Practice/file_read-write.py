# 7:
my_file = open("../DevOps_Lesson_Assignments/Archived Lessons/daniel.txt", 'w')
my_file.write("daniel")

my_file = open("../DevOps_Lesson_Assignments/Archived Lessons/daniel.txt", 'r')
s = my_file.read()

my_file.close()
print(s)
