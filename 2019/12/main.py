class Moon():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.velocity = (0, 0, 0)

    def positions(self):
        return self.x, self.y, self.z
    
    def update_positions(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.z += self.velocity[2]

    def update_velocity(self, x, y, z):
        ox, oy, oz = self.velocity
        self.velocity = (ox+x, oy+y, oz+z)


def read_input(file):
    moons = []
    with open(file) as f:
        for r in f.readlines():
            x, y, z = map(str.strip, r.strip().split(','))
            x = int(x[3:])
            y = int(y[2:])
            z = int(z[2:-1])
            moons.append(Moon(x, y, z))
    return moons


def part1():
    moons = read_input("input")
    for _ in range(1000):
        for m in moons:
            other_moons = moons[:]
            other_moons.pop(moons.index(m))
            for o in other_moons:
                m_x, m_y, m_z = m.positions()
                o_x, o_y, o_z = o.positions()
                
                if m_x > o_x:
                    v_x = -1
                elif m_x < o_x:
                    v_x = 1
                else:
                    v_x = 0
                    
                if m_y > o_y:
                    v_y = -1
                elif m_y < o_y:
                    v_y = 1
                else:
                    v_y = 0
                    
                if m_z > o_z:
                    v_z = -1
                elif m_z < o_z:
                    v_z = 1
                else:
                    v_z = 0
                m.update_velocity(v_x, v_y, v_z)
        for m in moons:
            m.update_positions()
    
    calc = 0
    for m in moons:
        pot = sum(map(abs, m.positions()))
        kin = sum(map(abs, m.velocity))
        calc += pot*kin

    print(calc)


part1()


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)
    

def part2():
    moons = read_input("input")
    
    x = y = z = False
    for i in range(1, 1000000):
        for m in moons:
            other_moons = moons[:]
            other_moons.pop(moons.index(m))
            for o in other_moons:
                m_x, m_y, m_z = m.positions()
                o_x, o_y, o_z = o.positions()
                
                if m_x > o_x:
                    v_x = -1
                elif m_x < o_x:
                    v_x = 1
                else:
                    v_x = 0
                    
                if m_y > o_y:
                    v_y = -1
                elif m_y < o_y:
                    v_y = 1
                else:
                    v_y = 0
                    
                if m_z > o_z:
                    v_z = -1
                elif m_z < o_z:
                    v_z = 1
                else:
                    v_z = 0
                m.update_velocity(v_x, v_y, v_z)
        for m in moons:
            m.update_positions()
        
        vees = [m.velocity for m in moons]
        if not x and 0 == vees[0][0] == vees[1][0] == vees[2][0] == vees[3][0]:
            x = i

        if not y and 0 == vees[0][1] == vees[1][1] == vees[2][1] == vees[3][1]:
            y = i

        if not z and 0 == vees[0][2] == vees[1][2] == vees[2][2] == vees[3][2]:
            z = i

        if x and y and z:
            break

    print(lcm(lcm(x, y), z) * 2)


part2()
