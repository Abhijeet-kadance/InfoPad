FROM python:3.9.7-slim

COPY . /app
WORKDIR /app 

RUN python3 -m venv /otp/venv

RUN /otp/venv/bib/pip install pip --upgrade && \
    /otp/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh

CMD [ "/app/entrypoint.sh" ]

