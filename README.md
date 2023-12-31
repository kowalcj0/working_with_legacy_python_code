https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/


## Quoutes

“Legacy Code is code without tests”

"Changes in a system can be made in two primary ways. 
I like to call them Edit and Pray and Cover and Modify."


## Summary

### First, add tests, then do your changes
When code is not tested, how do you know you didn’t break anything?
You need feedback. Automated feedback is the best. 
Thus, this is the first thing you need to do: write the tests.
Only then you’ll be safe to change the code and refactor.

### Characterization tests
Before you can refactor the code, you need tests. 
Writing tests can be challenging. Especially when code is hard to understand.
> “A characterization test is a test that characterizes the actual behavior of a piece of code.”

### Adding tests: The Legacy Code Dilemma
When we change code, we should have tests in place. To put tests in place, we often have to change code.
Before you change code, you should have tests in place. But to put tests in place, you have to change code.
Change as little code as possible to get tests in place.

The recipe is:

* Identify change points (Seams)
* Break dependencies
    * The two ways this problem manifests itself are difﬁculty instantiating objects in test harnesses and difﬁculty running methods in test harnesses.
    ...there are two reasons to break dependencies: sensing and separation.
        1. Sensing—We break dependencies to sense when we can’t access values our code computes.
        2. Separation—We break dependencies to separate when we can’t even get a piece of code into a test harness to run.
* Write tests
* Make your changes
* Refactor

### What's not a unit test
In short, your test is not unit if:
* it doesn’t run fast (< 100ms / test)
* it talks to the Infrastructure (e.g. a database, the network, the file system, environment variables…)

### Qualities of good unit tests
1. They run fast. (it should run in less than 100ms per test)
    A unit test that takes 1/10th of a second to run is a slow unit test.
    Unit tests run fast. If they don’t run fast, they aren’t unit tests.
    Other kinds of tests often masquerade as unit tests. A test is not a unit test if:

    1. It talks to a database.
    2. It communicates across a network.
    3. It touches the ﬁle system.
    4. You have to do special things to your environment (such as editing conﬁguration ﬁles) to run it.

    Tests that do these things aren’t bad. Often they are worth writing, and you generally
    will write them in unit test harnesses. However, it is important to be able to separate
    them from true unit tests so that you can keep a set of tests that you can run fast
    whenever you make changes.
2. They help us localize problems.


### Seams

Identify Seams to break your code dependencies
To test your code, you need to break these dependencies in the tests.

Therefore, you need to identify Seams.
"A seam is a place where you can alter behavior in your program without editing in that place."

Enabling Point
Every seam has an enabling point, a place where you can make the decision to use one behavior or another.


### Main techniques

#### The Sprout technique

You can Sprout a single method, a whole class or anything that will isolate your new code.

1. Create your code somewhere else.
2. Unit test it.
3. Identify where you should call that code from the existing code: the insertion point.
4. Call your code from the Legacy Code.


#### The Wrap technique

When the change you need to do should happen before or after the existing code, you can also wrap it.

1. Rename the old method you want to wrap.
2. Create a new method with the same name and signature as the old method.
3. Call the old method from the new method.
4. Put the new logic before/after the other method call.



