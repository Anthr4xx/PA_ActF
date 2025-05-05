from enum import Enum

class Direction(Enum):
    Static = "Static"
    Left = "Left"
    Right = "Right"
    Up = "Up"
    Down = "Down"


class MovementDirection(Enum):
    Horizontal = "Horizontal"
    Vertical = "Vertical"


class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        print(f"Rendering at {self.x},{self.y}")

    def __str__(self):
        return f"GameObject at {self.x},{self.y}"


class MovableObject(GameObject):
    def __init__(self, x, y, speed, movement_direction):
        super().__init__(x, y)
        self.speed = speed
        self.movement_direction = movement_direction
        self.direction = Direction.Static

    def handle_input(self, direction):
        if self.movement_direction == MovementDirection.Horizontal and direction in [Direction.Left, Direction.Right, Direction.Static]:
            self.direction = direction
        elif self.movement_direction == MovementDirection.Vertical and direction in [Direction.Up, Direction.Down, Direction.Static]:
            self.direction = direction
        else:
            print(f"Invalid movement: {direction} for {self.movement_direction}")

    def update(self, delta_time):
        if self.direction == Direction.Left:
            self.x -= self.speed * delta_time
        elif self.direction == Direction.Right:
            self.x += self.speed * delta_time
        elif self.direction == Direction.Up:
            self.y -= self.speed * delta_time
        elif self.direction == Direction.Down:
            self.y += self.speed * delta_time

    def __str__(self):
        return (f"{super().__str__()}  Moving {self.movement_direction} "
                f"{self.direction} at {self.speed}")


class Projectile(MovableObject):
    def __init__(self, x, y, speed, coalition):
        super().__init__(x, y, speed, MovementDirection.Vertical)
        self.coalition = coalition
        self.direction = Direction.Down  # Default direction for projectiles

    def __str__(self):
        return (f"Projectile {self.coalition} {super().__str__()}")


class Ship(MovableObject):
    def __init__(self, x, y, speed, coalition):
        super().__init__(x, y, speed, MovementDirection.Horizontal)
        self.coalition = coalition
        self.projectiles = []

    def fire(self):
        projectile = Projectile(self.x, self.y + 100, 10, self.coalition) #Projectil no hace spawn en la nave, +100 para desplazar un poco este spawn.
        self.projectiles.append(projectile)

    def update(self, delta_time):
        super().update(delta_time)
        for proj in self.projectiles:
            proj.update(delta_time)

    def __str__(self):
        ship_str = (f"Ship {self.coalition} {super().__str__()}")
        if self.projectiles:
            proj_strs = [str(proj) for proj in self.projectiles]
            return ship_str + " , Fired " + " | ".join(proj_strs)
        return ship_str




# Código de prueba
if __name__ == "__main__":
    go = GameObject(400, 200)
    print(go)

    mo = MovableObject(200, 200, 4, MovementDirection.Vertical)
    print(mo)

    ship = Ship(300, 300, 5, "Friend")
    print(ship)

    ship.handle_input(Direction.Left)
    ship.fire()
    ship.update(10)

    print(ship)
