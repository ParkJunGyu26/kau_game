from PIL import Image, ImageDraw, ImageFont


class Keeper:
    def __init__(self, position, background):
        self.position = position
        self.shape = Image.open("Keeper.gif").convert("RGBA")  # 경로 업데이트
        self.shape = self.shape.resize((100, 100))
        background = background.crop((position[0], position[1], position[0] + 100, position[1] + 100))
        self.shape = Image.alpha_composite(background, self.shape)
        
    def left(self):  # 왼쪽으로 움직이는 경우
        k_position = list(self.position)
        k_position[0] -= 3
        self.position = tuple(k_position)

    def right(self):  # 오른쪽으로 움직이는 경우
        k_position = list(self.position)
        k_position[0] += 3
        self.position = tuple(k_position)