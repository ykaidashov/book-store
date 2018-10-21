from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def copyright(context, start_year=None):
    template_mask = '&copy; {0}-{1}'
    if start_year is None:
        template_mask = '&copy; {1}'
    return template.Template(template_mask.format(start_year, '{% now "Y" %}')).render(context)
