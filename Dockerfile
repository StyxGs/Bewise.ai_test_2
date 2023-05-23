FROM python:3.10-alpine3.17
WORKDIR /task_2
COPY ./requirements.txt /task_2/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /task_2/requirements.txt
COPY . .
RUN chmod a+x *.sh
CMD ["sh", "app.sh"]