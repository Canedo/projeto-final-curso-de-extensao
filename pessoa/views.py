# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from pessoa.models import DocumentosPendentes
from core.models import get_documento_display
from django.contrib import messages


@user_passes_test(lambda u: u.tipo == u.ALUNO)
def documentos(request):
    context = {}
    documentos_pendentes = []
    obj = DocumentosPendentes.objects.filter(aluno=request.user).first()

    if obj:
        obj_list = ''.join(filter(str.isdigit, str(obj.documentos)))
        for documento in obj_list:
            if not documento:
                continue

            documentos_pendentes.append(get_documento_display(int(documento)))

        if obj.outros:
            documentos_pendentes += obj.outros.split(',')

        context['documentos'] = documentos_pendentes

    if len(documentos_pendentes) == 0:
        messages.add_message(request, messages.INFO, 'Você não possui documentos pendentes')
    return render(request, 'documentos.html', context)
