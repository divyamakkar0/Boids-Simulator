import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import math


class Boid:
    def __init__(self, x, y, velocityX, velocityY):
        self.x = x
        self.y = y
        self.velocityX = velocityX
        self.velocityY = velocityY

n = 10
boids = []
xPoints = []
yPoints = []
velocitiesX = []
velocitiesY = []

for boid in range(n):
    boid = Boid(random.randint(0,9), random.randint(0,9), 0,0)
    boids.append(boid)
    xPoints.append(boid.x)
    yPoints.append(boid.y)
    
    velocitiesX.append(boid.velocityX)
    velocitiesY.append(boid.velocityY)



def NewPosition(xPoints, yPoints, velocitiesX, velocitiesY, n):
    for boid in range(n):
        v1x,v1y = rule1(xPoints, yPoints, n, boid)
        v2x, v2y = rule2(xPoints, yPoints, n, boid)
        v3x, v3y = rule3(velocitiesX, velocitiesY, n, boid)
        
        velocitiesX[boid] += v1x+v2x+v3x
        velocitiesY[boid] += v1y + v2y + v3y
        boids[boid].velocityX = (velocitiesX[boid])
        boids[boid].velocityY = (velocitiesY[boid])

        xPoints[boid] += velocitiesX[boid]
        yPoints[boid] += velocitiesY[boid]
                
        boids[boid].x = xPoints[boid]
        boids[boid].y = yPoints[boid]
    
    

def rule1(xPoints, yPoints, n, i):
    totalx = sum(xPoints) - xPoints[i]
    totaly = sum(yPoints) - yPoints[i]
    totalPCX = ((totalx / (n-1)  - xPoints[i])/100)
    totalPCY = ((totaly / (n-1) - yPoints[i])/100)
    
    return (totalPCX, totalPCY)

def rule2(xPoints, yPoints, n, i):
    Xc = 0
    Yc = 0
    for j in range(n):
        if i is not j:
            distance = math.sqrt((xPoints[i] - xPoints[j])**2 + (yPoints[i] - yPoints[j])**2)
            if abs(distance) < 100:
                Xc -= (xPoints[j] - xPoints[i])
                Yc -= (yPoints[j] - yPoints[i])

    return (Xc , Yc )

def rule3(velocitiesX, velocitiesY, n, i):
    totalVx = sum(velocitiesX) - velocitiesX[i]
    totalVx = ((totalVx / (n-1) )- velocitiesX[i])/8
    totalVy = sum(velocitiesY) - velocitiesY[i]
    totalVy = ((totalVy / (n-1)) - velocitiesY[i])/8
    
    return (totalVx, totalVy)


fig,ax = plt.subplots()


def animate(num):
    NewPosition(xPoints, yPoints, velocitiesX, velocitiesY, n)
    xPos = [i.x for i in boids]
    yPos = [i.y for i in boids]
    # print(xPos)
    ax.clear()
    ax.plot(xPos, yPos, 'bo')
    rang = 7500
    ax.set_xlim(-rang, rang)
    ax.set_ylim(-rang, rang)


ani = animation.FuncAnimation(fig, animate, frames=5000, interval=100)
plt.show()

