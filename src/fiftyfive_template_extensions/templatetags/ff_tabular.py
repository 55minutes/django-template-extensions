from django.template import Library
register = Library()

def tabularize(value, cols):
    """modifies a list to become a list of lists
    eg [1,2,3,4] becomes [[1,2], [3,4]] with an argument of 2"""
    try:
        cols = int(cols)
    except ValueError:
        return [value]
    return map(*([None] + [value[i::cols] for i in range(0, cols)]))
register.filter('tabularize', tabularize)
