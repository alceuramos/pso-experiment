import random
class Particle(object):
    """docstring for Particle."""
    def __init__(self, dimension,id):
        super(Particle, self).__init__()
        self.id = id
        self.dimension = dimension
        self.velocity = [0] * dimension
        self.position = [0] * dimension

        for i in range(dimension):
            self.velocity[i] = random.random()*10 - 5
            self.position[i] = random.random()*10 - 5

        self.bestIndividualPosition = self.position[:]
        self.bestIndividualScore = None
        self.bestGlobalPosition = self.position[:]
        self.bestGlobalScore = None

        self.inertiaCoefficient = 0.5 #random.random()
        self.socialFactor = 0.9 #random.random()
        self.cognitiveFactor = 0.5 #random.random()

        #self.printParticle()

    def updateVelocity(self):
        for i in range(self.dimension):
            r1 = random.random()
            r2 = random.random()
            inertia =   (self.inertiaCoefficient * self.velocity[i])
            social =    (self.socialFactor * r1 * (self.bestGlobalPosition[i] - self.position[i]))
            cognitive = (self.cognitiveFactor * r2 * (self.bestIndividualPosition[i] - self.position[i]))
            self.velocity[i] =  inertia + social + cognitive
            self.velocity[i] = self.velocity[i]
    def updatePosition(self):
        #print("AQUI")
        #print(self.position)
        #print(self.velocity)
        for i in range(self.dimension):
            self.position[i] = self.position[i] + self.velocity[i]
        #print(self.position)
    def printParticle(self):
        print(self.__dict__)
