import pymysql
from django.template.defaultfilters import register
from django.utils.safestring import mark_safe

pymysql.install_as_MySQLdb()


@register.filter('get_attr')
def get_attr(value, attr_name):
    return eval('value.%s' % attr_name)


@register.filter('star_ellipse')
def star_ellipse(value, length):
    if len(str(value)) > int(length):
        return str(value)[:int(length)] + '***'
    return value


@register.filter(is_safe=True)
def to_str(value:str):
    return str(value)


@register.filter(is_safe=True)
def to_img_tag(value:str):
    if value.endswith('.jpg') or value.endswith('.jpgjpg') or value.endswith('.JPG') or value.endswith('.png') or value.endswith('jpeg') or value.startswith("http:"):
        return mark_safe('<img width="120px" height="100px" src="%s" >' % value)

    return mark_safe("%s" % value)


@register.filter(is_safe=True)
def spilt_url(value:str):
    return value.split('/')[-2]