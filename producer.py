import pika
import random
import time


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tareas_distribuidas', durable=True)

for i in range(10):
    complejidad = random.randint(1, 5)
    message = str(complejidad)
    channel.basic_publish(
        exchange='',
        routing_key='tareas_distribuidas',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,
        ))
    print(f" [x] Enviada tarea {i+1} con complejidad {complejidad}")
    time.sleep(0.2)

connection.close()

