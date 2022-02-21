import command_system


def main_manu():
    message = 'главное меню'
    return message, '', ''


main_manu_command = command_system.Command()

main_manu_command.keys = ['назад', 'меню', "главное меню", "начать"]
main_manu_command.description = 'Покажу главное меню'
main_manu_command.process = main_manu