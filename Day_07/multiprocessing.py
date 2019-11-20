# from multiprocessing import Process, Queue
import multiprocessing


def f(q):
    q.put([42, None, "Hello"])


if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
