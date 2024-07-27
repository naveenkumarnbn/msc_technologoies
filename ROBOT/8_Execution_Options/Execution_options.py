# To know robot version
    robot --version

# To run particular test case and Test cases
    robot -t Testcase:1 TEST_SUITE.robot
    robot -t Testcase:1 -t Testcase:3 TEST_SUITE.robot

## # [Tags] 
1. Using tags we can categorize(group) test cases like (sanity, smoke, regression).
2. With tags, we can include or exclude test cases to execute.
    # TO run a test case based on tag
        robot -i windows TEST_SUITE.robot

    # TO run all test cases except given tag
        robot -e test2 TEST_SUITE.robot

# paasing values to variable through command line =>
    robot -v NAME:10 -v EID:34 TEST_SUITE.robot

# Change logs path ==> 
    robot -d C:\INSTITUTE_COURSES\INST\2_ONLINE_CLASS\2_ROBOT\logs TEST_SUITE.robot




