from PIL import Image
import os
import shutil

def save_to_different_folder():
    # Открываем изображение
    image_path = "путь/к/исходному/изображению.jpg"  # Заменяем на свой путь 
    image = Image.open(image_path)
    
    # Преобразуем в черно-белое
    bw_image = image.convert('L')
    
    # Путь к НОВОЙ папке для сохранения
    new_folder = "путь/к/папке/куда/сохранить"  # Выбираем новый путь для сохранения
    
    
    
    # Сохраняем в новую папку
    new_path = os.path.join(new_folder, "имя_нового_файла.jpg")  # По желанию можно переименовать
    bw_image.save(new_path)
    
    print(f" Черно-белое фото сохранено в: {new_path}")

save_to_different_folder()