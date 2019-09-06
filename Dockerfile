FROM petronetto/opencv-alpine

WORKDIR /scripts
RUN pwd && ls

ENTRYPOINT ["python"]
