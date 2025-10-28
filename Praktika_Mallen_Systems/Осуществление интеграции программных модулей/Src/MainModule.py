from PIL import Image
import os
import shutil

def process_image():
    # Путь к исходному изображению
    image_path = "путь/к/твоему/исходному/изображению.jpg"  # Заменяем на свой путь
    
    # Открываем изображение
    image = Image.open(image_path)
    
    # Преобразуем в черно-белое
    bw_image = image.convert('L')
    
    # Папка с оригиналом
    original_folder = os.path.dirname(image_path)
    
    #  Имя файла без расширения
    original_filename = os.path.basename(image_path)
    name, ext = os.path.splitext(original_filename)
    
    # Создаем пути для сохранения
    original_copy_path = os.path.join(original_folder, f"{name}_original{ext}")
    bw_image_path = os.path.join(original_folder, f"{name}_black_white{ext}")
    
    # Сохраняем копию оригинальной фотографии
    image.save(original_copy_path)
    print(f" Копия оригинальной фото сохранена: {original_copy_path}")
    
    # Сохраняем черно-белую версию
    bw_image.save(bw_image_path)
    print(f" Черно-белая версия сохранена: {bw_image_path}")
    
    print(f" Обе фотографии лежат в папке: {original_folder}")

# Запускаем программу
process_image()