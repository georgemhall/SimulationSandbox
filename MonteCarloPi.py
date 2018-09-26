import threading, time, math, random, Queue

def PiSolver(numThrows, points_queue):
    circle_points = 0
    for x in range(0, numThrows, 1):
        randX = (random.random() * 2) - 1
        randY = (random.random() * 2) - 1
        distance = math.hypot(randX, randY)
        if(distance < 1):
            circle_points += 1
    points_queue.put(circle_points)

if __name__ == '__main__':
    my_queue = Queue.Queue()
    total_throws = 10000000
    ret = 0
    num_threads = 4
    for x in range(num_threads):
        mythread = threading.Thread(PiSolver(total_throws, my_queue))
        mythread.start()
        mythread.join()
        ret += my_queue.get()
        time.sleep(.9)
    print (4.0*ret)/(num_threads*total_throws)
