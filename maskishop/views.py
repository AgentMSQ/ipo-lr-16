# maskishop/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Главная страница с ссылками"""
    html_content = """
    <h1>Главная страница maskishop</h1>
    <p>Добро пожаловать в наш магазин!</p>
    
    <h2>Навигация:</h2>
    <ul>
        <li><a href="/yoga/aboutauthor/">Об авторе</a></li>
        <li><a href="/yoga/aboutshop/">О магазине</a></li>
    </ul>
    """
    return HttpResponse(html_content)

def about_author(request):
    """Страница об авторе с ссылкой на главную"""
    html_content = """
    <h1>Об авторе</h1>
    <p>Эту лабу сделал Попов Игнат 89ТП МГКЦТ(я сам все делал)</p>
    <p><a href="/yoga/">← Вернуться на главную</a></p>
    """
    return HttpResponse(html_content)

def about_shop(request):
    """Страница о магазине с ссылкой на главную"""
    html_content = """
    <h1>О магазине</h1>
    <p>Магазин товаров для йоги (коврики, блоки, ремни).</p>
    <p><a href="/yoga/">← Вернуться на главную</a></p>
    """
    return HttpResponse(html_content)