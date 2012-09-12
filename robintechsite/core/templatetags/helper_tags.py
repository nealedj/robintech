
from django import template

register = template.Library()

@register.tag
def nav_active(parser, token):
    tag_name, nav_name = token.split_contents()
    return NavActiveNode(nav_name)

class NavActiveNode(template.Node):
    def __init__(self, nav_name):
        self.current_section = template.Variable('current_section')
        self.nav_name = nav_name

    def render(self, context):
        try:
            return 'active' if self.current_section.resolve(context) == self.nav_name else ''
        except template.VariableDoesNotExist:
            return ''
