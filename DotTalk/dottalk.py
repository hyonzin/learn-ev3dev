from time import sleep
import pprint
from ev3dev.ev3 import *
import ev3dev.fonts as fonts
import hbcvt

class DotTalk(object):

    HANGUL = "hyonzin: Hello~ :D"
    BRAILLE = hbcvt.h2b.text(HANGUL)
    IS_UPDATED = True

    def __init__(self):
        super(DotTalk, self).__init__()
        self.stick = [0, 0, 1, 0, 1, 1, 1, 0, 0, 0]
        self.hangul = ""
        self.braille = []
        self.hangul_serial = []
        self.braille_serial = []
        self.b_cur = 0
        self.b_len = 0
        self.step = 41
        self.left_move_to = 0
        self.right_move_to = 0
        self.left_direction = "back"
        self.right_direction = "back"
        self.mt_speed = 100

        try:
            self.lcd = Screen()
            self.btn = Button()
            self.btn.on_up = self.up
            self.btn.on_down = self.down
            self.btn.on_left  = self.left
            self.btn.on_right = self.right

            self.mt_large_left   = LargeMotor ('outD')
            self.mt_large_right  = LargeMotor ('outA')
            self.mt_medium_right  = MediumMotor('outC')
            self.mt_medium_left = MediumMotor('outB')

        except Exception as e:
            print(e)

    def run(self):
        self.mt_reset()
        while True:
            if DotTalk.IS_UPDATED:
                DotTalk.IS_UPDATED = False
                self.hangul = DotTalk.HANGUL
                self.braille = DotTalk.BRAILLE

                self.hangul_serial = []
                self.braille_serial = []
                for word in self.braille:
                    for han in word[1]:
                        for br in han[1]:
                            self.hangul_serial.append(han[0])
                            self.braille_serial.append(br)
                self.b_cur = 0
                self.b_len = len(self.hangul_serial)

                self.put_down()
                self.set_left(self.braille_serial[self.b_cur][0:3])
                self.set_right(self.braille_serial[self.b_cur][3:6])
                self.put_up()

                print("DotTalk is running >", self.hangul)
            self.show_lcd()
            self.btn.process()
            sleep(0.001)

    def mt_reset(self):
        DotTalk.HANGUL = "hyonzin: Hello~ :D"
        DotTalk.BRAILLE = hbcvt.h2b.text(DotTalk.HANGUL)
        DotTalk.IS_UPDATED = True

        self.left_move_to = 0
        self.right_move_to = 0
        self.left_direction = "back"
        self.right_direction = "back"

        self.mt_medium_right.run_timed(time_sp=1000, speed_sp=50, stop_action="brake");
        sleep(0.3)
        self.mt_medium_left.run_timed(time_sp=1000, speed_sp=50, stop_action="brake");
        self.mt_medium_right.wait_while('running')
        self.mt_medium_left.wait_while('running')
        # sleep(1)
        self.mt_large_left.run_to_rel_pos(position_sp=350, speed_sp=100, stop_action="brake")
        self.mt_large_right.run_to_rel_pos(position_sp=350, speed_sp=100, stop_action="brake")
        self.mt_large_left.wait_while("running")
        self.mt_large_right.wait_while("running")
        sleep(3)
        self.mt_medium_right.reset()
        self.mt_medium_left.reset()
        self.mt_large_left.reset()
        self.mt_large_right.reset()

    def put_up(self):
        if len(self.mt_large_left.state) > 0 and self.mt_large_left.state[0] == 'running':
            self.mt_large_left.wait_while("running")
        if len(self.mt_large_right.state) > 0 and self.mt_large_right.state[0] == 'running':
            self.mt_large_right.wait_while("running")
        self.mt_medium_left.run_to_abs_pos(position_sp=-24, speed_sp=50, stop_action="brake")
        sleep(0.3)
        self.mt_medium_right.run_to_abs_pos(position_sp=-34, speed_sp=50, stop_action="brake")

    def put_down(self):
        self.mt_medium_right.run_to_abs_pos(position_sp=0, speed_sp=50, stop_action="brake")
        sleep(0.3)
        self.mt_medium_left.run_to_abs_pos(position_sp=0, speed_sp=50, stop_action="brake")
        sleep(0.4)

    def set_left(self, b_):
        b = b_.copy()
        move_to = self.find_dst(self.stick, b) * -self.step

        if move_to == self.left_move_to:
            return

        if self.left_direction == "go" and move_to > self.left_move_to:
            self.left_direction = "back"
        elif self.left_direction == "back" and move_to < self.left_move_to:
            self.left_direction = "go"

        self.left_move_to = move_to

        if self.left_direction == "go":
            move_to += 5
        # else:
        #     pass

        self.mt_large_left.run_to_abs_pos(position_sp=move_to, speed_sp=self.mt_speed, stop_action="brake")

    def set_right(self, b_):
        b = b_.copy()
        b.reverse()
        move_to = self.find_dst(self.stick, b) * -self.step

        if move_to == self.right_move_to:
            return

        if self.right_direction == "go" and move_to > self.right_move_to:
            self.right_direction = "back"
        elif self.right_direction == "back" and move_to < self.right_move_to:
            self.right_direction = "go"

        self.right_move_to = move_to

        if self.right_direction == "go":
            move_to -= 10
        elif self.right_direction == "back":
            move_to -= 20

        self.mt_large_right.run_to_abs_pos(position_sp=move_to, speed_sp=self.mt_speed, stop_action="brake")

    def up(self, state):
        if state:
            pass
            # self.put_up()
            # self.mt_large_left.run_to_rel_pos(position_sp=40, speed_sp=30, stop_action="brake")

    def down(self, state):
        if state:
            self.mt_reset()
            # self.put_down()
            # self.mt_large_left.run_to_rel_pos(position_sp=-40, speed_sp=30, stop_action="brake")

    def left(self, state):
        if state:
            if self.b_cur > 0:
                self.b_cur -= 1
                self.put_down()
                self.set_left(self.braille_serial[self.b_cur][0:3])
                self.set_right(self.braille_serial[self.b_cur][3:6])
                self.put_up()

    def right(self, state):
        if state:
            if self.b_cur < self.b_len - 1:
                self.b_cur += 1
                self.put_down()
                self.set_left(self.braille_serial[self.b_cur][0:3])
                self.set_right(self.braille_serial[self.b_cur][3:6])
                self.put_up()

    def show_lcd(self):
        char_per_line = 15
        lcd_str = ""
        n_line = 0
        n_char = 0
        is_printing_name = True
        self.lcd.clear()
        lcd_str = "{}/{} {}: {}{}{} {}{}{}".format( \
            self.b_cur+1, self.b_len,
            self.hangul_serial[self.b_cur],
            self.braille_serial[self.b_cur][0], self.braille_serial[self.b_cur][1], \
            self.braille_serial[self.b_cur][2], self.braille_serial[self.b_cur][3], \
            self.braille_serial[self.b_cur][4], self.braille_serial[self.b_cur][5], )
        self.lcd.draw.text((0, 0), lcd_str, font = fonts.load('luBS18'))
        lcd_str = ""

        for char in self.hangul:
            lcd_str += char
            n_char += 1
            if n_char >= char_per_line:
                n_line += 1
                self.lcd.draw.text((0, n_line * 20), lcd_str, font = fonts.load('luBS18'))
                lcd_str = ""
                n_char = 0
            if is_printing_name and char == ":":
                n_char = char_per_line
                is_printing_name = False
        if n_char > 0:
            n_line += 1
            self.lcd.draw.text((0, n_line * 20), lcd_str, font = fonts.load('luBS18'))
        self.lcd.update()

    def find_dst(self, stick, b):
        for i in range(len(stick)-2):
            if stick[i] == b[0] and stick[i+1] == b[1] and stick[i+2] == b[2]:
                return i
