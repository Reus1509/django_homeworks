#from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return HttpResponse('''<!DOCTYPE html>
                            <html lang="en">
                            <head>
                            <meta charset="UTF-8">
                            <title>Главная</title>
                            <style>
                                 h3 { 
                                     font-size: 120%; 
                                     font-family: Verdana, Arial, Helvetica, sans-serif; 
                                     color: #333366; 
                                    }
                            </style>
                            </head>
                            <body>
                                <h3>Это главная страница веб приложения на Django</h3>
                                <a href="http://127.0.0.1:8000/about">Обо мне</a>
                            </body>
                            </html>''')


def about_me(request):
    return HttpResponse('''<!DOCTYPE html>
                            <html lang="en">
                            <head>
                            <meta charset="UTF-8">
                            <title>Обо мне</title>
                            <style>
                                 h3 { 
                                     font-size: 120%; 
                                     font-family: Verdana, Arial, Helvetica, sans-serif; 
                                     color: #333366; 
                                    }
                            </style>
                            </head>
                            <body>
                                <h3>Это страница обо мне</h3>
                                <a href="http://127.0.0.1:8000">Главная</a>
                            </body>
                            </html>''')
