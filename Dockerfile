FROM python:3.8-slim


WORKDIR /home
RUN mkdir -p /home/data /home/output


COPY . /home/data

RUN touch /home/output/result.txt


RUN chmod +x /home/data/Vishali.py
RUN chmod +w /home/output/result.txt

CMD ["python3", "/home/data/Vishali.py"]