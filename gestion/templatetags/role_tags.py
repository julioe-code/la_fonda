from django import template

register = template.Library()

@register.filter
def has_group(user, group_names):
    if not user.is_authenticated:
        return False

    if user.is_superuser:
        return True

    if isinstance(group_names, str):
        names = [name.strip() for name in group_names.split(',') if name.strip()]
        return user.groups.filter(name__in=names).exists()

    return False

@register.simple_tag
def user_role(user):
    if not user.is_authenticated:
        return ''
    if user.is_superuser:
        return 'Administrador'
    group = user.groups.first()
    return group.name if group else ''
