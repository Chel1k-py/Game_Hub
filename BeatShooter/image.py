import pygame
import os

# Пути к файлам
input_path = "img/score.png"
output_path = "img/score_scaled.png"

# Проверяем, что файл существует
if not os.path.exists(input_path):
    raise FileNotFoundError(f"Файл не найден: {input_path}")

# Инициализируем Pygame и создаём временный дисплей
pygame.init()
pygame.display.set_mode((1, 1))  # нужно для convert_alpha()

# Загружаем изображение с поддержкой прозрачности
original_image = pygame.image.load(input_path).convert_alpha()

# Увеличиваем в 4 раза (без сглаживания)
scale_factor = 3
new_size = (
    original_image.get_width() * scale_factor,
    original_image.get_height() * scale_factor
)
scaled_image = pygame.transform.scale(original_image, new_size)

# Сохраняем увеличенное изображение
pygame.image.save(scaled_image, output_path)

pygame.quit()

print(f"✅ Изображение увеличено и сохранено: {output_path}")
