import unittest
class Task:
    def __init__(self, task_id, description, status="pending"):
        self.task_id = task_id
        self.description = description
        self.status = status

    def complete_task(self):
        self.status = "completed"
        return self.status

    def __str__(self):
        return f"Task {self.task_id}: {self.description} ({self.status})"


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task(task_id=1, description="Dasturni yakunlash")

    def test_task_initialization(self):
        """Task obyekti to'g'ri yaratilganligini tekshiradi."""
        self.assertEqual(self.task.task_id, 1)
        self.assertEqual(self.task.description, "Dasturni yakunlash")
        self.assertEqual(self.task.status, "pending")

        task_done = Task(2, "Testlarni yozish", "completed")
        self.assertEqual(task_done.status, "completed")

    def test_complete_task(self):
        """complete_task() metodi statusni to'g'ri yangilashini tekshiradi."""

        new_status = self.task.complete_task()

        self.assertEqual(self.task.status, "completed")
        self.assertEqual(new_status, "completed")

    def test_string_representation(self):
        """__str__ metodi to'g'ri formatdagi string qaytarishini tekshiradi."""
        expected_str = "Task 1: Dasturni yakunlash (pending)"
        self.assertEqual(str(self.task), expected_str)

        self.task.complete_task()
        expected_completed_str = "Task 1: Dasturni yakunlash (completed)"
        self.assertEqual(str(self.task), expected_completed_str)


if __name__ == '__main__':
    unittest.main()