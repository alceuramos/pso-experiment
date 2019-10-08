from Particle import Particle
from plot import Plot
import random
def aimFunc(particle):
    x = particle.position[0]
    y = particle.position[1]

    return x*x+y*y

def main():
    dimension = 2
    numParticles = 20
    particles = []
    maxInteractions = 100
    numInteractions = 0
    maxError = 1e-8
    maxScore = 1

    plot = Plot()
    plot.startPlot()
    #p.updatePlot([1,2,3],[3,2,1],[1,2,3])

    X = []
    Y = []
    Z = []

    for i in range(numParticles):
        p = Particle(i, dimension)
        particles.append(p)
        pScore = aimFunc(p)
        p.updateIndividual(p.position, pScore)
        p.updateGlobal(p.position, pScore)
        X.append(p.position[0])
        Y.append(p.position[1])
        Z.append(aimFunc(p))
    while numInteractions < maxInteractions and maxError < maxScore:
        maxScore = 0
        for p in particles:
            p.updateVelocity()
            p.updatePosition()
            X[p.id] = p.position[0]
            Y[p.id] = p.position[1]
            Z[p.id] = aimFunc(p)
            plot.updatePlot(X,Y,Z)
            pScore = aimFunc(p)
            if pScore < p.bestIndividualScore:
                p.updateIndividual(p.position, pScore)
                if pScore < p.bestGlobalScore:
                    for adj in particles: #just update connected particles
                        adj.updateGlobal(p.position, pScore)
            #print(p.position,aimFunc(p))
            if pScore > maxScore:
                maxScore = pScore
        numInteractions += 1
        plot.updatePlot(X,Y,Z)

if __name__ == '__main__':
    main()
