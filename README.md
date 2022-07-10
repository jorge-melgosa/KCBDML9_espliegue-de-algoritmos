# Modulo: Despliegue de algoritmos
`Fecha maxima de entrega: 10 de Julio 2022`

### Enunciado:
Durante este último año la plataforma de vídeo en streaming Twitch ha cogido mucha popularidad debido a la situación que hemos vivido debido al COVID-19. Por esto, mucha gente de todas las edades ha empezado a consumir esta plataforma de manera diaria.

Como consecuencia, no sólo han aumentado las personas que ven contenido en Twitch, sino también el número de los denominados trolls, gente que pone comentarios ofensivos en los chat de los streamers.

En esta práctica se desarrollará un sistema autónomo basado en IA y desplegado en GCP que detectará en tiempo real si los mensajes que se envían a un canal de Twitch son de un troll o no. La práctica constará de tres partes principales que serán evaluadas en la corrección:

- Entrenamiento e inferencia en Batch de un modelo usando Dataflow y AI Platform. (3.5 puntos).
- Despliegue e inferencia online en microservicio con el modelo. (3.5 puntos).
- Inferencia en streaming de un canal de Twitch con el microservicio anterior. (3 puntos).

### Resumen de la implementación:
Hemos realizado la tarea en [Google Colab](https://colab.research.google.com/) llamado [MEL_Detección_Trolls_en_Twitch.ipynb](https://github.com/jorge-melgosa/KCBDML9_espliegue-de-algoritmos/tree/main/colab/MEL_Detección_Trolls_en_Twitch.ipynb)

El colab tiene toda la información necesaria para entender el desarrollo realizado con el objetivo de realizar la practica planteada. 
