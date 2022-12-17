import unittest
import backend.controllers.handler as handler
import backend.models.models as models
import backend.mysql.models as mysql_models
from backend.mysql.mysql import DatabaseClient
import backend.utils.vars as gb
from sqlalchemy.orm import Session

class myTest(unittest.TestCase):

    def create_dino(self):
        #primero llamar al metodo create del hanlder pasandole el objeto
        #llamar al metodo getdinos para ver si existe
        #self.assertTrue(dinosaurioNuevoBD)
        newDino=["Prueba", "Ane",23,4242,False,False,1]
        handler.create_dinosaur(newDino)
        dinos=handler.get_dinos(self)
        self.assertTrue(newDino)