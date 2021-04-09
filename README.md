# pymc3-gpu-docker

This repository contains Docker files for running PyMC3 with GPU support for Theano.

To build the Docker:
```
docker build -t theano_secure .
```

To start the Docker:
```
nvidia-docker run -d -p 8888:8888  -e PASSWORD="123abcChangeThis" theano_secure
```
Open your browser at http://HOST:8888 and use `PASSWORD` to log in.

To start it with a more secure remote connection:
```
nvidia-docker run -d -p 8888:8888  -e PASSWORD="123abcChangeThis" -e USE_HTTPS=yes theano_secure
```
Then open your browser at https://HOST:8888.
