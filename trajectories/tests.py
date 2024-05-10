from django.test import TestCase # type: ignore
from .models import Trajectories, Taxi


class TrajectoriesModelTest(TestCase):
    def test_create_trajectories_table(self):
        # Srea un objeto Taxi para relacionarlo conTrajectories
        taxi = Taxi.objects.create(plate='A1234')

        # Se crea un objeto Trajectories
        trajectory = Trajectories.objects.create(taxi=taxi, date='2024-05-10 12:00:00', latitude=0.0, longitude=0.0)

        # Se verifica que el objeto Trajectories se haya creado correctamente
        self.assertIsNotNone(trajectory)
        self.assertEqual(trajectory.latitude, 0.0)
        self.assertEqual(trajectory.longitude, 0.0)

