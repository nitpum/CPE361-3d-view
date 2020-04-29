class Surface:
    edges = []

    def __init__(self, edgesList):
        self.edges = edgesList
    def is_point_in_surface(self, point):
