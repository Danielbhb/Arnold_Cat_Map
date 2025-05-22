import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def arnold_cat_map(image, iterations=1):
    if image.shape[0] != image.shape[1]:
        raise ValueError("La imagen debe ser cuadrada")
    
    size = image.shape[0]
    transformed_image = np.zeros_like(image)
    
    for i in range(size):
        for j in range(size):
            new_i, new_j = i, j  # Inicializar con las coordenadas originales
            
            # Aplicar la transformación 'iterations' veces
            for _ in range(iterations):
                new_i, new_j = (2 * new_i + new_j) % size, (new_i + new_j) % size
            
            # Copiar el valor del píxel
            if len(image.shape) == 2:
                transformed_image[new_i, new_j] = image[i, j]
            else:
                transformed_image[new_i, new_j, :] = image[i, j, :]
    
    return transformed_image

# Cargar una imagen 
image_path = 'C:\\Users\\danie\\OneDrive - Universidad Politécnica de San Luis Potosí\\2. Segundo Semestre\\Matemáticas 3\\prueba.jpeg'  # Cambia esto por la ruta de tu imagen
original_image = np.array(Image.open(image_path))

# Si la imagen no es cuadrada, la recortamos
min_dim = min(original_image.shape[0], original_image.shape[1])
square_image = original_image[:min_dim, :min_dim]

# Aplicar el mapeo de Arnold Cat
iterations = 5
transformed_image = arnold_cat_map(square_image, iterations)

# Mostrar las imágenes
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(square_image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title(f'Imagen Transformada (iteraciones={iterations})')
plt.imshow(transformed_image)
plt.axis('off')

plt.tight_layout()
plt.show()