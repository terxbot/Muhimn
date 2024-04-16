FROM Muhimn/Muhimn:cc-bot

RUN git clone https://github.com/terxbot/Muhimn.git /root/main.py

WORKDIR /root/main.py

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/main.py/bin:$PATH"

CMD ["python3","-m","main.py"]
