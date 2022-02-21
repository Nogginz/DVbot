import command_system

def rating():
   message = 'тут будет рейтинг'
   return message, '', ''

rating_command = command_system.Command()

rating_command.keys = ['рейтинг']
rating_command.description = 'Покажу рейтинг'
rating_command.process = rating