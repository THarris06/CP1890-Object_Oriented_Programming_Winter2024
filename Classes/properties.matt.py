class Ninja:
    def __init__(self):
        self.name = "Arun"
        self._skill = 5
        self.__pid = 7754


    # def get_skill(self):
    #     return self._skill
    #
    # def set_skill(self, new_skill):
    #     self._skill = new_skill

    @property
    def skill(self) -> int:
        return self._skill

    @skill.setter
    def skill(self, value):
        if value < 0:
            raise ValueError("Your Ninja has no skills")
        else:
            self._skill = value

    @skill.getter
    def skill(self):
        return self._skill + 50

n = Ninja()
print(n.name)
print(n._skill)
print(n._Ninja__pid)
# print(dir(n))

# n.set_skill(100)
# # print(n.get_skill())
print(n.skill)
n.skill = 6