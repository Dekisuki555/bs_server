import _ba
import bs
import bsInternal
import bsUtils
import json
import os
import time
import threading

OWNER_PB_ID = 'pb-IF4yUU0fNw'

roles = {}
tickets = {}
questions = []
database = {}

def load_data():
    global roles, tickets, questions, database
    if os.path.exists('roles.json'):
        roles = json.load(open('roles.json'))
    if os.path.exists('tickets.json'):
        tickets = json.load(open('tickets.json'))
    if os.path.exists('question.json'):
        questions = json.load(open('question.json'))
    if os.path.exists('database.json'):
        database = json.load(open('database.json'))

def save_roles():
    json.dump(roles, open('roles.json', 'w'))

def save_tickets():
    json.dump(tickets, open('tickets.json', 'w'))

def save_database():
    json.dump(database, open('database.json', 'w'))

def handle_command(msg, client_id, pb_id):
    if pb_id != OWNER_PB_ID:
        return
    if msg == '/kickall':
        for p in bsInternal._getGameRoster():
            if p['clientID'] != client_id:
                bsInternal._disconnectClient(p['clientID'])
        bs.screenMessage('✅ COMMAND ACCEPTED YOUR GRACE!', color=(1, 1, 0), transient=True)
    elif msg.startswith('/setrole'):
        try:
            parts = msg.split(' ')
            target_id = parts[1]
            role = parts[2]
            roles[target_id] = role
            save_roles()
            bs.chatMessage(f"Role {role} set to {target_id}")
        except:
            bs.chatMessage('Invalid usage')
    elif msg.startswith('/addtickets'):
        try:
            parts = msg.split(' ')
            target_id = parts[1]
            amount = int(parts[2])
            tickets[target_id] = tickets.get(target_id, 0) + amount
            save_tickets()
            bs.chatMessage(f"Added {amount} tickets to {target_id}")
        except:
            bs.chatMessage('Invalid usage')
    elif msg.startswith('/change'):
        mode = msg.split(' ')[1]
        bs.screenMessage(f'✅ Game mode changed to {mode}', color=(1, 1, 0))
        # Mode change logic

load_data()