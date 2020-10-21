import sports
from pynotifier import Notification

matchinfo = sports.get_sport('Cricket')
Notification(title='ipl live score', description=str(matchinfo), duration=60).send()