import ev3dev.ev3 as ev3

leftM = ev3.LargeMotor('outC')
rightM = ev3.LargeMotor('outB')

leftM.speed_sp = 200
rightM.speed_sp = 200

leftM.run_timed(time_sp = 3000)
rightM.run_timed(time_sp = 3000)

leftM.wait_until_not_moving()

leftM.speed_sp = 200
rightM.speed_sp = -200

leftM.run_timed(time_sp = 1700)
rightM.run_timed(time_sp = 1700)

leftM.wait_until_not_moving()

leftM.speed_sp = 200
rightM.speed_sp = 200

leftM.run_timed(time_sp = 3000)
rightM.run_timed(time_sp = 3000)

leftM.wait_until_not_moving()
ev3.Sound.speak("Done!")