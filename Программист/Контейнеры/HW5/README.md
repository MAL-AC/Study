Запустим 2 контейнера
sudo docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0.31

	--name some-mysql (Имя some-mysql)
	-e MYSQL_ROOT_PASSWORD=my-secret (YSQL_ROOT_PASSWORD -константа, пароль - my-secret
	-d запустить в режиме демона
	mysql:8.0.31 - имя образа

sudo docker run --name myphp -d --link some-mysql:db -p 8081:80 phpmyadmin/phpmyadmin

	--link some-mysql:db - связыввает контейнер myphp с my-scl
	-p 8081:80 - проброс портов
	phpmyadmin/phpmyadmin - имя образа на котором будет создан контейнер

В браузере вводим: http://localhost:8081/

![Alt text](<Снимок экрана от 2023-10-24 16-54-14-1.png>)
![Alt text](<Снимок экрана от 2023-10-24 17-00-04-1.png>)


Создаём Docker-compose файл
mal@SkyNet:~$ mkdir composefolder
mal@SkyNet:~$ cd composefolder/
mal@SkyNet:~/composefolder$ nano docker-compose.yml
Прописываем в файле:
version: '3.9'
services:
  db:
    image: mariadb:10.10.2
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: 12345
  adminer:
    image: adminer:4.8.1
    restart: always
    ports:
      - 6080:8080

Запускаем:
sudo docker-compose up -d

В браузере открываем: http://localhost:6080/

![Alt text](<Снимок экрана от 2023-10-24 17-07-09-1.png>)
![Alt text](<Снимок экрана от 2023-10-24 17-15-17-1.png>)