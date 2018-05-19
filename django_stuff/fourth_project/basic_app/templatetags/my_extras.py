from django import template

register = template.Library()

def cutfilter(value,arg):
    """
    This cuts out all values of "arg" form the string!
    """
    return value.replace(arg,'')

register.filter('cutfilter',cutfilter)
