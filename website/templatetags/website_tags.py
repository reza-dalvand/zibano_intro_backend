"""
Custom Jinja2 template tags/filters.
"""

# فیلترها در jinja2_env.py تعریف شده‌اند
# این فایل برای فیلترهای اضافی Django templates است

from django import template

register = template.Library()


@register.filter
def to_persian_digit(value):
    """تبدیل اعداد انگلیسی به فارسی"""
    if value is None:
        return ''
    return str(value).translate(
        str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    )


@register.filter
def format_price(value):
    """فرمت قیمت فارسی"""
    if value is None:
        return '۰'
    try:
        num = int(value)
        formatted = f'{num:,}'.translate(
            str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
        )
        return f'{formatted} تومان'
    except (ValueError, TypeError):
        return str(value)