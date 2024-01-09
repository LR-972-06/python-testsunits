import unittest

# Importer la classe Calcul
from calcul import Calcul

# Classe de tests héritant de unittest.TestCase
class TestCalcul(unittest.TestCase):

    # Méthode de configuration exécutée avant chaque test
    def setUp(self):
        # Initialisation des ressources nécessaires pour les tests
        self.calc = Calcul()
    
    # Test d'addition
    def test_additionner(self):
        resultat = self.calc.additionner(3, 5)
        # Vérifier si le résultat est égal à 8
        self.assertEqual(resultat, 8)

    # Test de soustraction
    def test_soustraire(self):
        resultat = self.calc.soustraire(10, 4)
        # Vérifier si le résultat est égal à 6
        self.assertEqual(resultat, 6)

    # Test de multiplication
    def test_multiplier(self):
        resultat = self.calc.multiplier(6, 6)
        # Vérifier si le résultat est égal à 36
        self.assertEqual(resultat, 36)

    # Test de division
    def test_diviser(self):
        resultat = self.calc.diviser(9, 3)
        # Vérifier si le résultat est égal à 3
        self.assertEqual(resultat, 3)

    # Test de division par zéro
    def test_diviserZero(self):
        resultat = self.calc.diviser(72, 0)
        # Vérifier si la division par 0 est gérée
        self.assertEqual(resultat,"Division par zéro impossible")
    
    # Test de division par zéro - exception
    def test_diviser_par_zero(self):
        with self.assertRaises(ZeroDivisionError, msg="Division par zéro impossible"):
                    self.calc.diviser(5, 0)

# Exécuter les tests si le script est exécuté directement
if __name__ == '__main__':
    unittest.main()




