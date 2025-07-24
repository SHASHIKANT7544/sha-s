FROM REDHAD/UBI8

RUN yum install python3 -y

RUN pIP3 install flask

COPY app.py /app.py

CMD [ "python3" , "/app.py"]