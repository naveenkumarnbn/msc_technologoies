# What is testing ?
    1. Testing is a process to verify the functionality of a software appliction.
    2. Testing used to identify the defects to ensure that the product is defect free and relese quality product.

# What is manual testing ?
    1. If we do any testing with human interaction without using any automation tool or script that testing is called manual testing.
    2. In manual testing the tester takes over the roles of an end user and tests a software to identify any unexpected behavior or bug.

# What is automation testing ?
    1. If tester use any automation tool, software or scripts to test software application that testing is called automation testing.

# What is the use of automation testing ?
    1. Automation testing is used to rerun the test scenarios quickly and repeatedly.
    2. It is used for regression testing.
    3. Using automation, we can test application on load.
    4. We can do Performance and stress testing.
    5. It increases the test coverage and improve accuracy.
    6. Save time, resource and cost compare to manual testing.

# When you deside to go automation ?
    1. When test case is clear and stable.
    2. Tests that are impossible to perform manually(Load and stress testing).
    2. Results are predictable.
    3. To run same test case multiple times.

# When Automation is not PREFERRED ?
    1. When requirements are keep changing.
    2. To check usability or look-and-feel.
    3. application is still being developed and evolving / changing frequently.
    4. If run test case only once and not running again.
    5. For application functions that are extremely complex, test automation may be a major challenge (time & cost investment outweighs the benefit)

# What are the testing levels or software testing levels ?
    1. Unit Testing
    2. Integration Testing
    3. System Testing
    4. Acceptance Testing

# What is unit testing ?
    1. Testing the individual units of a software. 
    2. The purpose is to validate that each unit of the software performs as designed.
    3. This testing done by developer.

# What is Integration testing ?
    1. Testing after combined individual units as a group.
    2. The purpose of this level of testing is to expose faults in the interaction between integrated units.
    3. This teting done by Tester.

# What is System Testing ?
    1. Testing entire system after integrated all units. 
    2. The purpose of this test is to vreify all application specified features.
    3. This testing done by tester.

# What is User Acceptance Testing ?
    1. The major aim of this test is to confirm application is working or not as end user requirementes.
    2. Acceptance testing is basically done by the user or customer.

    ## Example for testing levels or software testing
        1. During the process of manufacturing a ball pen.
        2. The cap, the body, the tail, the ink and the ballpoint are produced separately, and every unit tested separately that is called Unit testing.
        3. When two or more units ready they assembled and will do integration testing. 
        4. When complete all units integration then system testing is performed.
        5. Acceptance testing will do on client location.

# What are the testing types ?
    1. Functional Testing 
        '''Functional testing is testing the ‘Functionality’ of a software or an application.
        It tests the behavior of the software. Based on the requirement of the client'''
        * Unit Testing
        * Integration Testing
        * System Testing
        * Beta/Acceptance Testing
        * Sanity Testing
        * Smoke Testing
        * Regression Testing

    2. Non Functional Testing
        ''' There are some aspects which are complex such as Performance of an application
        2. This testing checks the Quality of the software to be tested. Quality majorly depends on Time, Accuracy, Stability, correctness and durability of a product under various adverse circumstances.'''
        * Performance Testing
        * Load Testing
        * Stress Testing
        * Security Testing
        * Compatibility Testing
        * Recovery Testing
        * Reliability Testing
        * Usability Testing

# Regression Testing ?
    1. In regression testing If we change any code or module, we have to check entire functionality of application to make sure whether it is working or not properly after code change.

    # Types of Regression Testing 

    Often, regression testing is done through several phases of testing. It is for this reason, that there are several types of regression testing, such as: 

    Unit regression – Unit regression testing, executed during the unit testing phase, tests the code as a single unit. It has a narrow and focused approach, where complex interactions and dependencies outside the unit of code in question are temporarily blocked. 

    Partial regression – Partial regression is performed after impact analysis. In this testing process, the new addition of the code as a unit is made to interact with other parts of older existing code. Doing so determines that even with code modification, the system functions in silos as desired.

    Complete regression – Complete regression testing is often carried out when the code changes for modification or the software updates seep way back into the roots. It is also carried out in case there are multiple changes to the existing code. It gives a comprehensive view of the system as a whole and weeds out any unforeseen problems. A sort of a “final” regression testing is implemented to certify that the build (new lines of code) has not been altered for a period of time. This final version is then deployed to the end users. 

