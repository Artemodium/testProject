# projectTest
Тестовое задание для работодателя.
Интерфейс для добавления оборудования в базу данных.
Решение выполнено с помощью фреймворка DJANGO, библиотеки стилей BOOTSTRAP и СУБД SQLite.

База данных состоит из двух таблиц Equipments и EquipmentType. 

    EquipmentType -> id - PrimaryKey, name(Наименование оборудования), serialNumberMask(маска серийного 
    номера)

    Equipments -> id, serialNumber, EquipmentType_id - ForeignKey

Интерфес состоит из полей: 
    Select - для выбора наименования оборудования, берётся из базы данных.
  
    Textaria - для ввода серийных номеров, можно вводить как угодно, лишь бы с не численно-буквенным
    разделителем. Введённые данные проверяются при помощи RegExp.
  
    Button - при нажатии обрабатывается содержимое полей и выводится результат произведённых действий.
                           
До запуска приложения может потребоваться установить зависимости pip install testProject\Storage -r requirements.txt

Приложение запускается командой python testProject\Storage manage.py runserver
