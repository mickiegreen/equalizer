# -*- coding: utf-8 -*-

# Copyright (c) 2018 Michael Green
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sshtunnel
import MySQLdb

class MysqlTunnelConnection(object):
    def __init__(self, host, user, password, schema, port=3306,
                 use_tunnel=False, ssh_port=22, ssh_host=None,
                 ssh_user=None, ssh_passwd=None, remote_mysql_port=None,
                 remote_bind_address=None, local_bind_address=None):

        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.schema = schema
        self.use_tunnel = use_tunnel

        # if tunnel is required
        if use_tunnel == True:
            self.ssh_tunnel_info = dict(
                ssh_address_or_host=(ssh_host, ssh_port),
                ssh_username=ssh_user,
                ssh_password=ssh_passwd,
                remote_bind_address=(remote_bind_address, remote_mysql_port),
                local_bind_address=(local_bind_address, port)
            )

    def __enter__(self):
        if self.use_tunnel:
            self.tunnel = sshtunnel.SSHTunnelForwarder(
                **self.ssh_tunnel_info
            )

        self.connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.schema,
                port=self.port
        )

        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # closing both
        self.connection.__exit__(exc_type, exc_val, exc_tb)

        if hasattr(self, 'tunnel'):
            self.tunnel.__exit__(exc_type, exc_val, exc_tb)