# -*- encoding : utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from models import ItemAgenda
from forms import FormItemAgenda

@login_required
def lista(request):
	lista_itens = ItemAgenda.objects.filter(usuario=request.user)
	return render_to_response("lista.html",{'lista_itens': lista_itens},
						context_instance=RequestContext(request))
@login_required
def adiciona(request):
	if request.method == "POST":
		form = FormItemAgenda(request.POST, request.FILES)
		if form.is_valid():
			item = form.save(commit=False)
			item.usuario = request.user
			item.save()
			return render_to_response("salvo.html",{})
	else:
		form = FormItemAgenda()
	return render_to_response("adiciona.html",{'form':form},
				  context_instance=RequestContext(request))
@login_required
def item(request, nr_item):
	item = get_object_or_404(ItemAgenda, pk=nr_item, usuario=request.user)
	if request.method == "POST":
		form = FormItemAgenda(request.POST, request.FILES, instance=item)
		if form.is_valid():
			item = form.save(commit=False)
			item.usuario = request.user
			item.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormItemAgenda(instance=item)
	return render_to_response("item.html", {'form':form},
				  context_instance=RequestContext(request))
@login_required
def remove(request, nr_item):
	item = get_object_or_404(ItemAgenda, pk=nr_item, usuario=request.user)
	if request.method == "POST":
		item.delete()
		return render_to_response("removido.html",{})
	return render_to_response("remove.html", {'item':item},
				  context_instance=RequestContext(request))
	

