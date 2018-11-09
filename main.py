def five_timer_calc(RA,RB,C): # RA and RB in Ohms, C in uF
	time_high = 0.693 * (RA+RB) * (C * 10**-6)
	time_low = 0.693 * RB * (C * 10**-6)
	period = (time_high + time_low) * 100
	frequency = 1/(period/100)
	duty_cycle = (time_high / (period/100)) * 100

	print('Period:', round(period,2), 'ms')
	print('Frequency:', round(frequency),'Hz')
	print('Time High:', round(time_high*100,2), 'ms')
	print('Time Low:', round(time_low*100,2),'ms')
	print('Duty Cycle:', str(round(duty_cycle,1)) + '%')
