""" Самая далекая планета  """

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_farthest_orbit(arr):
    S = 0
    S_max = 0
    farthest_orbit = 0
    for i in range(len(orbits)):
        S = 3.14 * orbits[i][0] * orbits[i][1]
        if orbits[i][0] != orbits[i][1] and S > S_max:
            S_max = S
            farthest_orbit = i
    return orbits[farthest_orbit]


print(*find_farthest_orbit(orbits))
