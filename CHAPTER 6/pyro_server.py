import Pyro4

# 1️⃣ Expose class so clients can call remotely
@Pyro4.expose
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

# 2️⃣ Create a Pyro daemon
daemon = Pyro4.Daemon()  # listens for incoming requests

# 3️⃣ Locate Name Server and register object
ns = Pyro4.locateNS()
uri = daemon.register(Calculator)  # register object with daemon
ns.register("example.calculator", uri)  # logical name for clients

print("Server is running. Object registered as 'example.calculator'")
daemon.requestLoop()  # keeps listening
