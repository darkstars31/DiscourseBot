from perlin import PerlinNoiseFactory

class WorldBuilder:

    def __init__(self):
        self.worldSize = 40
        self.terrianMap = [[0 for x in range(self.worldSize)] for y in range(self.worldSize)]
        self.pnf = PerlinNoiseFactory(2,octaves=5, tile=(0,0))

    def buildWorld(self):
        for i in range(self.worldSize):
            for j in range(self.worldSize):
               self.terrianMap[i][j] = round(self.pnf(i/self.worldSize,j/self.worldSize), 5)
        for i in range(self.worldSize):
            print("\n")
            for j in range(self.worldSize):
               print(self.terrianMap[i][j], end="")
        print()
        for i in range(self.worldSize):
            print("\n")
            for j in range(self.worldSize):
                if self.terrianMap[i][j] > 0:
                    print("x", end="")
                else:
                    print( " ", end="")