# What is Sanity testing ?
    1. Sanity test is a narrow regression test it focus one or few areas of functionality. We make this testing when we have less time.

# Smoke Testing ?
    1. Smoke testing covers most of major functions of software but none of them in depth.
    2. The result of this test is used to decide whether to proceed with further testing if smoke testing pass, we go ahead with further testing if it fails, we have to stop next testing phase and ask for a new build with the required fixes.
    3. It is used to save time before going regression, integration and acceptance tests.
    4. In this testing we test very essential features of applications and hardware setups.

# What is Performance Testing ?
    1. Performance Testing is defined as a type of software testing to ensure software applications will perform well under their expected workload.
    ## The focus of Performance Testing is checking a software program's
    Speed - Determines whether the application responds quickly
    Scalability - Determines maximum user load the software application can handle.
    Stability - Determines if the application is stable under varying loads

# What is Load Testing ?
    1. Load testing is testing that checks with a limit how systems working under a heavy number of concurrent users performing transactions over a certain period of time.

# What is Stress Testing ?
    1. Stress testing is testing that checks the upper limits of your system by testing it under extreme loads. The testing examines how the system behaves under heavy loads, and how it recovers when going back to normal usage.

# What is Scalability Testing ?
    1. Scalability Testing is a type of non-functional testing.
    2. The main objective of scalability testing is to determine the software application’s effectiveness in “scaling up” to support an increase in user load.
    Scalability Testing Attributes:
        A. Response Time
        B. Performance measurement with number of users
        C. CPU Usage
        D. Memory Usage
        E. Network Usage

# What Alpha Testing ?
    1. Alpha testing is a type of acceptance testing to identify all possible issues/bugs before releasing the product to end user.
    2. Alpha testing we use black box and white box techniques.
    3. Alpha testing performed by Testers  who are usually internal employees of the organization.
    4. Alpha Testing performed at developer's site.

# What is Beta Testing ?
    1. Beta testing is performed by Clients or End Users who are not employees of the organization.
    2. Beta testing is performed at a client location or end user of the product.
    3. Beta Testing typically uses Black Box techniques.

# What is black box testing ?
    1. In Black box testing the tester doesn't required to know the internal coding/ design and implementation of the application.
    2. Tester need to check only functionality of the application.

# What is White box testing ?
    1. In white box testing the tester should know internal structure and code to test the application internal structure also.

# What is Gray box testing ?
    1. Gray Box Testing is a software testing technique which is a combination of Black Box Testing technique and White Box Testing technique.
    2. In Gray box testing the tester should know partially internal structure, design and implementation.

# What is Software Development Life Cycle(SDLC) ?
    ## The entire SDLC process divided into the following stages.
    Phase 1: Requirement collection and analysis
    Phase 2: Design:
    Phase 3: Coding:
    Phase 4: Testing:
    Phase 5: Installation/Deployment:
    Phase 6: Maintenance

# What is Testing Development Life Cycle(TDLC) ?
    ## The entire TDLC process divided into the following stages.
    1. Test Paln
    2. Identify Test Scenarios
    3. Preparing Test Cases
    4. Executing Test cases
    5. Identify Defects
    6. Reporting Defects
    7. Tracking Defects
    8. Close test

# What is Bug Life Cycle ?
    * The bug has a life cycle in software development process. The bug should go through the life cycle to be closed. 
    ## The life cycle of bug 
    1. New:  When a defect is logged and posted for the first time. Its state is given as new.

    2. Assigned:  After the tester has posted the bug, the lead of the tester approves that the bug is genuine, and he assigns the bug to corresponding developer and the developer team. Its state given as assigned.

    3. Open:  At this state the developer has started analyzing and working on the defect fix.

    4. Fixed:  When developer makes necessary code changes and verifies the changes then he/she can make bug status as ‘Fixed’ and the bug is passed to testing team.

    5. Retest:  At this stage the tester does the retesting of the changed code which developer has given to him to check whether the defect got fixed or not.

    6. Verified:  The tester tests the bug again after it got fixed by the developer. If the bug is not present in the software, he approves that the bug is fixed and changes the status to “verified”.

    7. Closed:  Once the bug is fixed, it is tested by the tester. If the tester feels that the bug no longer exists in the software, he changes the status of the bug to “closed”. This state means that the bug is fixed, tested and approved.

