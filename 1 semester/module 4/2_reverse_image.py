def reverse_image(image):
    return [[abs(1 - pixel) for pixel in row] for row in image]

def reverse_image_recursive(image):
    if not image:
        return image
    first_row = [abs(1 - pixel) for pixel in image[0]]
    return [first_row] + reverse_image_recursive(image[1:])

# Пример входных данных
input_image = [
    [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
    ],
    [
    [1, 1, 1],
    [0, 0, 0]
    ],
    [
    [1, 0, 0],
    [1, 0, 0]
    ]
]
for index, item in enumerate(input_image):
    # Вывод результатов
    print("Пример №", index + 1)
    print("Обычный метод:", reverse_image(item))
    print("Рекурсивный метод:", reverse_image_recursive(item))