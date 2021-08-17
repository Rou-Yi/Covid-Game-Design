from _night.level_setting import level_setting


class ManaGroup:
    def __init__(self, level):
        self.max_mana = level_setting[level]['mana_value']
        self.mana = self.max_mana
        self.cd_count = 0
        self.cd_max_count = level_setting[level]['mana_recovery']

    def mana_update(self, value):
        self.mana = value

    def advance(self):
        # Restore mana with cd
        if self.cd_count >= self.cd_max_count:
            if self.mana < self.max_mana:
                self.mana += 1
                self.cd_count = 0
        else:
            self.cd_count += 1

    @property
    def mana_value(self):
        return self.mana
