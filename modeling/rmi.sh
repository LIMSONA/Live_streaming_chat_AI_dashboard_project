docker stop jupyter-notebook && docker rm jupyter-notebook && docker image rmi my-cuda:0.1


docker rmi $(docker images -f "dangling=true" -q)