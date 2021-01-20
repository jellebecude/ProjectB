import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )



shift_clock_pin = 5
latch_clock_pin = 6
schuif_data_pin = 13
GPIO.setup( shift_clock_pin, GPIO.OUT )
GPIO.setup( latch_clock_pin, GPIO.OUT )
GPIO.setup( schuif_data_pin, GPIO.OUT )

sr04_trig = 20
sr04_echo = 21
GPIO.setup( sr04_trig, GPIO.OUT )
GPIO.setup( sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

servo = 2
GPIO.setup( servo, GPIO.OUT )
pwm = GPIO.PWM(servo,50) # 50 Hz (20 ms PWM period)
pwm.start(7) # start PWM by rotating to 90 degrees

switch_on = 4
switch_off = 17
GPIO.setup(switch_on, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setup( switch_off, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

led_clock_pin = 19
led_data_pin = 26
GPIO.setup(led_clock_pin, GPIO.OUT)
GPIO.setup(led_data_pin, GPIO.OUT)

key = 'C76019E63D217C7437EF94C5D1545716'
SteamID = '76561198202050042'
FriendUrl = f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={key}&steamid={SteamID}&relationship=friend'
friendlist = requests.get(FriendUrl).json()['friendslist']['friends']


#Afstand sensor
def sr04(trig_pin, echo_pin):

    GPIO.output(trig_pin, True)
    time.sleep(1)
    GPIO.output(trig_pin, False)

    StartTime = time.time()
    while GPIO.input(echo_pin) == 0:
        StartTime = time.time()

    StopTime = time.time()

    StopTime = time.time()
    while GPIO.input(echo_pin) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance


#zend de bytes naar het shift register
def hc595( shift_clock_pin, latch_clock_pin, data_pin, value, delay ):
   GPIO.output(latch_clock_pin,0)
   for x in range(8):
      GPIO.output(data_pin, (value >> x) & 1)
      GPIO.output(shift_clock_pin, 1)
      GPIO.output(shift_clock_pin, 0)
   GPIO.output(latch_clock_pin, 1)
   time.sleep(delay)


#Telt hoeveel vrienden online zijn en returned het aantal bytes
def printOnlineFriends():

    global lamp
    lamp = 0
    steamidlist = []
    # For each friend json item, retrieve the Steam ID of each friend and append it to a list/array
    for i in range(len(friendlist)):
        steamidlist.append(friendlist[i]['steamid'])

    # Convert the list/array to a comma-separated list of Steam user IDs for the API to retrieve.
    joinedsids = ','.join(steamidlist)

    useruri = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={joinedsids}'
    userget = requests.get(useruri).json()['response']

    onlinefrends = []
    for i in range(len(userget['players'])):
        online = userget['players'][i]['personastate']
        if online == 1:
            onlinefrends.append(online)
    lengtelist = len(onlinefrends)
    print(lengtelist)

    if lengtelist == 1:
        lamp = 1
    elif lengtelist == 2:
        lamp = 3
    elif lengtelist == 3:
        lamp = 7
    elif lengtelist == 4:
        lamp = 15
    elif lengtelist == 5:
        lamp = 31
    elif lengtelist == 6:
        lamp = 63
    elif lengtelist == 7:
        lamp = 127
    elif lengtelist >= 8:
        lamp = 255

    return lamp


 # zend de bytes naar de APA102 LED strip die is aangesloten op de clock_pin en data_pin
def apa102_send_bytes(clock_pin, data_pin, bytes):


    count = 0
    for byte in bytes:
        for bit in [byte]:
            count = count + 1
            # print(count, "bit", bit)
            if bit == 1:
                GPIO.output(data_pin, GPIO.HIGH)
            elif bit == 0:
                GPIO.output(data_pin, GPIO.LOW)
            GPIO.output(clock_pin, GPIO.HIGH)
            GPIO.output(clock_pin, GPIO.LOW)


def apa102(clock_pin, data_pin,color):

    nulbytes = [0, 0, 0, 0, 0, 0, 0, 0]  # een byte is 8 bits
    eenbytes = [1, 1, 1, 1, 1, 1, 1, 1]

    apa102_send_bytes(clock_pin, data_pin, nulbytes)
    apa102_send_bytes(clock_pin, data_pin, nulbytes)
    apa102_send_bytes(clock_pin, data_pin, nulbytes)
    apa102_send_bytes(clock_pin, data_pin, nulbytes)

    count = 0
    while count < 16:  # of 14?
        apa102_send_bytes(clock_pin, data_pin, eenbytes)
        for i in range(8):

            apa102_send_bytes(clock_pin, data_pin, color)
        count = count + 1

    apa102_send_bytes(clock_pin, data_pin, eenbytes)
    apa102_send_bytes(clock_pin, data_pin, eenbytes)
    apa102_send_bytes(clock_pin, data_pin, eenbytes)
    apa102_send_bytes(clock_pin, data_pin, eenbytes)


def walk(clock_pin, data_pin, color, n=8):


    for x in range(0, n):
        apa102(clock_pin, data_pin, color)
        time.sleep(0.1)


def GameFriends():

    steamidlist = []
    # For each friend json item, retrieve the Steam ID of each friend and append it to a list/array
    for i in range(len(friendlist)):
        steamidlist.append(friendlist[i]['steamid'])

    # Convert the list/array to a comma-separated list of Steam user IDs for the API to retrieve.
    joinedsids = ','.join(steamidlist)

    useruri = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={joinedsids}'
    userget = requests.get(useruri).json()['response']
    # print(userget)
    games_playing = []

    # online = userget['players']['personaname']
    # print(online)
    for i in range(len(userget['players'])):
        online = userget['players'][i]['personastate']
        if online == 1:
            try:
                games = userget['players'][i]['gameextrainfo']
                print(games)
                games_playing.append(games)
            except:
                pass
    return games_playing




Favourite_game = 'Factorio'
Black = [0, 0, 0]
Green = [0]
FinalLamp = printOnlineFriends()
delay = 0.1
count = 1
preferred_distance = 10
try:

    while True:

        print(f"count = {count}")
        if( GPIO.input( switch_on ) ):
            if count == 0:
                count += 1
        # walk(led_clock_pin, led_data_pin, Black)

        while count == 1:
            FinalLamp = printOnlineFriends()
            hc595(shift_clock_pin, latch_clock_pin, schuif_data_pin, FinalLamp, delay)
            distance = ( sr04( sr04_trig, sr04_echo ))
            being_played = GameFriends()


            print(distance)

            if Favourite_game in being_played:
                if distance < preferred_distance:
                    walk(led_clock_pin, led_data_pin, Black)

                else:
                    walk(led_clock_pin, led_data_pin, Green)


            elif Favourite_game not in being_played:
                walk(led_clock_pin, led_data_pin, Black)



            if distance >= preferred_distance:
                    pwm.ChangeDutyCycle(2.0)  # rotate to 0 degrees
                    time.sleep(0.5)
            else:
                pwm.ChangeDutyCycle(7.5)  # rotate to 90 degrees
                time.sleep(0.5)


            if (GPIO.input(switch_off)):
                if count == 1:
                    count -= 1
                   
                    walk(led_clock_pin, led_data_pin, Black)

            time.sleep(0.5)

        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('Quit')


