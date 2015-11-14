import heapq

def fastestFirstSchedulingNoPre(tasks):
    tasks.sort()
    # For additional info about the problem
    s = 0
    for i in range(len(tasks)):
        s += sum(tasks[:i+1])
    print 'avgTime = ', float(s)/len(tasks)
    #Addition info ends here
    return tasks

def fastestFirstSchedulingWithPre(tasks):
    tasks.sort()
    premQ = []
    # For additional info about the problem
    time = 0
    prevTaskTime = 0
    for i in range(len(tasks)):
        currentTime = tasks[i][0]
        prevTaskPending = 0 if (currentTime - time) >= prevTaskTime else prevTaskTime - (currentTime - time)
        #Check to preempt or not
        newCompletionTime = 0
        if prevTaskPending <= task[i][1]:
            #continue with the current task
            #Add the new task to the queue
            premQ.heappush(tasks[i][1])
            #Update the new Completion Time
            newCompletionTime = prevTaskPending
        else:
            #Preempt the current task and run the new task
            newCompletionTime = task[i][1]
            
        time = tasks[i][0]
        #If the current task stops before the previous task
        while i<len(tasks)-1 and time + newCompletionTime < tasks[i+1][0]:
            #Current processing ends before the release of next process
            #So take preempted tasks from priority Q and process them
            time += newCompletionTime
            pTask = heapq.heappop(premQ)
            if pTask < tasks[i+1][0]:
                newCompletionTime = pTask
            else:
                time = tasks[i+1][0]
            
        
        #If current task ends before the next task, call the preempted tasks
        pT = tasks[i][1]
    print 'avgTime = ', float(s)/len(tasks)
    #Addition info ends here
    return tasks
        