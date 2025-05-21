from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    try:
        # Öffne das Bild
        img = Image.open(input_path)
        
        # Konvertiere zu RGB falls nötig
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Speichere das komprimierte Bild
        img.save(output_path, optimize=True, quality=quality)
        
        # Berechne die Kompressionsrate
        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        print(f"Komprimiert: {input_path}")
        print(f"Original: {original_size/1024:.1f}KB")
        print(f"Komprimiert: {compressed_size/1024:.1f}KB")
        print(f"Kompressionsrate: {compression_ratio:.1f}%\n")
        
    except Exception as e:
        print(f"Fehler bei {input_path}: {str(e)}")

def main():
    # Erstelle einen temporären Ordner für die komprimierten Bilder
    if not os.path.exists('static/compressed'):
        os.makedirs('static/compressed')
    
    # Liste der zu komprimierenden Bilder
    images = [
        'IT-Safety_Cat.png',
        'IT-Solution_Cat.png',
        'IT-Support_Cat.png',
        'My_Logo.PNG',
        'ich.jpg'
    ]
    
    # Komprimiere jedes Bild
    for image in images:
        input_path = os.path.join('static', image)
        output_path = os.path.join('static/compressed', image)
        compress_image(input_path, output_path)

if __name__ == "__main__":
    main() 