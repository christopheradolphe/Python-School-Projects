def initialize():
    #Initialize all global variables

    #Total health points individual has gathered; will store positive integers
    global health
    health = 0

    #Total hedons individual has gathered; will store integer values
    global hedons
    hedons = 0

    #Total time in minutes that has surpassed in a given simulation
    #Value will always be >= 0
    global time
    time = 0

    #Total number of stars that have been awarded in a simulation
    #Value will always be >= 0
    global stars
    stars = 0

    #List compiling times in minutes at which stars were awarded
    global star_time_starts
    star_time_starts = []

    #Amount of time that has elapsed since last star was given
    global star_time
    star_time = 0

    #Activity that the last star was awarded towards
    # Will be ' ' , 'running' , 'textbooks', or 'resting'
    global star_activity
    star_activity = ''

    #Amount of continued rest that has elapsed
    #Value will be integer >= 0
    global resting_time
    resting_time = 0

    #Time between the current time and when the user started running
    #Value will be integer >= 0
    global running_time
    running_time = 0

    #Time between the current time and time user started carrying textbooks
    #Value will be integer >= 0
    global textbook_time
    textbook_time = 0

    #Variable storing whether user is bored or not
    #Value will either be True or False
    global bored
    bored = False


def get_cur_hedons():
    #Return number of hedons user has accumulated
    global hedons

    return hedons

def get_cur_health():
    #Return number of health points user has accumulated
    global health

    return health

def star_can_be_taken(activity):
    #Return true or false depending on whether star can be used or not
    #Parameters:
    #   activity is a string; one of 'running', 'textbooks' or 'resting'
    global star_time
    global bored
    global star_activity

    return star_time == 0 and not bored and star_activity == activity

def offer_star(activity):
    #Simulate offering user a star for engaging in "activity"
    # Parameters:
    #     activity is a string; one of 'running', 'textbooks' or 'resting'
    global star_activity
    global star_time
    global stars
    global star_time_starts
    global bored
    global star

    star = True
    star_activity = activity
    star_time = 0
    stars += 1
    star_time_starts.append(time)
    if stars >= 3:
        if star_time_starts[-1] - star_time_starts[-3] < 120:
            bored = True

def check_tired():
    #Determine whether individual is tired
    global resting_time
    global time

    if not time == 0 and resting_time >= 120 or time == 0:
        return False
    else:
        return True

def perform_activity(activity, duration):
    #Simulate user perfroming an activity

    #Parameters: a)activity: string
    #                    -aserts which activity is being performed
    #                    -can only be  "running", "textbooks" or "resting"
    #            b) duration: positive integer
    #                    - length of time acitivity is being performed for
    global health
    global hedons
    global previous_activity
    global time
    global running_time
    global resting_time
    global textbook_time
    global star
    global star_time
    global bored

    if time == 0:
        previous_activity = 'nothing'

    if activity == 'running':
        #Health Points for Running
        if previous_activity == 'running':
            previous_run = running_time
            running_time += duration
            if running_time <= 180:
                health += duration * 3
            else:
                health += (180-previous_run)*(3) + (running_time - 180)*(1)
        else:
            if duration <= 180:
                health += duration * 3
            else:
                health += (180)*(3) + (min - 180)*(1)

        #Hedons for Running
        if duration <= 10 and not check_tired():
            hedons += duration * 2
        if duration > 10 and not check_tired():
            hedons += (20 - (2* (duration - 10)))
        if check_tired():
            hedons -= duration *2

        resting_time = 0
        textbook_time = 0
        running_time += duration
        previous_activity = "running"

    elif activity == 'textbooks':

        #Health Points for carrying textbooks
        health += (duration*2)

        if check_tired():
            hedons -= duration *2

        #Hedons for carrying textbooks
        if not check_tired():
            if duration <= 20:
                hedons += duration
            else:
                hedons += ((20) - (duration-20))




        running_time_time = 0
        textbook_time += duration
        resting_time = 0
        previous_activity = 'textbooks'


    elif activity == 'resting':
        running_time = 0
        textbook_time = 0
        resting_time += duration

        previous_activity = 'resting'
    else:
        return "Not a valid activity"


    if star_can_be_taken(activity):
    #Hedons recieved for doing a star activity
        if duration <= 10:
            hedons += duration * 3
        else:
            hedons += 30
        star_activity = ''

    time += duration
    star_time += duration
    star = False


