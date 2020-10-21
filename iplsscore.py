import sports
from pynotifier import Notification

matchinfo = sports.get_sport('cricket')
Notification(title='ipl live score', description=str(matchinfo), duration=60).send()