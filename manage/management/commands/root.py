from django.core.management.base import BaseCommand, CommandError, CommandParser

import os, argparse

from . import ls


class Command(BaseCommand):

    def run_from_argv(self, argv):
        try:
            super().run_from_argv(argv)
        except CommandError as e:
            parser = CommandParser()
            _, subcommand = parser.parse_known_args(argv[2:])
            parser = self.create_parser(argv[0], argv[1])
            for action in parser._actions:
                if action.dest is argparse.SUPPRESS:
                    action.choices.get(subcommand[0]).print_help()
        except Exception as e:
            print(e)

    def add_arguments(self, root_parser):

        subparsers = root_parser.add_subparsers(
                title='subcommands',
                help='additional help')
        parser = subparsers.add_parser('ls')

        # aqui agragar todo lo que te guste para ls :3
        parser.set_defaults(func=ls.cmd)

        parser = subparsers.add_parser('rm')
        parser.add_argument('file')
        # aqui agregar todo lo que te guste para rm

    def handle(self, *args, **options):

        if options.get('func'):
            options['func']()
        else:
            self.print_help('manage.py', "root")



