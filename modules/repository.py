from flask import Flask, render_template,request,redirect
from flask_restful import Api, Resource,reqparse
from texts import *
from transformers import pipeline
import requests


