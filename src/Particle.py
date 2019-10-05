import random
class Particle(object):
    """docstring for Particle."""
    def __init__(self, dimension):
        super(Particle, self).__init__()
        self.dimension = dimension
        self.velocity = [0] * dimension
        self.position = [0] * dimension
        rangeP = 20
        self.bestIndividualPosition = self.position[:]
        self.bestIndividualScore = 99999999
        self.bestGlobalPosition = self.position[:]
        self.bestGlobalScore = 99999999

        self.inertiaCoefficient = 0.5
        self.socialFactor = 0.9
        self.cognitiveFactor = 0.5

        for i in range(dimension):
            self.velocity[i] = random.random()*rangeP - rangeP/2
            self.position[i] = random.random()*rangeP - rangeP/2


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
        for i in range(self.dimension):
            self.position[i] = self.position[i] + self.velocity[i]
    def updateIndividual(self, position, score):
        self.bestIndividualScore = score
        self.bestIndividualPosition = position[:]
    def updateGlobal(self, position, score):
        self.bestGlobalScore = score
        self.bestGlobalPosition = position[:]

    def printParticle(self):
        print(self.__dict__)
