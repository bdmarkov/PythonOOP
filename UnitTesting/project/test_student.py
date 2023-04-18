from project.student import Student

from unittest import TestCase, main

class TestStudent(TestCase):
    def setUp(self) -> None:
        self.default_course = 'Python'
        self.default_notes = ["n1", "n2"]
        self.student = Student("Name", {self.default_course: self.default_notes})

    def test_student_initialization(self):
        student = Student("Name", {'Python': ["n1", "n2"]})

        self.assertEqual('Name', student.name)
        self.assertEqual({'Python': ["n1", "n2"]}, student.courses)


    def test_student_initialization_without_courses(self):
        student = Student("Name")

        self.assertEqual('Name', student.name)
        self.assertEqual({}, student.courses)

    def test_enroll_should_extend_notes_for_already_enrolled_course(self):
        new_notes = ['n3', 'n4']
        expected_notes = self.default_notes + new_notes
        result = self.student.enroll(self.default_course, new_notes)

        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertTrue(self.default_course in self.student.courses)
        self.assertEqual(expected_notes, self.student.courses[self.default_course])

    def test_enroll_should_add_new_course_with_notes(self):
        for idx, command in enumerate(['', 'Y']):
            course_name = f"JavaScript{idx}"
            course_notes = ['random JS', 'IE']
            result = self.student.enroll(course_name, course_notes, command)

            self.assertEqual('Course and course notes have been added.', result)
            self.assertTrue(course_name in self.student.courses)
            self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll_should_add_new_course_without_notes(self):

        course_name = "JavaScript"
        course_notes = ['random JS', 'IE']
        result = self.student.enroll(course_name, course_notes, 'N')

        self.assertEqual('Course has been added.', result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])


    def test_add_notes_should_raise_error_when_student_is_not_enrolled_for_the_given_course(self):
        course_name = "JavaScript"

        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course_name, ['JS1', 'JS2'])

        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_add_notes_should_raise_error_when_student_is_enrolled_for_the_given_course(self):
        new_note = 'random note'
        expected_notes = [x for x in self.default_notes]
        expected_notes.append(new_note)
        result = self.student.add_notes(self.default_course, new_note)


        self.assertEqual('Notes have been updated', result)
        self.assertEqual(expected_notes, self.student.courses[self.default_course])

    def test_leave_course_raise_error(self):

        with self.assertRaises(Exception) as ex:
            self.student.leave_course('JavaScript')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course(self):
        result = self.student.leave_course(self.default_course)
        self.assertEqual('Course has been removed', result)
        self.assertTrue(self.default_course not in self.student.courses)

if __name__ == "__main__":
    main()
