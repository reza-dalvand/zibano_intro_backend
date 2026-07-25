"""
Views for zibano_intro website.
"""

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import (
    SiteSettings, HeroSection,
    FeaturesSection, Feature,
    HowToSection, HowToStep,
    ServicesSection, ServiceCategory,
    AboutSection, AboutPoint,
    TeamSection, TeamMember,
    StatsSection, StatItem,
    FAQSection, FAQItem,
    ContactSection, ContactMessage,
    DownloadSection,
    TrustBadge,
    NavItem,
    FooterLinkGroup,
)
from .forms import ContactForm


def index(request):
    """صفحه اصلی سایت معرفی"""

    context = {
        'page_title': 'زیبانو | رزرو آنلاین خدمات زیبایی و سلامت',
    }

    return render(request, 'index.html', context)


@require_POST
def submit_contact(request):
    """پردازش فرم تماس"""

    form = ContactForm(request.POST)

    if form.is_valid():
        message = ContactMessage.objects.create(
            full_name=form.cleaned_data['full_name'],
            phone=form.cleaned_data['phone'],
            email=form.cleaned_data.get('email', ''),
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message'],
        )

        # دریافت پیام موفقیت از تنظیمات
        contact_settings = ContactSection.objects.first()
        success_msg = 'پیام شما با موفقیت ارسال شد.'
        if contact_settings:
            success_msg = contact_settings.form_success_message

        return JsonResponse({
            'success': True,
            'message': success_msg,
        })

    return JsonResponse({
        'success': False,
        'message': 'لطفاً تمام فیلدهای الزامی را پر کنید.',
        'errors': form.errors,
    }, status=400)