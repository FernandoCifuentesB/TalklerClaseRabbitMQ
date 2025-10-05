import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tareas_distribuidas', durable=True)

channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):
    complejidad = int(body)
    print(f" [x] Recibida tarea con complejidad {complejidad}")
    time.sleep(complejidad)  # Simula el procesamiento
    print(f" [✓] Tarea completada en {complejidad} segundos")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    queue='tareas_distribuidas',
    on_message_callback=callback
)

print(' [*] Esperando tareas. Presiona CTRL+C para salir')
channel.start_consuming()