def most_fun_activity_minute():
    #Return activity that would give most hedons if it was performed for one minute
    global health
    global hedons
    global previous_activity
    global time
    global running_time
    global resting_time
    global textbook_time
    global star
    global star_time
    global bored
    global star_activity

    act_list = ['running', 'textbooks', 'resting']
    hedons_gained = []
    for i in range(len(act_list)):
        current_hedons = get_cur_hedons()
        current_health = get_cur_health()
        current_resting_time = resting_time
        current_running_time = running_time
        current_textbook_time = textbook_time
        current_star_time = star_time
        current_previous_activity = previous_activity
        current_time = time
        current_star_activity = star_activity
        current_star = star

        perform_activity(act_list[i], 1)
        new_hedons = get_cur_hedons()
        change_hedons = new_hedons - current_hedons
        hedons_gained.append(change_hedons)


        hedons = current_hedons
        health = current_health
        resting_time = current_resting_time
        running_time = current_running_time
        textbook_time = current_textbook_time
        star_time = current_star_time
        previous_activity = current_previous_activity
        star_activity = current_star_activity
        time = current_time
        star = current_star

    max_hedons = hedons_gained.index(max(hedons_gained))
    return act_list[max_hedons]
    #What about if its two are tied





if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
    print(get_cur_health()) # 90 = 30 * 3
    print(most_fun_activity_minute()) # resting
    print(get_cur_hedons())
    print(get_cur_health())
    perform_activity("resting", 30)
    print(get_cur_hedons())
    print(get_cur_health())
    offer_star("running")
    print(most_fun_activity_minute()) # running
    perform_activity("textbooks", 30)
    print(get_cur_health())
    #
    print("Sim 1 Ended")
    #
    #sim 2 code
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
    print(get_cur_health()) # 90 = 30 * 3
    print(most_fun_activity_minute()) #resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute()) # running
    perform_activity("textbooks", 30)
    print(get_cur_health()) # 150 = 90 + 30*2
    print(get_cur_hedons()) # -80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health()) # 210 = 150 + 20 * 3
    print(get_cur_hedons()) # -90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health()) # 700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons())  # -430 = -90 + 170 * (-2)
    initialize()
    offer_star("running")
    perform_activity("running", 60)
    offer_star("textbooks")
    perform_activity("running", 59)
    offer_star("running")
    print(bored)


    # initialize()
    # perform_activity("textbooks", 40)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("textbooks", 140)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # offer_star("textbooks")
    # perform_activity("resting", 100)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # offer_star("running")
    # perform_activity("resting", 40)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # offer_star("textbooks")
    # perform_activity("textbooks", 10)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("running", 140)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("resting", 40)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # print(most_fun_activity_minute())
    # perform_activity("textbooks", 90)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("resting", 40)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # offer_star("textbooks")
    # perform_activity("resting", 20)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("running", 80)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("resting", 100)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("resting", 20)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # perform_activity("running", 140)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # perform_activity("running", 30)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("textbooks", 100)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # perform_activity("running", 110)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # offer_star("running")
    # perform_activity("resting", 90)
    # print(get_cur_health())
    # print(get_cur_hedons())

    # initialize()
    # perform_activity("running", 50)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("textbooks", 80)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # offer_star("running")
    # perform_activity("resting", 140)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # perform_activity("running", 50)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("running", 100)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("textbooks", 20)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("resting", 50)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("running", 60)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("textbooks", 110)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # offer_star("textbooks")
    # perform_activity("textbooks", 10)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("running", 140)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # perform_activity("textbooks", 80)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # offer_star("running")
    # print(most_fun_activity_minute())
    # perform_activity("textbooks", 130)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # perform_activity("resting", 50)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # offer_star("running")
    # perform_activity("running", 120)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("textbooks", 80)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # print(most_fun_activity_minute())
    # print(most_fun_activity_minute())
    # print(most_fun_activity_minute())
    # print(most_fun_activity_minute())
    # print(most_fun_activity_minute())

    # initialize()
    # offer_star("textbooks")
    # print(most_fun_activity_minute())  # textbooks
    # offer_star("textbooks")
    # print(most_fun_activity_minute())  # textbooks
    # offer_star("textbooks")
    # print(most_fun_activity_minute())  # running
    #
    # initialize()
    # offer_star("textbooks")
    # print(most_fun_activity_minute())  # textbooks
    # offer_star("textbooks")
    # print(most_fun_activity_minute())  # textbooks
    # offer_star("textbooks")
    # perform_activity("running", 30)
    # print(most_fun_activity_minute())  # resting
    #
    # initialize()
    # offer_star("textbooks")
    # perform_activity("running", 101)
    # print(get_cur_health()) # 303
    # print(get_cur_hedons()) # -162
    # offer_star("textbooks")
    # print(most_fun_activity_minute())  # textbooks
    # perform_activity("textbooks", 20)
    # offer_star("textbooks")
    # print(most_fun_activity_minute())  # textbooks
    #
    # initialize()
    # offer_star("resting")
    # offer_star("textbooks")
    # perform_activity("running", 101)
    # print(get_cur_health()) # 303
    # print(get_cur_hedons()) # -162
    # perform_activity("textbooks", 20)
    # offer_star("textbooks")
    # print(most_fun_activity_minute())  # textbooks
    # perform_activity("textbooks", 20)
    # offer_star("textbooks")
    # print(most_fun_activity_minute())  # textbooks

