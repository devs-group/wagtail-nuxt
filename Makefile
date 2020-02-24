install:
	docker-compose exec cms bash -c 'pip install -r requirements.txt'

install_web_frontend:
	docker-compose run --rm web_frontend bash -c 'rm -fr node_modules && yarn install --force'

migrate:
	docker-compose exec cms bash -c 'python manage.py makemigrations'
	docker-compose exec cms bash -c 'python manage.py migrate'

createsuperuser:
	docker-compose exec cms bash -c "python manage.py createsuperuser"

backup:
	docker-compose exec cms bash -c 'python manage.py dumpdata --natural-foreign --indent 2 \
    -e contenttypes -e auth.permission \
    -e wagtailcore.groupcollectionpermission \
    -e wagtailcore.grouppagepermission -e wagtailimages.rendition \
    -e sessions -e wagtailcore.site > fixtures.json'

load:
	docker-compose exec cms bash -c 'python manage.py loaddata fixtures.json'


deletewagtailimages:
	docker-compose exec cms bash -c 'python manage.py delete_all_wagtail_images'


initial: migrate createsuperuser
