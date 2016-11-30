import curses
import serial
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage:')
        print('debug.py <serial device>')
        quit()
    screen = curses.initscr()
    screen.border(0)
    screen.addstr(0,5,'HYTECH RACING 2016 VEHICLE SERIAL DEBUGGER')
    screen.addstr(3,5,'RMS INVERTER')
    screen.addstr(4,5,'UPTIME: ')
    screen.addstr(5,5,'MOTOR TEMP: ')
    screen.addstr(6,5,'TORQUE SHUDDER: ')
    screen.addstr(7,5,'MOTOR ANGLE: ')
    screen.addstr(8,5,'MOTOR SPEED: ')
    screen.addstr(9,5,'ELEC OUTPUT FREQ: ')
    screen.addstr(10,5,'DELTA RESOLVER FILT: ')
    screen.addstr(11,5,'PHASE A CURRENT: ')
    screen.addstr(12,5,'PHASE B CURRENT: ')
    screen.addstr(13,5,'PHASE C CURRENT: ')
    screen.addstr(14,5,'DC BUS VOLTAGE: ')
    screen.addstr(15,5,'INVERTER STATE: ')
    screen.addstr(16,5,'INVERTER ENABLE: ')
    screen.addstr(17,5,'POST FAULT LO: ')
    screen.addstr(18,5,'POST FAULT HI: ')
    screen.addstr(19,5,'RUN FAULT LO: ')
    screen.addstr(20,5,'RUN FAULT HI: ')
    screen.addstr(21,5,'COMMANDED TORQUE: ')
    screen.addstr(22,5,'TORQUE FEEDBACK: ')
    screen.addstr(3,55,'THROTTLE CONTROL UNIT')
    screen.addstr(4,55,'UPTIME: ')
    screen.addstr(5,55,'STATE: ')
    screen.addstr(6,55,'START BUTTON ID: ')
    screen.addstr(3,105,'POWER CONTROL UNIT')
    screen.addstr(4,105,'UPTIME: ')
    screen.addstr(5,105,'STATE: ')
    screen.addstr(6,105,'BMS FAULT: ')
    screen.addstr(7,105,'IMD FAULT: ')
    curses.wrapper(live)
    curses.endwin()

def live(screen):
    ser = serial.Serial(sys.argv[1], 115200)

    incomingLine = ''
    char = screen.getch()
    while char != ord('q') and char != ord('Q'):
        char = screen.getch()
        if (ser.inWaiting() > 0):
            incomingLine += ser.read(ser.inWaiting()).decode('ascii')
            if ('\n' in incomingLine):
                updateScreen(screen, incomingLine[0:incomingLine.find('\n')])
                incomingLine = incomingLine[incomingLine.find('\n') + 1:]

def updateScreen(screen, incomingLine):
    if ('RMS Uptime' in incomingLine):
        screen.addstr(4,5,'UPTIME: ')
        #todo finish
    if ('Inverter' in incomingLine):
        screen.addstr(16,5,'INVERTER ENABLE: ' + incomingLine)
        #todo finish
    #todo finish
    screen.refresh()


main()
