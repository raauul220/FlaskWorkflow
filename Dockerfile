FROM python:3.9.16-alpine3.16

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .

EXPOSE 80

RUN chmod +x entrypoint.sh
CMD [ "./entrypoint.sh" ]

#ENTRYPOINT [ "python3", "entry_point.py"]