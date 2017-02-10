import webbrowser
import time

print('----- Take a Break -----')
print('Programming starting on {}'.format(time.ctime()))
print('It will remind you to take break every 2 hrs.')
for i in range(0,3):
    print('Time to take a break..')
    time.sleep(10)
    webbrowser.open('https://youtu.be/uKhXLRgsJuM?list=FLxqoDYxC90qALER5jVMwL5A')
