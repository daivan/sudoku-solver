docker build -t foo . && docker run -it foo
docker build -f Dockerfile_tests -t tests . && docker run -it tests