from flask import Flask, Blueprint
from common.api import api_request, post_and_redirect

joernalia = Blueprint('joernalia',
                      __name__)


@joernalia.route('/')
@post_and_redirect(filename='index.html')
def index():
    data = {
        'host_url': 'http://127.0.0.1:5000'
    }
    return data


#
# @joernalia.route('search_product', methods=['POST'])
# @api_request(spec_class=SearchProductSpec)
# def search_products(spec):
#     """
#     :type spec: SearchProductSpec
#     :param filter:
#     :return:
#     """
#     return None


# class GetProductDetail(object):
#     def __init__(self):
#         self.product_id = None
#
#
# @braderhut.route('product_detail', methods=['POST'])
# @api_request(spec_class=GetProductDetail)
# def get_product_detail(spec):
#     """
#     :type spec: GetProductDetail
#     :param spec:
#     :return:
#     """
#     return None
#
#
# class AddProductToCartSpec(object):
#     def __init__(self):
#         self.product_id = None
#         self.amount = None
#
#
# @braderhut.route('add_to_cart', methods=['POST'])
# @api_request(spec_class=AddProductToCartSpec)
# def add_product_to_cart(spec):
#     """
#     :type spec: AddProductToCartSpec
#     :param spec:
#     :return:
#     """
#     return None
#

app = Flask(__name__)
app.register_blueprint(joernalia, url_prefix='/')
