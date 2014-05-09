#! coding=utf-8
#import markdown2
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django. utils.safestring import mark_safe


register = template.Library()

#@register.filter(is_safe=True)
#@stringfilter
#def md2(value):
#    '''
#        目前markdown2 无法处理井号（####）标题
#    '''
#    return mark_safe(markdown2.markdown(
#                force_unicode(value),
#                safe_mode=True)
#            )
#    return mark_safe(markdown2.markdown(value))


try:
    import misaka as m
    from misaka import Markdown, HtmlRenderer
    #https://github.com/FSX/misaka
    #优先使用misaka解析markdown
    @register.filter(is_safe=True)
    @stringfilter
    def md1(value):
        rndr = HtmlRenderer()
        md = Markdown(rndr)
        return md.render(value)
        #return m.html(value)
except:
    @register.filter(is_safe=True)
    @stringfilter
    def md1(value):
        extensions = ["nl2br", "codehilite"]
        return mark_safe(markdown.markdown(force_unicode(value),
                                           extensions,
                                           safe_mode=True,
                                           enable_attributes=False))
