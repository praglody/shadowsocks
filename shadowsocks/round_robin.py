#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RoundRobin():
    servers = []
    weight_sum = 0

    def __init__(self):
        pass

    @staticmethod
    def get_a_server():
        max = 0
        index = -1
        for i, server in enumerate(RoundRobin.servers):
            server['current_weight'] += server['weight']
            if server['current_weight'] > max:
                max = server['current_weight']
                index = i
        RoundRobin.servers[index]['current_weight'] -= RoundRobin.weight_sum
        return (RoundRobin.servers[index]['server'], RoundRobin.servers[index]['server_port'],
                RoundRobin.servers[index]['password'])

    @staticmethod
    def init(servers):
        RoundRobin.servers = servers
        for server in servers:
            if 'weight' not in server or server['weight'] < 1:
                server['weight'] = 1
            server['current_weight'] = 0
            RoundRobin.weight_sum += server['weight']
