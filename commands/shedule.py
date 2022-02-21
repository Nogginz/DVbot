import command_system

def shedule():
   message = 'тут будет расписание'
   return message, '', ''

shedule_command = command_system.Command()

shedule_command.keys = ['расписание']
shedule_command.description = 'Покажу Расписание'
shedule_command.process = shedule