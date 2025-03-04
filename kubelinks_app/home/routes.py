from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from . import gateway_list, ingress_list, extra_list

home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates')


@home_bp.route('/', methods=["GET"])
def home():
    try:
        ingress = ingress_list.get_ingress_list()
        gateway = gateway_list.get_gw_list()
        extraurls = extra_list.get_eu_list()

        return render_template("home.html",
                               ingress=ingress,
                               gateway=gateway,
                               extraurls=extraurls)
    except TemplateNotFound:
        abort(404)
