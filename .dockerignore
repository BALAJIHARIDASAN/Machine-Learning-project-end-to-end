
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app


# os
# app name
# working directory
# required library for project installation
# port number required by heroku or render 
# to run the app service
