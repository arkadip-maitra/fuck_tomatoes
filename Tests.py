import Printer, time

testPoints = [
(176, 204),
(306, 208),
(354, 159),
(218, 134),
(277, 126),
(335, 126),
(246, 189)
]

p = Printer.Printer('COM4', (200,200))
time.sleep(8)
p.writePoint((75, 75))
while 1:
    res = p.packageIsExecuting()
    if 'Count' in res:
        xy = res.split('Count')[1].split('Z')[0].strip().replace('Y:', '').split(' ')[1:]
        x, y = (xy[0], xy[1])
        print(str(x) + '  ' + str(y))