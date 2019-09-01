import matplotlib.pyplot as plt
import time
from sympy import pi
import os
import math

powers = []
times = []

def nextlog(i):
    if i == 0:
        i+=1
    else:
        r=math.log10(i)
        s=int(math.log10(i))
        if r == s:
            i*=2
        else:
            i+=10**s
    return i
def durationcompute(d,starttime):
    i=0
    while time.time()<=starttime+d:
        print(i)
        start = time.process_time()
        2**i
        end = time.process_time()
        powers.append(i)
        duration = end-start
        times.append(duration)
        #i=nextlog(i)
        i+=50000000000

def powercompute(n):
    i=0
    while i <= n:
        print(i)
        start = time.process_time()
        2**i
        end = time.process_time()
        powers.append(i)
        duration = end-start
        times.append(duration)
        i=nextlog(i)

userchoice = input('Do you want to run according for a certain duration or up to a certain power ? (d/p)')
if userchoice == 'd':
    duration = int(input('How long do you want to compute (in seconds) ?'))
    os.system('date')
    print('Computing...')
    startall = time.time()
    durationcompute(duration, startall)
elif userchoice == 'p':
    maxpower = int(input('Which power of 2 would you like to reach ?'))
    os.system('date')
    print('Computing...')
    startall = time.time()
    powercompute(maxpower)

#os.system('nmcli radio wifi off')
#print('Wifi turned off')

endall = time.time()
os.system('date')

#os.system('nmcli radio wifi on')
#print('Wifi turned back on')


k=1
while os.path.exists('./results_' + str(k)):
    k+=1

print('Creating path ./results_{}'.format(k))
os.system('mkdir results_' + str(k))
print('Changing directory')
os.chdir('results_' + str(k))

del(k)

upperpower = int(math.log10(powers[-1]))
size = 1
for p in range(1,upperpower+1):
    size += 9*p

size+=(powers[-1]/10**upperpower)*upperpower
size+=len(powers)



print('List is {} elements long. The first file will be about {} bytes. The second will be larger (about {} bytes)'.format(len(powers), size, size*3.5))

print('Writing list elements')

with open('powers.txt', 'w') as powersfile:
    for number in powers:
        powersfile.write('%s\n' % number)

print('Powers done')

with open('times_poweroftwo.txt', 'w') as times_poweroftwo:
    for time in times:
        times_poweroftwo.write('%s\n' % time)

print('Times done')

print('Creating log')
with open('log.txt', 'w') as log:
    log.write(str(endall-startall))


print('Creating log y plot')
plt.yscale('log')
plt.xscale('linear')
plt.plot(powers, times, 'ro')
plt.ylabel('Computation time (log)')
plt.xlabel('Digits')
plt.savefig('powers_log_y.png')

print('Creating log x plot')
plt.yscale('linear')
plt.xscale('log')
plt.plot(powers, times, 'ro')
plt.ylabel('Computation time')
plt.xlabel('Digits (log)')
plt.savefig('powers_log_x.png')

print('Creating plot')
plt.yscale('linear')
plt.xscale('linear')
plt.plot(powers, times, 'ro')
plt.ylabel('Computation time')
plt.xlabel('Powers of 2')
plt.savefig('powers.png')
plt.show()

print('Done')
