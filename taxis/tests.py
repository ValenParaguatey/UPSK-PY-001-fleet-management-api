from django.test import TestCase # type: ignore
from .models import Taxi


class TaxiModelTest(TestCase):
    def test_create_taxi(self):
        # Creando un objeto Taxi
        taxi = Taxi.objects.create(plate='A1234')

        # Se Verifica que el objeto Taxi se haya creado correctamente
        self.assertIsNotNone(taxi)
        self.assertEqual(taxi.plate, 'A1234')

    def test_save_taxi_to_database(self):
        # Se crea un objeto Taxi
        taxi = Taxi(plate='XYZ789')
        taxi.save()

        # Se verifica que el objeto Taxi se haya guardado correctamente en la base de datos
        self.assertIsNotNone(taxi.id)
        self.assertEqual(taxi.plate, 'XYZ789')

