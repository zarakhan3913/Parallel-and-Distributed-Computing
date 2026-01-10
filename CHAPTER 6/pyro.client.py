import Pyro4

# Locate the object by logical name
calculator = Pyro4.Proxy("PYRONAME:example.calculator")

# Call methods remotely
print("2 + 3 =", calculator.add(2, 3))
print("4 * 5 =", calculator.multiply(4, 5))
