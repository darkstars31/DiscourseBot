import random

biomes = []
rooms = []

roomTypes = ["hallway","bedroom","master bed room","kitchen","dungeon","cellar","annex"]
roomDescriptions = [{
    "hall"
}]

random.seed()

class StoryBuilder:

    def createArea():
        areaSize = random.randint(12,18)
        areaBiome