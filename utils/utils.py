class utils:
    @staticmethod
    def convergeRelativeCoordinateToAbsoultCoordinates(origin_width, origin_height, center_x, center_y, width, height):
        x1 = (origin_width * center_x) - (origin_width * width) / 2
        x2 = (origin_width * center_x) + (origin_width * width) / 2
        y1 = (origin_height * center_y) - (origin_width * height) / 2
        y2 = (origin_height * center_y) + (origin_width * height) / 2
        return x1, x2, y1, y2
    pass
