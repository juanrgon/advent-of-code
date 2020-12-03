import os.path
from collections import defaultdict

COM = "COM"
SAN = "SAN"
YOU = "YOU"

INFINITY = float("inf")


def main():
    print("Solution to Part 1: " + _part_1())
    print("Solution to Part 2: " + _part_2())


class Planet(object):
    def __init__(self):
        self.primary = None
        self.satellites = []

    def distance_to_planets_primary(self, planet, exclude_planet_from_search=None):
        if self.primary and self.primary == planet.primary:
            return 0

        if planet.primary in self.satellites:
            return 0

        for satellite in self.satellites:
            if satellite == exclude_planet_from_search:
                continue

            distance = satellite.distance_to_planets_primary(
                planet, exclude_planet_from_search=self
            )
            if distance != INFINITY:
                return distance + 1

        if self.primary != exclude_planet_from_search:
            return (
                self.primary.distance_to_planets_primary(
                    planet, exclude_planet_from_search=self
                )
                + 1
            )

        return INFINITY

    def orbits(self):
        orbits = 0
        for satellite in self.satellites:
            orbits += satellite._system_count() + satellite.orbits()
        return orbits

    def trap_in_orbit(self, planet):
        self.satellites.append(planet)
        planet.primary = self

    def _system_count(self):
        count = 1
        for satellite in self.satellites:
            count += satellite._system_count()
        return count


def _planets():
    planets = defaultdict(Planet)
    with open(os.path.join(os.path.abspath("."), "input")) as f:
        for orbit in f.readlines():
            planet_name, satellite_name = orbit.strip().split(")")
            planets[planet_name].trap_in_orbit(planets[satellite_name])
    return planets


def _part_1():
    com = _planets()[COM]
    return str(com.orbits())


def _part_2():
    planets = _planets()
    you = planets[YOU]
    santa = planets[SAN]
    return str(you.distance_to_planets_primary(santa))


if __name__ == "__main__":
    main()
