from PIL import Image


class Utils:
    @staticmethod
    def convergeRelativeCoordinateToAbsoultCoordinates(origin_width, origin_height, center_x, center_y, width, height):
        x1 = (origin_width * center_x) - (origin_width * width) / 2
        x2 = (origin_width * center_x) + (origin_width * width) / 2
        y1 = (origin_height * center_y) - (origin_width * height) / 2
        y2 = (origin_height * center_y) + (origin_width * height) / 2
        return x1, y1, x2, y2
    pass

    @staticmethod
    def getAllClassesAndCoordinates(origin_width, origin_height, result):
        object_list = []
        objects = result[0]['objects']
        for item in objects:
            object_list_item = {}
            object_list_item['class_id'] = item['class_id']
            object_list_item['class'] = item['name']
            object_list_item['relative_coordinates'] = Utils.convergeRelativeCoordinateToAbsoultCoordinates(
                origin_width, origin_height, item['relative_coordinates']['center_x'], item['relative_coordinates']['center_y'], item['relative_coordinates']['width'], item['relative_coordinates']['height'])
            object_list_item['result_text'] = ''
            object_list.append(object_list_item)
            pass
        return object_list
    pass

    @staticmethod
    def cropImage(image, x1, y1, x2, y2):
        cropped_image = image.crop((x1, y1, x2, y2))
        return cropped_image
