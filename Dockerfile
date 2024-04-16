FROM Muhimn/Muhimn:cc-bot

RUN git clone https://github.com/terxbot/Muhimn.git /root/main

WORKDIR /root/main

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/main/bin:$PATH"

CMD ["python3","-m","main.py"]
