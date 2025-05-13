from kafka import KafkaConsumer, KafkaProducer
import json
from collections import Counter

consumer = KafkaConsumer(
    'user_actions',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='user_group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

dlt_producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

stats = Counter()
total = 0

print("📡 Ожидание сообщений из 'user_actions'...")

for msg in consumer:
    try:
        data = msg.value
        if data.get("action") == "purchase":
            total += 1
            stats[data["action"]] += 1
            print(f"✔️ Получено сообщение: {data}")
            print(f"📊 Статистика: всего = {total}, частые действия = {stats}")
        else:
            print(f"⏭️ Игнорировано: {data}")
    except Exception as e:
        print("❌ Ошибка при обработке сообщения:", e)
        dlt_producer.send("user_actions_dlt", msg.value)