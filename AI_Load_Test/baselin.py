# Import required libraries
import requests          # Used to send HTTP requests to the API
import time              # Used to measure request time (latency)
import statistics        # Used to calculate performance metrics

# API endpoint to test
URL = "http://127.0.0.1:8005/notes"

# List to store latency values (in milliseconds)
latencies = []

# Send 50 GET requests to the API
for _ in range(50):
    # Record start time
    start = time.time()
    
    # Send GET request to the API
    r = requests.get(URL)
    
    # Record end time
    end = time.time()
    
    # Calculate latency in milliseconds and store it
    latencies.append((end - start) * 1000)

# Print performance analysis
print("Average Latency:", statistics.mean(latencies), "ms")      # Mean response time
print("Min Latency:", min(latencies), "ms")                      # Fastest response
print("Max Latency:", max(latencies), "ms")                      # Slowest response
print("Std Deviation:", statistics.stdev(latencies), "ms")       # Consistency of response times