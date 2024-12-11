cd set_get_user
source project_one/bin/activate
pip install -r requirements.txt
cd ..
sudo docker-compose build
docker-compose up --detach
docker-compose ps
docker-compose restart profile_srv
идем на http://localhost:8000/docs
в Swagger делаем пост запрос:
curl -X 'POST' \
  'http://localhost:8000/profiles/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "string@mail.ru",
  "first_name": "Ivan",
  "last_name": "Ivanov"
}'
он доступен по: http://localhost:8000/profiles/
docker-compose exec db_service psql -U postgres -d postgres
SELECT * FROM USERS;
 id |     email      | firstname | lastname
----+----------------+-----------+----------
  1 | string@mail.ru | Ivan      | Ivanov
(1 row)
