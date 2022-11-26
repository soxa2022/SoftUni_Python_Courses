from unittest import main, TestCase

from project.student import Student


class StudentTests(TestCase):

    def setUp(self) -> None:
        self.student = Student("Ivan")
        self.student2 = Student("Ani", {"Python": ["new start"]})

    def test_init_work_correct(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"Python": ["new start"]}, self.student2.courses)

    def test_student_update_notes_correct(self):
        result = self.student2.enroll("Python", ["start notes"], "")
        self.assertEqual({"Python": ["new start", "start notes"]}, self.student2.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_student_add_new_course_and_notes_with_y_correct(self):
        result = self.student2.enroll("Java", ["start notes"], "Y")
        self.assertEqual({"Python": ["new start"], "Java": ["start notes"]}, self.student2.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_student_add_new_course_and_notes_with_empty_correct(self):
        result = self.student2.enroll("Java", ["start notes"], "")
        self.assertEqual({"Python": ["new start"], "Java": ["start notes"]}, self.student2.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_student_add_new_course_without_notes(self):
        result = self.student2.enroll("Java", ["start notes"], "N")
        self.assertEqual({"Python": ["new start"], "Java": []}, self.student2.courses)
        self.assertEqual("Course has been added.", result)

    def test_student_add_notes_none_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Python", "new notes")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_student_add_notes_correct(self):
        result = self.student2.add_notes("Python", "new notes")
        self.assertEqual({"Python": ["new start", "new notes"]}, self.student2.courses)
        self.assertEqual("Notes have been updated", result)

    def test_student_leave_course_none_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student2.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_student_leave_course_correct(self):
        result = self.student2.leave_course("Python")
        self.assertEqual({}, self.student2.courses)
        self.assertEqual("Course has been removed", result)


if __name__ == "__main__":
    main()
