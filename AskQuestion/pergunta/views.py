from django.shortcuts import render,redirect,get_object_or_404
from .models import Pergunta,Resposta
from .forms import UserRegistrationForm,PerguntaRegistrationForm,RespostaForm,UpdatePerguntaForm,UpdateRespostaForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Views referentes às perguntas
@login_required
def perguntas_list(request):
    if 's' in request.GET:
        s = request.GET['s']
        perguntas_list = Pergunta.objects.filter(titulo__icontains=s).order_by('-publicado')
    else:
        perguntas_list = Pergunta.objects.all().order_by('-publicado')

    paginator = Paginator(perguntas_list, 4)
    page = request.GET.get('page')
    try:
        perguntas = paginator.page(page)

    except PageNotAnInteger:
        perguntas = paginator.page(1)

    except EmptyPage:
        perguntas = paginator.page(paginator.num_pages)

    return render(request,'perguntas/perguntas.html',{'perguntas_list':perguntas, 'page':page})


@login_required
def pergunta_detalhes(request,slug):
    pergunta= get_object_or_404(Pergunta, slug=slug)
    lista_respostas = Resposta.objects.filter(pergunta=pergunta)

    #Resposta do usuário
    if request.method == 'POST':
        resposta_form = RespostaForm(request.POST)
        if resposta_form.is_valid():
            resposta = resposta_form.save(commit=False)
            resposta.pergunta = pergunta
            resposta.autor = request.user
            resposta = resposta_form.save()

            return redirect('pergunta_detalhes', slug=pergunta.slug)

    else:
        resposta_form = RespostaForm()

    return render(request,'perguntas/pergunta_detalhes.html',{'pergunta':pergunta,'lista_respostas':lista_respostas,'resposta_form':resposta_form})



@login_required
def create_pergunta(request):
    if request.method == 'POST':
        pergunta_form = PerguntaRegistrationForm(request.POST)

        if pergunta_form.is_valid():
            pergunta = pergunta_form.save(commit=False)
            pergunta.autor = request.user
            pergunta = pergunta_form.save()

            return redirect('perguntas')
    else:
        pergunta_form = PerguntaRegistrationForm()

    return render(request,'perguntas/add_pergunta.html',{'pergunta_form':pergunta_form})


@login_required
def update_pergunta(request, slug):
    pergunta= get_object_or_404(Pergunta, slug=slug)
    form = UpdatePerguntaForm(request.POST or None, instance=pergunta)
    if form.is_valid():
        form.save()
        return redirect('perguntas')

    return render(request,'perguntas/update_pergunta.html',{'form':form})


@login_required
def delete_pergunta(request, slug):
    pergunta = get_object_or_404(Pergunta, slug=slug)
    pergunta.delete()
    return redirect('perguntas')




#Views referentes às respostas (atualizar e excluir) A criação de respo

@login_required
def update_resposta(request, id):
    resposta = get_object_or_404(Resposta, id=id)
    form = UpdateRespostaForm(request.POST or None, instance=resposta)
    if form.is_valid():
        form.save()
        return redirect('pergunta_detalhes', slug=resposta.pergunta.slug)

    return render(request,'update_resposta.html',{'form':form})


@login_required
def delete_resposta(request, id):
    resposta = get_object_or_404(Resposta, id=id)
    resposta.delete()
    return redirect('pergunta_detalhes', slug=resposta.pergunta.slug)




#Listagem de perguntas e respostas que cada usuario enviou
@login_required
def list_info(request):
    perguntas = Pergunta.objects.filter(autor=request.user).order_by('-publicado')
    respostas = Resposta.objects.filter(autor=request.user).order_by('-publicado')

    return render(request,'list_info.html',{'perguntas':perguntas, 'respostas':respostas})




#Views referentes ao registro e conta
def registrar(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'registration/register_done.html',{'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request,'registration/register.html',{'user_form':user_form})



@login_required
def change_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'O perfil foi alterado com sucesso!')

    form = ProfileForm(instance=request.user)
    return render(request,'registration/profile.html',{'form':form})





