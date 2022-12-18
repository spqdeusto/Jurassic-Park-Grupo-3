import unittest
from backend.controllers.handler import Controllers
import backend.models.models as models
import backend.mysql.models as mysql_models
from backend.mysql.mysql import DatabaseClient
import backend.utils.vars as gb
from sqlalchemy.orm import Session

class TestCreateDinosaur(unittest.TestCase):
    def test_create_dinosaur(self):

        # Crea una instancia de la clase de prueba
        test_instance = Controllers()
        
        # Crea un objeto Dinosaur para pasar como argumento al método create_dinosaur
        body = models.Dinosaur(name='Velociraptor', species='Dinosauria', age=3, weigh=50, gender=True, dangerousness=True, recinto=2)
        
        # Llamar al método create_dinosaur y guardar el resultado
        result = test_instance.create_dinosaur(body)
        
        # Comprueba que el resultado es correcto
        self.assertEqual(result, {"status": "ok"})

class TestDeleteDinosaur(unittest.TestCase):
    def test_delete_dinosaur(self):
        # Crea una instancia de la clase de prueba
        test_instance = Controllers()
        
        # Crea un objeto DeleteRequest para pasar como argumento al método delete_dinosaur
        body = models.DeleteRequest(id=1)
        
        # Llamar al método delete_dinosaur y guardar el resultado
        result = test_instance.delete_dinosaur(body)
        
        # No hay un resultado esperado para este método, ya que no devuelve ningún valor.
        # En lugar de eso, podrías comprobar que no se produce ningún error al ejecutar el método.
        self.assertIsNone(result)

class TestQuitElectricity(unittest.TestCase):
    def test_quit_electricity(self):
        # Crea una instancia de la clase de prueba
        test_instance = Controllers()
        
        # Crea un objeto GetRequest para pasar como argumento al método quit_electricity
        body = models.GetRequest(id=1)
        
        # Llamar al método quit_electricity y guardar el resultado
        result = test_instance.quit_electricity(body)
        
        # Verifica que el resultado sea un diccionario con las claves "alerta", "recintos" y "jeeps"
        self.assertIsInstance(result, dict)
        self.assertIn("alerta", result)
        self.assertIn("recintos", result)
        self.assertIn("jeeps", result)
        
class TestGetJeeps(unittest.TestCase):
    def test_get_jeeps(self):
        # Arrange
        controllers = Controllers()

        # Act
        result = controllers.get_jeeps()

        # Assert
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(i, mysql_models.TodoTerreno) for i in result))

if __name__ == '__main__':
    unittest.main()