# What tool you used for Bug tracking ?
    1. I am using Jira toll for bug tacking

# Difference between priority and severity ?
    * SEVERITY
        a. How impact bug on the application
        b. Depending in functionality 
        c. Set by the tester
        d. Severity Levels ( Critical, Major, Minor, Cosmetic and Enhancement )
    * PRIORITY
        a. Priority define how soon developer need to fix bug
        b. Depending on time
        c. Set by the developer
        d. Priority Levels(p1,p2,p3,p4,p5)
    ## https://www.quora.com/What-is-severity-and-priority-in-testing-with-examples

# What is Error, Bug, Defect and Failure ?
    * Error
    1. We can’t compile or run a program due to coding mistake in a program. If a developer unable to successfully compile or run a program then they call it as an error.

    * Bug
    1. If testers find any mismatch in the application/system in testing phase then they call it as Bug.
    2. As I mentioned earlier, there is a contradiction in the usage of Bug and Defect. People widely say the bug is an informal name for the defect.

    * Defect
    1. The difference between the actual result and expected result is known as defect.
    2. If a developer finds an issue and corrects it by himself in the development phase then it’s called a defect.

    * Failure
    1. Once the product is deployed and customers find any issues then they call the product as a failure product. After release, if an end user finds an issue then that particular issue is called as failure

# What is Software Testing Methodology ?
    1. Software testing methodologies are the various strategies or approaches used to test an application to ensure it behaves and looks as expected.

# Types of  Software Testing Methodologies ?
 ''' 
 YOUTUBE LINK ==> https://www.youtube.com/watch?v=9TycLR0TqFA 
                  https://www.youtube.com/watch?v=WjwEh15M5Rw
 
 ''' 
    1. Waterfall Model
        1. Waterfall module is a simple and traditional project management 
        2. This is a sequential software development model.

    2. Agile Model
        '''
        The most widely-used Agile methodologies include:
        Agile Scrum Methodology
        Lean Software Development
        Kanban
        Extreme Programming (XP)
        Crystal
        Dynamic Systems Development Method (DSDM)
        Feature Driven Development (FDD)
        '''
        1. AGILE methodology is a continuous iteration of development and testing throughout the software development lifecycle of the project.
        2. In Agile the entire project will de

# What is the duration of a each sprint ?
    1. my sprint is two weeks.

# What is Daily Stand-Up meeting ?
    1. As agile process we have a daily stand-up meeing for almost 15 minutes.
    2. We have stand-up call every day 10AM.
    3. In this meeting i will tell , What was done yesterday,  What is plan for today work and discuss if i have any issues.

# What is retrospective meeting ?
    1. In retrospective meeting we discuss What we did well in last sprint, What we did not do well,  What we will work on doing better.
    2. We have retrospective meeting for every relese.
    3. It is used to improve work process.

# What is difference between Epic, User stories & Tasks ?
    User Stories:User Stories defines the actual business requirement. Generally created by Business owner.

    Task: To accomplish the business requirements development team create tasks.

    Epic: A group of related user stories is called an Epic.

# What is framewrok ?
    1. A Framewrork is a set of inbult functions to achive particular task.

# What is Data driven framework ?
    1. In Data driven framework tests are run multiple times with different values which get form external files.
    2. The test cases receive required test data from the external files(CSV, Excel, Yaml, XML, Json).

# What is Keyword driven framework ?
    ## https://www.guru99.com/keyword-driven-testing.html
    1. A keyword-driven framework is a table-driven testing or action word based testing.
    2. In Keyword Driven Testing, first identify a set of keywords and then associate an action. like Open browser, do click and enter text, get text then close browser.

# What is Hybrid driven framework ?
    1. Hybrid Test framework is a concept where we are using the advantage of both Keyword and Data-driven framework.
