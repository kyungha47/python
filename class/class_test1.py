class Annie:
    def __init__(self, **kwargs):
        self.health = kwargs["health"]
        self.mana = kwargs["mana"]
        self.ap = kwargs["ability_power"]

    def tibbers(self):
        value = self.ap * 0.65 + 400
        print(f"티버: 피해량 {value}")

health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()