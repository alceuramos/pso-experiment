from Particle import Particle
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
    for i in range(numParticles):
        p = Particle(dimension)
        particles.append(p)
        pScore = aimFunc(p)
        p.updateIndividual(p.position, pScore)
        p.updateGlobal(p.position, pScore)
    while numInteractions < maxInteractions and maxError < maxScore:
        maxScore = 0
        for p in particles:
            p.updateVelocity()
            p.updatePosition()
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
    #print(maxScore)

if __name__ == '__main__':
    main()
