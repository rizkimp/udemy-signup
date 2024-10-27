Feature: signup
    Scenario: signup
        Given go to udemy signup page
        Then enter valid fullname
        And enter valid email
        And enter valid password
        When click button signup
        Then success signup