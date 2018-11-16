import unittest

Product_Info = __import__("Product_Info")
Service_Info = __import__("Service_Info")


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Product_Info))
suite.addTests(loader.loadTestsFromModule(Service_Info))



runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
