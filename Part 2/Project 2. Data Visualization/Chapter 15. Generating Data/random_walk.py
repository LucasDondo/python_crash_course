from random import choice

class RandomWalk:
    def __init__(self, num_points=5_000):
        ''' Initialize attributes of a random walk. '''

        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def walk(self):
        ''' Walk. '''

        while len(self.x_values) < self.num_points:
            x_step = self._get_step()
            y_step = self._get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def _get_step(self):
        ''' Decide how far and in what direction to go. '''

        direction = choice([-1, 1])
        distance  = choice([0, 1, 2, 3, 4])
        step      = direction * distance

        return step