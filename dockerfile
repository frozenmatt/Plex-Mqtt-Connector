FROM python:3.9

RUN pip install flask-restful paho-mqtt requests

ENV YES_YOU_ARE_IN_A_CONTAINER="True"

RUN mkdir -p /app/scripts
COPY src/ /app/scripts/
RUN chmod a+x /app/scripts/mqtt-plex-connector.py

CMD [ "python", "-u", "/app/scripts/mqtt-plex-connector.py"]