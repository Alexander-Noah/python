import pika
QUEUE_NAME='scrape'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))#连接
channel =  connection.channel()#频道对象
channel.queue_declare(queue=QUEUE_NAME)#声明队列
channel.basic_publish(exchange='',
                      routing_key=QUEUE_NAME,
                      body='Hello World!')