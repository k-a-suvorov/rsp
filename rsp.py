#!/usr/bin/python
# -*- coding: utf-8 -*-
# Игра камень ножницы бумага в функционально-структурном программировании
# В конструкции try; except ловятся ошибки загрузки модулей, ошиббок типов переменных 
# ошибок самих переменных и системные ошибки

try:
	
	# Загрузка модулей
	import random
	import os
	import time

	# Cyfxfkf eстановите библиотеку командой pip3 install colorama
	import colorama
	from colorama import Fore, Back, Style
	colorama.init()	

	# Объявление глобальной переменной
	switch = True
	
	
	# функция загрузки анимации
	def loadStartAnimation():
		print(Fore.MAGENTA + 'Загружаем игру... \n')
		time.sleep(0.1)
		start = '0123456789'
		succsess = ' Game was loaded successfully!'
		
		for i in range(len(start)):
			i = '|*'
			time.sleep(0.2)
			print(Fore.GREEN, Style.BRIGHT + " ", i, end="")
		print(succsess)
	
	
	# функция загрузки анимации
	def loadShutdownAnimation():
		print(Fore.RED + 'Выгружаем игру... \n')
		time.sleep(0.1)
		start = '0123456789'
		succsess = ' Game was shutdown successfully!'
		
		for i in range(len(start)):
			i = '*|'
			time.sleep(0.2)
			print(Fore.RED + " ", i, end="")
		print(succsess)
	
	
	# функция очистки дисплея с автоопределением системы и вызова игрового меню
	def clearScreen():
		if (os.name == 'nt'):
			time.sleep(2)
			os.system('cls')
			menuGame()
		elif (os.name == 'posix'):
			time.sleep(2)
			os.system('clear')
			menuGame()
		else:
			print(Fore.YELLOW, Back.RED + 'Другие операционные системы не поддерживаются!')
			exitGame()	
		
	# функция игры
	def startGame():
		loadStartAnimation()
		global switch
		global comp
		print(Fore.CYAN + '1 - камень, 2 - ножницы. 3 - бумага \n')
		select = int(input('>>> '))
		if (select < 0 or select > 3):
			print(Fore.YELLOW, Back.RED, Style.BRIGHT + 'Похоже вы сегодня не в форме спорить. Приходите завтра!')
			exitGame()
		elif(select == 1):
			comp = random.randint(1,3)
			if (select == 1 and comp == 1):
				print(Fore.YELLOW + 'Ничья - камень | камень')
				clearScreen()					
			elif (select == 1 and comp == 2): 	
				print(Fore.GREEN + 'Вы выиграли камень | ножницы')
				clearScreen()	
			elif (select == 2 and comp == 1): 	
				print(Fore.RED + 'Вы проиграли ножницы | камень')
				clearScreen()	
			elif (select == 3 and comp == 1): 	
				print(Fore.GREEN + 'Вы выиграли бумага | камень')
				clearScreen()	
			elif (select == 3 and comp == 1): 	
				print(Fore.RED + 'Вы проиграли камень | бумага')
				clearScreen()	
		elif(select == 2):
			comp = random.randint(1,3)
			if (select == 2 and comp == 2):
				print(Fore.YELLOW + 'Ничья - ножницы | ножницы')
				clearScreen()	
			elif (select == 1 and comp == 2): 	
				print(Fore.GREEN + 'Вы выиграли камень | ножницы')
				clearScreen()	
			elif (select == 2 and comp == 1): 	
				print(Fore.RED + 'Вы проиграли ножницы | камень')
				clearScreen()	
			elif (select == 2 and comp == 3): 	
				print(Fore.GREEN + 'Вы выиграли ножницы | бумага')
				clearScreen()	
			elif (select == 3 and comp == 1): 	
				print(Fore.RED + 'Вы проиграли бумага | ножницы')	
				clearScreen()	
		elif(select == 3):
			comp = random.randint(1,3)
			if (select == 3 and comp == 3):
				print(Fore.YELLOW + 'Ничья - бумага| бумага')
				clearScreen()	
			elif (select == 3 and comp == 1): 	
				print(Fore.GREEN + 'Вы выиграли бумага | камень')
				clearScreen()	
			elif (select == 1 and comp == 3): 	
				print(Fore.RED +  'Вы проиграли камень | бумага')
				clearScreen()	
			elif (select == 2 and comp == 3): 	
				print(Fore.GREEN + 'Вы выиграли ножницы | бумага')
				clearScreen()	
			elif (select == 3 and comp == 2): 	
				print(Fore.RED + 'Вы проиграли бумага | ножницы')		
				clearScreen()	
	
	# функция меню игры
	def menuGame():
		global switch
		print(Fore.YELLOW + ''' 
		_____________________________________________________________________________
		*** Игра \"Камень, ножницы бумага!\" (Created by Opsis, ver 1.0.console) ***
		*** Выберете 1, что бы сыграть, 0 - что бы выйти из игры ***
		_____________________________________________________________________________
		''')
		print()
		user = int(input(Fore.YELLOW + 'Желаете сыграть? \n 1 - Да \n 0 - Выход \n>>> '))
		if ((user < 0 or user > 1) or (user == 0)):
			exitGame()
		else:
			startGame()	

	# функция выхода из игры
	def exitGame():
		time.sleep(2)
		print(Fore.RED + 'До свидания!')
		loadShutdownAnimation()
				
	# Вызов функции меню			
	menuGame()
	
	# Обработка исключений
	
except ValueError:
    print("You have some mistake of userinput current float Value")
except TypeError:
   print("You have some mistake of userinput float Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!")
except ImportError:
	print("Some modules not loaded, please check your source code!")
