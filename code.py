import pygame
import sys
import random
import time

# Инициализация Pygame
pygame.init()
font = pygame.font.Font(None, 24)


# Получение метода инициализации мира
def get_input_method():
    method = input(
        "Желаете ввести живые клетки вручную (введите 'в') или сгенерировать случайно (введите 'с')? ").lower()
    return method


# Получение положительного целого числа
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Введите целое, положительное число.")
        except ValueError:
            print("Введите целое, положительное число.")


# Инициализация мира
def initialize_world(length, method='с'):
    if method == 'в':
        return user_define_world(length)
    else:
        return [random.choice([0, 1]) for _ in range(length)]


# Ввод пользователем живых клеток
def user_define_world(length):
    world = [0] * length
    initial_cells = input(f"Введите позиции живых клеток, разделенные пробелом (индексация с 1, макс. {length}): ")
    for i in map(int, initial_cells.split()):
        if 1 <= i <= length:
            world[i - 1] = 1
        else:
            print(f"Индекс {i} вне допустимого диапазона. Пропускаем.")
    return world


# Генерация следующего поколения
def next_generation(current_gen):
    length = len(current_gen)
    new_gen = [0] * length
    for i in range(length):
        neighbors = current_gen[i - 1] + current_gen[(i + 1) % length]
        if neighbors == 1:
            new_gen[i] = 1
    return new_gen


# Отрисовка мира
def draw_world(world, screen, cell_size):
    for i, cell in enumerate(world):
        color = (69, 123, 157) if cell == 1 else (241, 250, 238)
        pygame.draw.rect(screen, color, (i * cell_size, 150, cell_size, cell_size))


# Отрисовка интерфейса пользователя
def draw_ui(screen, generations, population, running, speed, screen_width):
    if not running:
        pygame.draw.rect(screen, (230, 57, 70), pygame.Rect(screen_width // 2 - 40, 10, 80, 30))
        text = font.render("Начать", True, (241, 250, 238))
        screen.blit(text, (screen_width // 2 - 20, 15))

    timer_text = font.render(f"Поколений: {generations}", True, (0, 0, 0))
    population_text = font.render(f"Население: {population}", True, (0, 0, 0))
    screen.blit(timer_text, (10, 50))
    screen.blit(population_text, (10, 70))


# Отрисовка ползунка скорости
def draw_speed_slider(screen, speed, screen_width):
    slider_rect = pygame.Rect(10, 120, screen_width - 20, 10)
    handle_position = 10 + int(speed * (screen_width - 50) / 100)
    handle_rect = pygame.Rect(handle_position, 115, 20, 20)
    pygame.draw.rect(screen, (29, 53, 87), slider_rect)
    pygame.draw.rect(screen, (230, 57, 70), handle_rect)


def main():
    length = get_positive_integer("Введите длину мира: ")
    cell_size = 20
    screen_width = length * cell_size
    screen_height = 200 + cell_size

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Game of Life 1d')

    method = get_input_method()
    world = initialize_world(length, method)
    generations = 0
    running = False
    speed = 50
    dragging = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if screen_width // 2 - 40 <= mouse_x <= screen_width // 2 + 40 and 10 <= mouse_y <= 40 and not running:
                    running = True
                elif 10 <= mouse_x <= screen_width - 10 and 115 <= mouse_y <= 135:
                    dragging = True
                    speed = int((mouse_x - 10) / (screen_width - 50) * 100)
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            elif event.type == pygame.MOUSEMOTION and dragging:
                mouse_x, mouse_y = event.pos
                speed = max(0, min(100, int((mouse_x - 10) / (screen_width - 50) * 100)))

        screen.fill((241, 250, 238))
        draw_world(world, screen, cell_size)
        population = sum(world)
        draw_ui(screen, generations, population, running, speed, screen_width)
        draw_speed_slider(screen, speed, screen_width)
        pygame.display.flip()

        if running:
            world = next_generation(world)
            generations += 1
            time.sleep(max(0.1, 2 - (speed / 50)))


if __name__ == "__main__":
    main()
