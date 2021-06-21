# python_practice
	Основная идея проекта – реализовать функционал легендарной игры-головоломки “сапер”, используя знания, полученные во время семестра. Несмотря на небольшой объем проекта – сделать игру простой и интересной. 
	Был создан ряд функций. Check_mines - Функция, возвращающая количество мин вокруг соседей. Generate_neighbors - Возвращает клетки соседствующие с square. Clearance – эффективная функция для очистки поля(окрашивает безопасные(не соседствующие с минами) клетки в зеленый), Click – обрабатывает клик(ход) – если попадаем на мину, то клетка окрашивается в красный и вызывается функция Finish, в ином случае клетка окрашивается в зеленый. Markmine – позволяет пометить мину желтым цветом. 
	Для реализации интерфейса был использована библиотека  “tkinter”, так же была использована библиотека «random» - для генерации. “tkinter.messagebox” -для реализации всплывающих окон.