# Cycle Analyser (speedtest) - v0.3
# by: Dylan Dwyer
# ///////////////////////////////

import sys, time, random, comarg

print '{}'.format('Starting Speedtest...') # because Dries told me to ;\

# initialize variables
count = 0
longest_cycle = 0
shortest_cycle = 999999
init_time = time.time()
last_time = 0

# user can adjust the number of prior cycles to average with the -memory flag
memory_size = int(comarg.mode_value('memory', 1000))
recent_times = [0]*memory_size

# recursive method called through recursion called through recursion...
def deep_python(target_depth, **kwargs):
    depth = kwargs.get('depth',0)
    data = kwargs.get('data', [])
    if depth < target_depth:
        data.append(bool(round(random.random(),0)))
        depth+=1
        return deep_python(target_depth, depth=depth, data=data)
    else:
        return data

# main loop - number of cycles controlled by -limit flag
while not comarg.is_mode('limit') or\
      count < int(comarg.mode_value('limit', 10)):
    count+=1
    
    # artificial random delay set by user with -rdelay flag
    if comarg.is_mode('rdelay'):
        random_delay = int(comarg.mode_value('rdelay', 1))
        delay = random.random()*random_delay
        time.sleep(delay)

    # it's pythons all the way down
    test_data = deep_python(700)
        
    # records maximum & minimum cycle time
    now_time = time.time()
    if count == 1:
        diff_time = 0
    else:
        diff_time = now_time - last_time
        shortest_cycle = min(shortest_cycle, diff_time)
    last_time = now_time
    longest_cycle = max(longest_cycle, diff_time)
    
    # computes recent (as defined by user) and total average time per cycle
    recent_times[count % memory_size] = diff_time #ilovemodulo
    recent_average = sum(recent_times)/float(len(recent_times))
    lifetime_average = (time.time()-init_time) / count
    
    # flips units to cycles/sec - really silly how many lines this takes over
    #   pedantic mathematical nonesense there's no easy way to deal with...
    if float(recent_average) == 0:
        recent_average = 'infinity'
    else:
        recent_average = float(1)/float(recent_average)
        
    if float(lifetime_average) == 0:
        lifetime_average = 'infinity'
    else:
        lifetime_average = float(1)/float(lifetime_average)

    # all those zeroes we filled the list with will skew results until they've
    #   been overwritten for the first time.
    if count < memory_size:
        recent_average = "calculating..."
    
    # prints stream of results to console
    print '{} cycles in {} seconds... (high: {} sec) (low: {} sec)'\
          .format(count, time.time()-init_time, longest_cycle, shortest_cycle)
    print '(recent average: {} cycles/sec) (lifetime average: {} cycles/sec)'\
          .format(recent_average, lifetime_average)

#//////////////////////////////////////////////////////////////////////////////
