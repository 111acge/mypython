# coding= utf-8
# author: FFFYZ
# date: 2019/8/15

import pygame, sys, time, random
from pygame.locals import *

# 定义颜色变量
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)
headColour = pygame.Color(0, 119, 255)


# 定义gameOver函数
def gameOver(playSurface):
    gameOverFont = pygame.font.SysFont('arial', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()
    sys.exit()


# 定义main函数
def main():
    # 初始化pygame
    pygame.init()
    # 定义一个变量用来控制游戏速度
    fpsClock = pygame.time.Clock()
    # 创建pygame显示层
    playSurface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('贪吃蛇')

    # 初始化变量
    snakePosition = [100, 100]
    # 列表元素个数=蛇长度
    snakeSegments = [[100, 100], [80, 100], [60, 100]]
    foodPosition = [300, 300]
    foodFlag = 1  # 食物标志位，1表示没被吃
    direction = 'right'
    changeDirection = direction
    while True:
        # 监听pygame按键事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # 判断键盘事件
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # 与非逻辑判断是否输入了反方向
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection
        # 根据方向移动蛇头的坐标
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20
        # 增加蛇的长度
        snakeSegments.insert(0, list(snakePosition))
        # 判断是否吃掉了食物
        if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
            foodFlag = 0
        else:
            snakeSegments.pop()
        # 如果吃掉食物，则重新生成食物,生成的食物不能与蛇重合
        if foodFlag == 0:
            while foodPosition in snakeSegments:
                x = random.randrange(1, 40)
                y = random.randrange(1, 30)
                foodPosition = [int(x * 20), int(y * 20)]
        foodFlag = 1
        # 绘制pygame显示层
        playSurface.fill(blackColour)
        # 遍历，把蛇和食物画出来
        for position in snakeSegments:
            pygame.draw.rect(playSurface, whiteColour, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playSurface, headColour, Rect(snakePosition[0], snakePosition[1], 20, 20))
            pygame.draw.rect(playSurface, redColour, Rect(foodPosition[0], foodPosition[1], 20, 20))

        # 刷新pygame显示层
        pygame.display.flip()
        # 判断是否死亡，分为撞墙和撞自己
        if snakePosition[0] > 780 or snakePosition[0] < 0:
            gameOver(playSurface)
        if snakePosition[1] > 580 or snakePosition[1] < 0:
            gameOver(playSurface)
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameOver(playSurface)
        # 控制游戏速度
        fpsClock.tick(10)


if __name__ == "__main__":
    main()
