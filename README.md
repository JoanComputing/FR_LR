# Reconocimiento de Rostros en Imágenes de Baja Resolución

## Descripción
Este proyecto aborda el problema de reconocimiento facial en imágenes de baja resolución, utilizando técnicas avanzadas de súper-resolución de imágenes (SR) y modelos de redes neuronales profundas. Fue desarrollado en el contexto académico para evaluar y comparar el rendimiento de diferentes arquitecturas de reconocimiento facial.

## Integrantes
- **Juan Vergara**
- **Julio Jofré**


## Metodología
1. **Súper-Resolución Facial**  
   Se utilizó ESRGAN (Enhanced Super-Resolution Generative Adversarial Networks) para transformar imágenes de baja resolución en imágenes de alta resolución. Esta técnica busca mejorar los detalles faciales antes de aplicar modelos de reconocimiento.

2. **Modelos de Reconocimiento Facial**  
   Se evaluaron tres arquitecturas preentrenadas con pesos de ImageNet:
   - **ResNet50**: Con 50 capas profundas y bloques residuales.
   - **MobileNetV2**: Optimizada para dispositivos de recursos limitados.
   - **EfficientNetB0**: Diseñada para maximizar precisión y eficiencia.

3. **Dataset**  
   Se utilizó **TinyFace**, un conjunto de datos con 5139 identidades y 169,403 imágenes de resolución promedio 20×16 píxeles.

4. **Métricas de Evaluación**  
   - *Mean Average Precision (mAP)*
   - *Ranking Normalizado*
   - *Rank-1* y *Rank-20*

## Resultados
### Métricas de Desempeño
| Modelo              | Rank-1 (%) | Rank-20 (%) | Tiempo de Inferencia (s) |
|---------------------|------------|-------------|--------------------------|
| ResNet50 (SR)       | 55.93      | 72.30       | 0.005203                |
| MobileNetV2 (SR)    | 48.82      | 69.30       | 0.005600                |
| EfficientNetB0 (SR) | 51.83      | 70.49       | 0.007811                |

### Observaciones
- La súper-resolución tuvo un impacto limitado en la mejora del rendimiento.
- Los modelos mostraron robustez frente a variaciones en las condiciones de las imágenes.

## Conclusiones
Aunque los resultados no alcanzaron el nivel del estado del arte, se obtuvieron aprendizajes valiosos sobre las limitaciones de las técnicas aplicadas. Futuros trabajos podrían centrarse en:
- Utilizar datasets especializados para preentrenar los modelos.
- Implementar métricas de similitud más adecuadas al problema.

## Referencias
1. [Face Super-Resolution](https://github.com/SkyLionx/face-super-resolution/blob/main/README.md)  
2. [ESRGAN](https://arxiv.org/abs/1809.00219)  
3. [TinyFace Dataset](https://paperswithcode.com/dataset/tinyface)





