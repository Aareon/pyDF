from item import Item


class MapTile():
    """ MapTile class, generic class for a tile """
    def __init__(self, value):
        self.value = value
        self.content = []
        self.mobs = []
        self.blocked = False
        if int(self.value) == 0 or int(self.value) == 5:
            self.blocked = True

    def digTile(self, value):
        oldvalue = self.value
        self.value = value
        self.add(Item('crumbledwall', 16))


    def addMob(self, mob):
        self.mobs.append(mob)
        return self.mobs

    def removeMob(self, mob):
        self.mobs.append(mob)
        return self.mobs

    def add(self, content):
        self.content.append(content)
        return self.content

    def remove(self, content):
        self.content.remove(content)
        return self.content

    def pickup(self):
        for item in self.content:
            if item.selected:
                val = item
                self.remove(item)
                return val
        return None
