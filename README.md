# magicurl
A python REST based application that generates small URL's for all requests.

# Docker image hosted at dockerhub
https://hub.docker.com/repository/docker/prateek2408/magicurl

# Usage
1. Start a docker container either in daemon or non-daemon mode- For example-
1. **docker run -it --rm -p 2408:2408 prateek2408/magicurl**
1. Once the container starts, from another terminal try running-
   * curl -XGET http://0.0.0.0:2408

1. This should give you an output like this-
   * Welcome to the magicurl utility for more info visit https://github.com/prateek2408/magicurl
1. To create a magic/short URL for any request do-
   * curl -XPOST -d "URL=https://mario.com" http://0.0.0.0:2408/shorten
1. You should be getting an output similar to this-
   * Short URL= https://murl.ly/9b85da0f4abe56f86e7e3812129d6dda
