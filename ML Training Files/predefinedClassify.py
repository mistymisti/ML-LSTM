import csv

r = csv.reader(open('trainingdata.csv'))

lines = list(r)

for i in range(len(lines)):
    memtotal = int(lines[i][6])
    memavail = int(lines[i][7])
    busythreads = int(lines[i][8])
    totalthreads = int(lines[i][9])
    cpuusage = int(lines[i][10])
    jvmcpuusage = int(lines[i][11])

    memoryIssue = memavail <= 0.30 * memtotal
    threadsIssue = busythreads == totalthreads
    cpuIssue = (cpuusage - jvmcpuusage) < 10

    if( memoryIssue or threadsIssue or cpuIssue ):
        lines[i].insert(13,"1")
    else:
        lines[i].insert(13,"0")

writer = csv.writer(open('traindata_final.csv', 'w'))
writer.writerows(lines)
