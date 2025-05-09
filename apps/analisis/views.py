import os
import base64
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from django.conf import settings
from django.shortcuts import render
from .forms import ImagenForm
from .utils import detectar_color

def index(request):
    color = None
    error = None
    form = ImagenForm()  # se define por defecto

    if request.method == 'POST':
        origen = request.POST.get("origen")

        if origen == "archivo":
            form = ImagenForm(request.POST, request.FILES)

            if form.is_valid():
                try:
                    imagen = form.cleaned_data['imagen']
                    temp_path = os.path.join(settings.MEDIA_ROOT, imagen.name)

                    with open(temp_path, 'wb+') as destino:
                        for chunk in imagen.chunks():
                            destino.write(chunk)

                    color = detectar_color(temp_path)

                    if os.path.exists(temp_path):
                        os.remove(temp_path)

                except UnidentifiedImageError:
                    error = "La imagen no pudo ser procesada. ¿Está corrupta?"
                except Exception as e:
                    error = f"Ocurrió un error al procesar la imagen: {str(e)}"
            else:
                error = "Seleccione una imagen válida."

        elif origen == "camara":
            try:
                data_url = request.POST.get('imagen_web')
                if data_url and ',' in data_url:
                    _, encoded = data_url.split(',', 1)
                    binary_data = base64.b64decode(encoded)
                    image = Image.open(BytesIO(binary_data)).convert("RGB")

                    temp_path = os.path.join(settings.MEDIA_ROOT, 'captura_web.jpg')
                    image.save(temp_path, 'JPEG')

                    color = detectar_color(temp_path)

                    if os.path.exists(temp_path):
                        os.remove(temp_path)
                else:
                    error = "La imagen capturada no es válida."

            except UnidentifiedImageError:
                error = "La imagen capturada no pudo ser procesada."
            except Exception as e:
                error = f"Ocurrió un error al procesar la captura: {str(e)}"

        else:
            error = "No se reconoció la fuente de imagen."

    return render(request, 'analisis/index.html', {
        'form': form,
        'color': color,
        'error': error
    })
