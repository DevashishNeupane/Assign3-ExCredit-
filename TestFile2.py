import unittest

Product_Info = __import__("(EC) Product CSV")
Service_Info = __import__("(EC) Service CSV")


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Product_Info))
suite.addTests(loader.loadTestsFromModule(Service_Info))



runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
