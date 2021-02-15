import threading

class AlreadyRunning(Exception):
    pass


class IntervalNotValid(Exception):
    pass


class setInterval():
    def __init__(self, func=None, sec=None, args=[], autostart=True):
        self.running = False
        self.func = func  # the function to be run
        self.sec = sec            # interval in second
        self.Return = None  # The returned data
        self.args = args
        self.runOnce = None  # asociated with run_once() method
        self.runOnceArgs = None   # asociated with run_once() method

        if (func is not None) and (sec is not None) and autostart:
            self.running = True

            if (not callable(func)):
                raise TypeError("non-callable object is given")

            if (not isinstance(sec, int) and not isinstance(sec, float)):
                raise TypeError("A non-numeric object is given")

            self.TIMER = threading.Timer(self.sec, self.loop)
            self.TIMER.start()

    def start(self):
        if (not self.running):
            if (not self.isValid()):
                raise IntervalNotValid("The function and/or the " +
                                       "interval hasn't provided or invalid.")
            self.running = True
            self.TIMER = threading.Timer(self.sec, self.loop)
            self.TIMER.start()
        else:
            raise AlreadyRunning("Tried to run an already run interval")

    def stop(self):
        self.running = False

    def isValid(self):
        if (not callable(self.func)):
            return False

        cond1 = not isinstance(self.sec, int)
        cond2 = not isinstance(self.sec, float)
        if (cond1 and cond2):
            return False
        return True

    def loop(self):
        if (self.running):
            self.TIMER = threading.Timer(self.sec, self.loop)
            self.TIMER.start()
            function_, Args_ = self.func, self.args

            if (self.runOnce is not None):  # someone has provide the run_once
                runOnce, self.runOnce = self.runOnce, None
                result = runOnce(*(self.runOnceArgs))
                self.runOnceArgs = None

                # if and only if the result is False. not accept "None"
                # nor zero.
                if (result is False):
                    return  # cancel the interval right now

            self.Return = function_(*Args_)

    def change_interval(self, sec):

        cond1 = not isinstance(sec, int)
        cond2 = not isinstance(sec, float)
        if (cond1 and cond2):
            raise TypeError("A non-numeric object is given")

        # prevent error when providing interval to a blueprint
        if (self.running):
            self.TIMER.cancel()

        self.sec = sec

        # prevent error when providing interval to a blueprint
        # if the function hasn't provided yet
        if (self.running):
            self.TIMER = threading.Timer(self.sec, self.loop)
            self.TIMER.start()

    def change_next_interval(self, sec):

        if (not isinstance(sec, int) and not isinstance(sec, float)):
            raise TypeError("A non-numeric object is given")

        self.sec = sec

    def change_func(self, func, args=[]):

        if (not callable(func)):
            raise TypeError("non-callable object is given")

        self.func = func

        if args is not None:
            self.args = args

    def change_argument(self, newArgument=[]):
        self.args = newArgument

    def run_once(self, func, args=[]):
        self.runOnce = func
        self.runOnceArgs = args

    def get_return(self):
        return self.Return