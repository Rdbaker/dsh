"""
    Ryan Baker
    rdbaker

    Python module to test throughput for the dsh program
"""
import subprocess
import timeit


def simple_connection():
    subprocess.call(['./bin/dsh', '-s', '54.209.124.158', '-c', '"pwd"'])


def long_conn():
    subprocess.call(['./bin/dsh', '-s', '54.209.124.158', '-c ', '"rm -f 2096-MB-fake-file.txt && fakefile 2096"'])


def setup():
    pass
    # subprocess.call(['function fakefile { perl -e "print \'0\' x 1024 x 1024 x $1" > $1-MB-fake-file.txt; }'])
    # subprocess.call(['./bin/dsh', '-s 54.209.124.158', '-c \'function fakefile { perl -e "print \'0\' x 1024 x 1024 x $1" > $1-MB-fake-file.txt; }'])


if __name__ == "__main__":
    # make the binary files
    st = subprocess.call(['make'])
    if st == 1:
        print 'Something went wrong with "make"'
        exit(1)
    # set up the fakefile function
    setup()
    conn_avg = timeit.timeit('simple_connection()', number=10000, setup="from __main__ import simple_connection")
    print "Network time for a simple connection (10,000 tries): ", conn_avg
    # long_conn_avg = timeit.timeit('long_conn()', number=100)
