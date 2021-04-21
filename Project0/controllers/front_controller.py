from controllers import client_controller, account_controller, home_controller


def route(app):
    # call other controllers
    client_controller.route(app)
    home_controller.route(app)
 #   account_controller.route(app)
