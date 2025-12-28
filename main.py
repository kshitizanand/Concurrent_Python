import time
import threading

def calculate_sum_square(num):
    sum_of_squares = 0
    for i in range(num):
        sum_of_squares += i**2
    print (sum_of_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    calc_start_time = time.time()

    current_threads = []
    for i in range(5):
        maximum_value = (i + 1) * 1_000_000
        t = threading.Thread(target=calculate_sum_square, args=(maximum_value, ))
        t.start()
        current_threads.append(t)

    for current_thread in current_threads:
        current_thread.join()

    print ("calulating sum of squares took: ", round(time.time() - calc_start_time, 1))
    sleep_start_time = time.time()
    current_threads = []
    for seconds in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(seconds, ))
        t.start()
        current_threads.append(t)

    for current_thread in current_threads:
        current_thread.join()

    print("slept for: ", round(time.time() - sleep_start_time, 1))
if __name__ == '__main__':
    main()