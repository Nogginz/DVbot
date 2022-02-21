import command_system

def workbook():
   message = 'тут будет рабочая тетрадь'
   return message, '', ''

workbook_command = command_system.Command()

workbook_command.keys = ['рабочая тетрадь']
workbook_command.description = 'Покажу рабочую тетрадь'
workbook_command.process = workbook