from Particle import Particle
import math
import random
def aimFunc(particle):
    x = particle.position[0]
    y = particle.position[1]

    return x*x+y*y

def main():
    dimension = 2
    numParticles = 5
    particles = []
    maxInteractions = 100
    numInteractions = 0
    gBestScore = 99999999999
    for p in range(numParticles):
        particles.append(Particle(dimension,p))
    for p in particles:
        pScore = aimFunc(p)
        if pScore < gBestScore:
            gBestScore = pScore
    while numInteractions < maxInteractions:
        for p in particles:
            p.updateVelocity()
            p.updatePosition()
            newScore = aimFunc(p)

            if newScore < p.bestIndividualScore or p.bestIndividualScore == None:
                p.bestIndividualScore = newScore
                p.bestIndividualPosition = p.position
                if newScore < gBestScore:
                    gBestScore = newScore
                    p.bestGlobalScore = newScore
                    p.bestGlobalPosition = p.position
            print(p.id,p.position,aimFunc(p))
        numInteractions += 1
    print(gBestScore)
if __name__ == '__main__':
    main()
