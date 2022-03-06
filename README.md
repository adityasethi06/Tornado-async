Tornado is a single threaded, async frameowrk.
We as devs need to make sure that code deos not have any blocking calls as it single threaded.
If there are blocking calls then there's no point in using Tornado as we won't be making use 
of the async features.

In the index.py, there are 2 endpoints.
1. /test-first
2. /test-second

Try running the app: python index.py

Make 2 HTTP calls in the following order

1. localhost:8888/test-first
2. localhost:8888/test-first

Observations

1. the first call has a 15 seconds sleep to mimic an IO call. couroutine call that returns a Future.
    we await the returned Future.
2. When the 2nd call is made we immediately get data back. while the first call is still waiting to   get response. This shows its non-blocking.
3. we get response for the 1st call after 15 seconds.
4. This async feature allows multiple requests to be catered to concurrently. High number of concurrent requests possible.

5. The only limitation here is the resources available on the machine to sustain the TCP connections.
Every TCP connection makes use of some memory on the server. 
6. If we need a high number of concurrent TCP connections we can consider horizontal scaling.
Spinning up more Containers to run our app on diff servers.