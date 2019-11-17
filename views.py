from flask import make_response,render_template


def get_response(template_file):
	return make_response(render_template(template_file))