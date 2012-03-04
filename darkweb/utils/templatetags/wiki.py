import re
from django import template
from django.template.defaultfilters import slugify

"""
[title|page] # slugify

OR

[title] # slugify
"""

LINK_RE = re.compile(r'\[\[(?P<title>[\w\s]+)(\|(?P<slug>[\w\s]+))?\]\]')

def link_replace(match):
    kwargs = match.groupdict()

    if not kwargs['slug']:
        kwargs['slug'] = slugify(kwargs['title'])

    return '<a href="/wiki/{slug}/">{title}</a>'.format(**kwargs)

register = template.Library()

@register.filter
def links(value):
    return LINK_RE.sub(link_replace, value)
links.is_safe = True
