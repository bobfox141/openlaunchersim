#!/usr/bin/env python3
# this is a anti air missile, generally the idea is shoot down incoming drones
# 


class Missile:
    INITPOS = [0,0,0]
    
        
    def __init__(self, id, arm ):
        fsm = off
        missile_id = id
        armed = arm 