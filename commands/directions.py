import command_system

def directions():
   message = 'тут будут направления проекта'
   return message, '', ''

directions_command = command_system.Command()

directions_command.keys = ['направления']
directions_command.description = 'Показываю направления'
directions_command.process = directions