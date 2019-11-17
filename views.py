from flask import render_template, request, redirect, url_for,make_response,jsonify, session as login_session
from werkzeug.utils import secure_filename
import bleach
import flask_login
from dbhelper import *
from auth import *
from main import app,loginManager


def get_response(template_file):
	return make_response(render_template(template_file))

