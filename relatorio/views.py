from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from refact.queries import (
    returna_consultas,
    select_medicos,
    select_datas,
    lista_medicos,
    lista_datas,
    lista_medicos_consultas,
)


def index(request):
    medicos = select_medicos()
    datas = select_datas()

    consultas = ""
    if request.method == "POST":

        nome_medico = request.POST.get("nome_medico")
        data_consulta = request.POST.get("data_consulta")

        if nome_medico == "" and data_consulta == "":
            return HttpResponseRedirect("/")
        if nome_medico != "" and data_consulta == "":
            consultas = lista_medicos(nome_medico)
        elif data_consulta != "" and nome_medico == "":
            consultas = lista_datas(data_consulta)
        else:
            consultas = lista_medicos_consultas(nome_medico, data_consulta)
            if len(consultas) == 0:
                messages.add_message(
                    request, messages.INFO, "Não há registro para o filtro."
                )

    else:

        consultas = returna_consultas()

        # Quantidade por paginas
    p = Paginator(consultas, 10)

    page_num = request.GET.get("page", 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {"consultas": page, "medicos": medicos, "datas": datas}
    return render(request, "index.html", context)
