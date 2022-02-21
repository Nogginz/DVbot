import command_system
from keyboards import KeyBoard

def about_project():
   message = 'тут будет рассказано о проекте'
   keyboard = KeyBoard(["Назад"])
   return message, '', keyboard.get_keyboard()

about_project_command = command_system.Command()

about_project_command.keys = ['о проекте']
about_project_command.description = 'Расскажу о проекте!'
about_project_command.process = about_project