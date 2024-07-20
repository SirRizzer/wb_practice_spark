from confluent_kafka import Producer
import json
import pandas as pd

config = {
    'bootstrap.servers': '192.168.0.58:29092',  # адрес Kafka сервера
    'client.id': 'simple-producer'
}

producer = Producer(**config)

def data():
    from clickhouse_driver import Client

    dbname = 'default'

    with open(f"/Users/evgenijkolosov/PycharmProjects/pythonProject/keys/wb_key_ch_pegas.json") as json_file:
        data = json.load(json_file)

    client = Client(data['server'][0]['host'],
                    user=data['server'][0]['user'],
                    password=data['server'][0]['password'],
                    verify=False,
                    database=dbname,
                    settings={"numpy_columns": True, 'use_numpy': True},
                    compression=True)

    deps = client.execute(f"""
                select shk_id, toString(dt_operation), lostreason_id, operation_code
                from Shk_LostPost
                where dt_operation > now() - interval 2 minute
                order by dt_operation desc
                limit 100
                """)
    return deps
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def send_message(data):
    try:
        # Асинхронная отправка сообщения
        producer.produce('lost', data.encode('utf-8'), callback=delivery_report)
        producer.poll(0)  # Поллинг для обработки обратных вызовов
    except BufferError:
        print(f"Local producer queue is full ({len(producer)} messages awaiting delivery): try again")

if __name__ == '__main__':
    res = data()
    list_to_json = [{"shk_id": x[0], "dt_operation": x[1], "lostreason_id": x[2], "operation_code": x[3]} for x in res]
    for i in list_to_json:
        send_message(json.dumps(i, ensure_ascii=False))
    producer.flush()
