import pygame
import random

# Инициализация Pygame
pygame.init()

# Установим размеры экрана
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Размер клетки змейки
BLOCK_SIZE = 20

# Начальные координаты змейки и еды
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_body = [(snake_x, snake_y)]
snake_direction = 'RIGHT'

food_x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
food_y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

# Скорость игры (FPS)
speed = 10

# Игровая информация
score = 0
level = 1

# Функция для отображения текста
def display_text(text, x, y, font_size=30, color=WHITE):
    font = pygame.font.SysFont("bahnschrift", font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Проверка на столкновение с границами экрана
def check_border_collision():
    global snake_x, snake_y
    if snake_x < 0:
        snake_x = WIDTH - BLOCK_SIZE  # Выход слева, появляется справа
    elif snake_x >= WIDTH:
        snake_x = 0  # Выход справа, появляется слева
    elif snake_y < 0:
        snake_y = HEIGHT - BLOCK_SIZE  # Выход сверху, появляется снизу
    elif snake_y >= HEIGHT:
        snake_y = 0  # Выход снизу, появляется сверху

# Проверка на столкновение с телом змейки
def check_self_collision():
    global snake_body
    if (snake_x, snake_y) in snake_body[1:]:
        return True
    return False

# Генерация новой позиции для еды, чтобы она не появлялась на стенах или теле змейки
def generate_food():
    global food_x, food_y
    while True:
        food_x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (food_x, food_y) not in snake_body:
            break

# Функция для отображения "Game Over"
def game_over():
    font = pygame.font.SysFont("bahnschrift", 50)
    game_over_text = font.render("Game Over", True, RED)
    screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 3))

    font_small = pygame.font.SysFont("bahnschrift", 30)
    restart_text = font_small.render("Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(restart_text, (WIDTH // 4, HEIGHT // 2 + 50))

# Основной игровой цикл
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Обработка ввода с клавиатуры для управления змейкой
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'
            elif event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'

    # Обновление координат змейки
    if snake_direction == 'LEFT':
        snake_x -= BLOCK_SIZE
    elif snake_direction == 'RIGHT':
        snake_x += BLOCK_SIZE
    elif snake_direction == 'UP':
        snake_y -= BLOCK_SIZE
    elif snake_direction == 'DOWN':
        snake_y += BLOCK_SIZE

    # Проверка на столкновение с границами экрана или своим телом
    check_border_collision()
    if check_self_collision():
        done = True

    # Добавление нового сегмента тела, если змейка съела еду
    snake_body.insert(0, (snake_x, snake_y))

    if snake_x == food_x and snake_y == food_y:
        score += 1
        if score % 3 == 0:  # Увеличение уровня после каждого 3-го съеденного яблока
            level += 1
            speed += 2  # Увеличиваем скорость на 2, когда уровень растет
        generate_food()  # Генерируем новую еду
    else:
        snake_body.pop()  # Убираем последний сегмент змейки, если еда не съедена

    # Отображение фона, змейки и еды
    screen.fill(BLACK)
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.draw.rect(screen, RED, pygame.Rect(food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

    # Отображение текущего счета и уровня
    display_text(f"Score: {score}", 10, 10)
    display_text(f"Level: {level}", WIDTH - 100, 10)

    pygame.display.flip()

    # Устанавливаем скорость игры (FPS)
    clock.tick(speed)

    # Если игра окончена, отображаем "Game Over" и ожидаем нажатие клавиш
    if done:
        game_over()
        pygame.display.flip()

        # Ожидаем, пока пользователь нажмет клавишу для перезапуска или выхода
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_input = False
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Перезапускаем игру
                        done = False
                        snake_x = WIDTH // 2
                        snake_y = HEIGHT // 2
                        snake_body = [(snake_x, snake_y)]
                        snake_direction = 'RIGHT'
                        food_x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
                        food_y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
                        score = 0
                        level = 1
                        speed = 10
                    elif event.key == pygame.K_q:
                        # Выход из игры
                        waiting_for_input = False
                        done = True

# Закрытие Pygame
pygame.quit()
