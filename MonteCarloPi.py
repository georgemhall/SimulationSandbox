# A multi-threaded monte carlo simulation for computing pi
import threading, time, math, random, Queue

def PiSolver(numThrows, hits_queue):
    circle_points = 0
    for x in range(0, numThrows, 1):
        randX = (random.random() * 2) - 1
        randY = (random.random() * 2) - 1
        distance = math.hypot(randX, randY)
        if(distance < 1):
            circle_points += 1
    hits_queue.put(circle_points)

if __name__ == '__main__':
    result_queue = Queue.Queue()
    hits = 0
    total_throws = 100000
    num_threads = 4
    throws_per_thread = total_throws / num_threads

    for x in range(num_threads):
        # Create a new thread targeting the PiSolver method and a queue for storing results
        mythread = threading.Thread(PiSolver(throws_per_thread, result_queue))
        mythread.start()
        mythread.join()
        hits += result_queue.get()
    print 4.0*hits/(num_threads*throws_per_thread)
