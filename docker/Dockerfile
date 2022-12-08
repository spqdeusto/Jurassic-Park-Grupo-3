FROM python:3.9
WORKDIR /code
COPY ./backend/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
RUN pip install uvicorn
RUN pip install mysqlclient
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
