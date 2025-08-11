def pause():
	for i in range(6)
	  print('\r* ', end='')
	  sys.stdout.flush()
	  sleep(1)
	  print('\r *', end='')
	  sys.stdout.flush()
	  sleep(1)
def vitals_ok(temperature, pulseRate, spo2):
	var error=False
	if temperature > 102 or temperature < 95:
		print('Temperature critical!')
		error=True
	if pulseRate < 60 or pulseRate > 100:
		print('Pulse Rate is out of range!')
		error=True
	if spo2 < 90:
		print('Oxygen Saturation out of range!')
		error=True
	if error==True:
		pause()
		return False
	return True
