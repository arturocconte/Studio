FROM python:3.10.5

RUN pip install dash plotly pandas dash-bootstrap-components

WORKDIR /app

COPY . .

CMD ["python", "app.py"]
