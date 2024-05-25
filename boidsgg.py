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

n = 5
boids = []

for _ in range(n):
    boid = Boid(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
    boids.append(boid)


def update_positions(boids):
    for i in range(n):
        v1x, v1y = rule1(boids, n, i)
        v2x, v2y = rule2(boids, n, i)
        v3x, v3y = rule3(boids, n, i)

        boids[i].velocityX += (v1x + v2x + v3x)
        boids[i].velocityY += (v1y + v2y + v3y)

        boids[i].x += boids[i].velocityX
        boids[i].y += boids[i].velocityY


def rule1(boids, n, i):
    totalx = sum(boid.x for boid in boids) - boids[i].x
    totaly = sum(boid.y for boid in boids) - boids[i].y
    totalPCX = ((totalx / (n - 1) - boids[i].x) / 100)
    totalPCY = ((totaly / (n - 1) - boids[i].y) / 100)

    return totalPCX, totalPCY


def rule2(boids, n, i):
    Xc = 0
    Yc = 0
    for j in range(n):
        if i != j:
            distance = math.sqrt((boids[i].x - boids[j].x) ** 2 + (boids[i].y - boids[j].y) ** 2)
            if abs(distance) < 100:
                Xc -= boids[j].x - boids[i].x
                Yc -= boids[j].y - boids[i].y

    return Xc, Yc


def rule3(boids, n, i):
    totalVx = sum(boid.velocityX for boid in boids) - boids[i].velocityX
    totalVy = sum(boid.velocityY for boid in boids) - boids[i].velocityY
    totalVx = (totalVx / (n - 1) - boids[i].velocityX) / 8
    totalVy = (totalVy / (n - 1) - boids[i].velocityY) / 8

    return totalVx, totalVy


def animate(frame):
    update_positions(boids)
    plt.cla()
    xPoints = [boid.x for boid in boids]
    yPoints = [boid.y for boid in boids]
    plt.plot(xPoints, yPoints, 'bo')
    plt.xlim(0, 100)
    plt.ylim(0, 100)


fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=10, interval=1200)

plt.show()
