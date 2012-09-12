from django.core.urlresolvers import resolve
def current_section(request):
    return{"current_section": resolve(request.get_full_path()).url_name}