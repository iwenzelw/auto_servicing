from django import template

register = template.Library()


# @register.filter
# def verbose_name(obj):
#     return obj._meta.verbose_name
#
#
# @register.filter
# def verbose_name_plural(obj):
#     return obj._meta.verbose_name


@register.simple_tag
def verbose_name(value):
    # Django template filter which returns the verbose name of a model.
    # Note: I set my verbose_name the same as the plural, so I only need one tag.
    if hasattr(value, 'model'):
        value = value.model
    return value._meta.verbose_name.title()


@register.simple_tag
def verbose_name_plural(value):
    '''
 Django template filter which returns the plural verbose name of a model.
    '''
    if hasattr(value, 'model'):
        value = value.model

    return value._meta.verbose_name_plural.title()


@register.simple_tag
def field_name(value, field):
    '''
 Django template filter which returns the verbose name of an object's,
    model's or related manager' sfield.
    '''
    if hasattr(value, 'model'):
        value = value.model

        return value._meta.get_field(field).verbose_name.title()
