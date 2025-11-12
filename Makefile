build:
	docker build -t pgjavier:1.0.1 .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml doramemon

rm:
	docker stack rm doramemon
