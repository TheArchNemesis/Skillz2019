from elf_kingdom import *
from w_location import LocationWrapper as Location
import GoblinSabotageSquad.location_calculator as location_calculator


class ElfWrapper:
    """
        this class is a wrapper for elf.
    """

    ATTACK_PORTAL_RADIUS = 1200
    DEFENSE_PORTAL_RADIUS = 1200
    MANAGEN_RADIUS = 800

    def __init__(self, elf, role):
        self.elf = elf
        self.role = role

    def get_location(self):
        return Location(self.elf.location)

    def get_x(self):
        return self.get_location().get_x()

    def get_y(self):
        return self.get_location().get_y()

    def move_to(self, location):
        self.elf.move_to(location.location)

    def act_attacker(self, enemy_castle, enemy_portals, **context):
        if self.get_location() == location_calculator.calc_attack_portal_location(enemy_castle,
                                                                                  self.ATTACK_PORTAL_RADIUS,
                                                                                  enemy_portals) and self.elf.can_build_portal():
            self.elf.build_portal()
        else:
            self.move_to(location_calculator.calc_attack_portal_location(enemy_castle, self.ATTACK_PORTAL_RADIUS,
                                                                         enemy_portals))

    def act_defender(self, castle, enemy_portals, mana_fountains):
        if self.get_location() == location_calculator.calc_defense_portal_location(self.DEFENSE_PORTAL_RADIUS,
                                                                                   castle,
                                                                                   enemy_portals,
                                                                                   mana_fountains) and self.elf.can_build_portal():
            self.elf.build_portal()
        else:
            self.move_to(
                location_calculator.calc_defense_portal_location(self.DEFENSE_PORTAL_RADIUS, castle, enemy_portals,
                                                                 mana_fountains))

    def act_mana_fountain(self, castle, enemy_castle, mana_fountains):
        if self.get_location() == location_calculator.calc_managen_location(self.MANAGEN_RADIUS, castle,
                                                                            enemy_castle,
                                                                            mana_fountains) and self.elf.can_build_mana_fountain():
            self.elf.build_mana_fountain()
        else:
            self.move_to(location_calculator.calc_managen_location(self.MANAGEN_RADIUS, castle,
                                                                   enemy_castle,
                                                                   mana_fountains))

    def act_portal(self):
        pass

    def act_cannibal(self):
        pass

    def act_destroyer(self):
        pass
