# wb_practice_spark

1) Считать данные из вашей Кафки через спарк. Если нужно, залейте немного данных с пегас.
   - Поднимаем контейнеры: clickhouse, spark, kafka </br>
      <img width="1608" alt="image" src="https://github.com/user-attachments/assets/6b187491-464c-41f6-b071-afe52d5bc694"></br>
   - Подключаемся к кафке через Offset Explorer </br>
      <img width="1356" alt="image" src="https://github.com/user-attachments/assets/1b80ac2a-ef06-463a-934b-cee73bf2ca2d"></br>
      </br>
   - Через [producer](https://github.com/SirRizzer/wb_practice_spark/blob/main/producer.py) заливаем данные из пегаса в топик кафки </br>
      <img width="1370" alt="image" src="https://github.com/user-attachments/assets/13c86b88-aa99-4f1b-aa9b-9dc15d196cd4"></br>
</br>
2) Добавить какую-нибудь колонку. Записать в ваш клик в докере. (*Можно через csv импортировать в ваш клик справочник объемов nm_id с пегаса, чтобы оттуда брать объем номенклатуры.)</br>

   - Подключаемся к локальному клику (default, default) </br>
      <img width="578" alt="image" src="https://github.com/user-attachments/assets/3a9e1240-19b4-4605-b055-7b7aeb401233"></br>
   - Эскпортируем словарь lostreason из пегаса и импортируем в локальный клик </br>
      <img width="789" alt="image" src="https://github.com/user-attachments/assets/d76705b0-0c7c-4c4b-841a-d68b2ebdfb05"></br>
</br>
3) Выложить папку с docker-compose файлами для развертывания контейнеров. Должно быть 2 файла: docker-compose.yml, .env.
  [docker-compose](https://github.com/SirRizzer/wb_practice_spark/tree/main/docker-compose)
</br>
4) Запушить в свой гит получившийся таск спарк. Не пушить файл с паролями.</br>
  ```
      spark-submit --master spark://spark-master:7077  \
      --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 \ 
      --executor-cores 1 \ </br>
      --conf spark.driver.extraJavaOptions="-Divy.cache.dir=/tmp -Divy.home=/tmp" \
      /opt/spark/Streams/shkCreate_edu_100/shkCreate_sync_edu.py
  ```
  [task](https://github.com/SirRizzer/wb_practice_spark/tree/main/pyspark)
</br>
5) Выложить в гит скрины с содержимым конечной папки в вашем клике.
<img width="1398" alt="image" src="https://github.com/user-attachments/assets/dfaae30e-3957-4a34-bbb2-b730b4a01a5e"></br>
</br>
7) Выложить код структуру конечной таблицы в вашем клике.
<img width="587" alt="image" src="https://github.com/user-attachments/assets/df4bfc8f-f32c-4c75-9bf8-bbb6d741fd8f"></br>
</br>
8) Выложить скрин веб интерфейса вашего спарк.
<img width="1728" alt="image" src="https://github.com/user-attachments/assets/73a2f02d-4d5a-436c-9c70-a4ee4841ac80"></br>
</br>
9) Скрин работы вашего приложения из консоли контейнера.</br>
<img width="1722" alt="image" src="https://github.com/user-attachments/assets/896dad21-26b3-4885-a5a2-27b73415d089"></br>
<img width="1211" alt="image" src="https://github.com/user-attachments/assets/791be120-732e-49fe-89db-b5af30e52cf5"></br>



