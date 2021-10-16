FROM python:3.8.2
LABEL authors="IKHLEF Ali and HAMZA Younes"
LABEL class="3GI-RSI-A"

WORKDIR /code
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 5100
CMD [ "python", "api/app.py" ]