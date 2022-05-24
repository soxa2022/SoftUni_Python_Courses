volume_pool = int(input())
flow_pipe_one = int(input())
flow_pipe_two = int(input())
time = float(input())
volume_pipe_one = flow_pipe_one * time
volume_pipe_two = flow_pipe_two * time
volume_total = volume_pipe_one + volume_pipe_two
volume_diff = volume_pool - volume_total
if volume_diff >= 0:
    percent_full = volume_total / volume_pool * 100
    percent_pipe1 = volume_pipe_one / volume_total * 100
    percent_pipe2 = volume_pipe_two / volume_total * 100
    print(f"The pool is {percent_full:.2f}% full. Pipe 1: {percent_pipe1:.2f}%. Pipe 2: {percent_pipe2:.2f}%.")
else:
    volume_diff = abs(volume_diff)
    print(f"For {time:.2f} hours the pool overflows with {volume_diff:.2f} liters.")
