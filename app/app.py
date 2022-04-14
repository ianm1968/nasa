from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    response=requests.get('https://api.nasa.gov/planetary/apod', params={'api_key':'ivjmWNKxDMBkaNoiXgaErQx3nm4A8ynl74fRaI0w'})
    content=json.loads(response.content)
    return render_template('index.html', landing_image=content['hdurl'])

@app.route('/mars')
def mars():
    response=requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000', params={'api_key':'ivjmWNKxDMBkaNoiXgaErQx3nm4A8ynl74fRaI0w'})
    content=json.loads(response.content)
    return render_template('mars.html')