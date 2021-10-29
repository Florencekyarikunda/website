from django import template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return template('fourOwfour.html'),404