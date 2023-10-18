from django import template
from django.shortcuts import get_object_or_404
from menu.models import MenuItems

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Функция получения основных (первых) пунктов меню
    """
    return_context = {}
    requested_url = context['request'].path
    menu_parts = (MenuItems.objects.filter(category__name=menu_name)
                  .select_related('category'))
    active_menu_item = None
    return_context['main_menu_items'] = []
    for part in menu_parts:
        if part.url == requested_url:
            active_menu_item = part
        if part.parent == None:
            return_context['main_menu_items'].append(part)
    # Получаем открытые пункты меню исходя из url
    if active_menu_item:
        open_menu_item_ids = (active_menu_item.get_elder_ids() +
                                   [active_menu_item.id])
        return_context['open_menu_item_ids'] = open_menu_item_ids
    return return_context


@register.inclusion_tag('sub_menu.html', takes_context=True)
def get_menu_item_children(context, menu_item_id):
    """
        Функция получения всех подпунктов меню
    """
    menu_item = get_object_or_404(MenuItems, pk=menu_item_id)
    return_context = {'menu_item': menu_item}
    if 'open_menu_item_ids' in context:
        return_context['open_menu_item_ids']\
            = context['open_menu_item_ids']
    return return_context
