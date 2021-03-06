"""
ifupdown_ng.commands.ifupdown  -  Command specification for 'ifup'/'ifdown'
Copyright (C) 2012-2013  Kyle Moffett <kyle@moffetthome.net>

This program is free software; you can redistribute it and/or modify it
under the terms of version 2 of the GNU General Public License, as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.

You should have received a copy of the GNU General Public License along
with this program; otherwise you can obtain it here:
  http://www.gnu.org/licenses/gpl-2.0.txt
"""

## Futureproofing boilerplate
from __future__ import absolute_import

import argparse
import logging
import sys

from ifupdown_ng.commands import common
from ifupdown_ng.config import parser

class IfUpDownCommandHandler(common.CommonCommandHandler):
	COMMANDS = {
		'ifup': 'Bring up network interfaces',
		'ifdown': 'Take down network interfaces',
	}
	def __init__(self, command):
		## Initialize the parent class
		super(IfUpDownCommandHandler, self).__init__(command,
			usage='%(prog)s [<options>] (--all | <iface>...)')

		## Add state-mutation options
		self.argp.add_argument('-n', '--no-act', action='store_false',
			dest='act',
			help='Display commands but do not run them '
				'(NOTE: Does not disable mapping scripts)')

		self.argp.add_argument('--force', action='store_true',
			help='Run commands even if already up/down')

		## Add the interface list flags
		self.argp.add_argument('iface', type=str, nargs='*',
			help=argparse.SUPPRESS)

		self.argp.add_argument('-a', '--all', action='store_true',
			help='Process all interfaces marked "auto"')

	def execute(self):
		## Load the configuration
		sysconfig = parser.SystemConfig()
		sysconfig.load_interfaces_file()
		sysconfig.log_total_errors()
		if self.log_total.nr_logs_above(logging.ERROR):
			self.logger.critical('Not safe to continue, exiting...')
			sys.exit(255)

		print "BLARG UPDOWN ME HARDER"
