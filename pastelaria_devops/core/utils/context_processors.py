import os

def common_variables(request):
    context = {}
    context['COMPANY'] = os.getenv('COMPANY', 'DEMO')
    return context
