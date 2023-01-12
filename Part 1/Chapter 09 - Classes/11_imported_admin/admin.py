from classes import User, Admin, Privileges

admin_0 = Admin('lucas', 'dondo', 'LucasDondo',
                ['install and uninstall apps', 'control the network',
                 'ban users', 'censor whatever (muajajaja)'])
admin_0.privileges.show_privileges()
