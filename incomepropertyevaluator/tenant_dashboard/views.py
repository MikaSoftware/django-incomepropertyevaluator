# -*- coding: utf-8 -*-
from django.shortcuts import render


def master_page(request):
    return render(request, 'tenant_dashboard/master_view.html',{
        'current_page_id': 'dashboard-master',
    })
