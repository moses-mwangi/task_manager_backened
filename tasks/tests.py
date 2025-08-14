from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Task.objects.create(title="Task 1", is_completed=False)
        Task.objects.create(title="Task 2", is_completed=True)

    def test_list_tasks(self):
        res = self.client.get('/api/tasks/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('results', res.data)
        self.assertGreaterEqual(len(res.data['results']), 1)

    def test_filter_completed_tasks(self):
        res = self.client.get('/api/tasks/?is_completed=true')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        for task in res.data['results']:
            self.assertTrue(task['is_completed'])

    def test_create_single_task(self):
        payload = {"title": "New Task", "description": "Test single creation"}
        res = self.client.post('/api/tasks/', payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], "New Task")
        self.assertFalse(res.data['is_completed'])

    def test_bulk_create_tasks(self):
        payload = [
            {"title": "Bulk Task 1", "description": "First bulk task"},
            {"title": "Bulk Task 2", "description": "Second bulk task", "is_completed": True},
            {"title": "Bulk Task 3"}  
        ]
        res = self.client.post('/api/tasks/', payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(res.data), 3)  
        self.assertEqual(res.data[0]['title'], "Bulk Task 1")
        self.assertTrue(res.data[1]['is_completed'] or res.data[1]['is_completed'] is False)

    def test_update_task(self):
        task = Task.objects.first()
        payload = {"title": "Updated Task", "is_completed": True}
        res = self.client.put(f'/api/tasks/{task.id}/', payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], "Updated Task")
        self.assertTrue(res.data['is_completed'])

    def test_delete_task(self):
        task = Task.objects.first()
        res = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
