from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
import random
import math


loadPrcFile("config/config.prc")

class Mygame(ShowBase):
    def __init__(self):
        super().__init__()

        #self.disableMouse()
        self.boxs =[]
        x=-50
        for i in range(100):
            self.boxs.append(self.loader.loadModel('models/box'))
        for i in self.boxs:
            x=x+1
            i.setPos(x*1.3, 10, 0)
            i.reparentTo(self.render)

        self.panda = self.loader.loadModel('models/panda')
        self.panda.setPos(-1, 10,1)
        self.panda.setScale(0.2, 0.2, 0.2)
        self.panda.reparentTo(self.render)

        self.x = 0
        self.speed = 0
        self.angle = 0
        self.taskMgr.add(self.update, "update")

    def update(self, task):

        self.panda.setH(self.angle)
        for i in self.boxs:
            i.setHpr(self.angle, 0, self.angle)
        self.angle += 1
        #self.x += self.speed *dt

        return task.cont





game = Mygame()


game.run()