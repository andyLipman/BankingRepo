from flask import request, jsonify


def route(app):

    @app.route("/contact", methods=['GET'])
    def contact():
        return "Contact us via email: andrew@email.com or by phone: 999-999-999"
